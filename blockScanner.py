from web3 import Web3
import json
import time
from web3.middleware import geth_poa_middleware
import datetime
import enum
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from threading import Thread

engine = create_engine('sqlite:///db.sqlite3', connect_args={
                       'check_same_thread': False})
Base = declarative_base(engine)

w3BSC = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
w3BSC.middleware_onion.inject(geth_poa_middleware, layer=0)

w3ETH = Web3(Web3.HTTPProvider('https://cloudflare-eth.com/'))
w3ETH.middleware_onion.inject(geth_poa_middleware, layer=0)

w3MATIC = Web3(Web3.HTTPProvider('https://polygon-rpc.com/'))
w3MATIC.middleware_onion.inject(geth_poa_middleware, layer=0)

w3FTM = Web3(Web3.HTTPProvider('https://fantom-mainnet.public.blastapi.io/'))
w3FTM.middleware_onion.inject(geth_poa_middleware, layer=0)

class Tokens(Base):

  __tablename__ = 'listOfTokens_bsctoken'

  id = Column(Integer, primary_key = True)
  created_on = Column(DateTime, default=datetime.datetime.utcnow)
  scannerLink = Column(String)
  exchangerLink = Column(String)
  name = Column(String)
  symbol = Column(String)
  address = Column(String)
  networkName_id = Column(Integer)

  def __init__(self, scannerLink, exchangerLink, name, symbol, address, networkName_id):

    self.scannerLink = scannerLink
    self.exchangerLink = exchangerLink
    self.name = name
    self.symbol = symbol
    self.address = address
    self.networkName_id = networkName_id



class NetworkName(enum.Enum):
  BSC = 1
  ETH = 2
  MATIC = 3
  FANTOM = 4





def loadSession():
  metadata = Base.metadata
  Session = sessionmaker(bind=engine)
  session = Session()
  return session

session = loadSession()

with open('./panABI.json') as file:
  panABI = json.load(file)

with open('./erc20ABI.json') as file:
  erc20ABI = json.load(file)


def scan(provider):
  #Scans method id's in the latest block and returns a list of transaction hashes
  hashes = []
  latestBlock = provider.eth.getBlock('latest', full_transactions = True)
  for i in latestBlock['transactions']:
    if i.input[0:10] in methodIds:
      hashes.append(provider.toHex(i.hash))
  print(len(hashes))
  return hashes

def checkTx(provider, exchLink, aggregLink, networkname, abi):
  #Scans for token contract addresses and adds values to the database
  while True:
    hashes = scan(provider)
    for i in hashes:
      tx = provider.eth.get_transaction_receipt(i)
      contract = provider.eth.contract(address = tx.contractAddress, abi = abi)
      try:
        token = Tokens(exchLink+tx.contractAddress, aggregLink+tx.contractAddress,contract.functions.name().call(), contract.functions.symbol().call(), tx.contractAddress, networkname)

        if token.name == '':
          continue
        else:
          session.add(token)
          session.commit()

      #some contracts have no name or symbol which throws an error, hence why exception continues
      except Exception as e:
        print(e)
        continue

    #networkname = 2 is ETHEREUM which has block time of average 21 seconds.
    #other networks average on 3 seconds
    if networkname == 2:
      time.sleep(21)
    else:
      time.sleep(3)

if __name__ == "__main__":
  bscScanLink = 'https://www.bscscan.com/address/'
  pooCoinLink = 'https://poocoin.app/tokens/'

  ethScanLink = 'https://etherscan.io/address/'
  ethUniSwapLink = 'https://app.uniswap.org/#/swap?outputCurrency='

  maticScanLink = 'https://polygonscan.com/address/'
  maticQuickSwapLink = 'https://quickswap.exchange/#/swap?outputCurrency='

  ftmScanLink = 'https://ftmscan.com/address/'
  ftmSpookySwapLink = 'https://spookyswap.finance/swap?outputCurrency='

  methodIds = ['0x60806040',
  '0x60a06040',
  '0x69d3c21b',
  '0x6818ce40',
  '0x60e06040',
  '0x60c06040',
  '0x61010060',
  '0x61016060',
  '0x210f5dda',
  '0x662386f2']

  test1 = session.query(Tokens).get(870)
  if test1.name == '':
    print('smth')

  threads = [Thread(target=checkTx, args=(w3BSC, bscScanLink, pooCoinLink, NetworkName.BSC.value, panABI,)),
  Thread(target=checkTx, args=(w3ETH, ethScanLink, ethUniSwapLink, NetworkName.ETH.value, erc20ABI,)),
  Thread(target=checkTx, args=(w3MATIC, maticScanLink, maticQuickSwapLink, NetworkName.MATIC.value, erc20ABI,)),
  Thread(target=checkTx, args=(w3FTM, ftmScanLink, ftmSpookySwapLink, NetworkName.FANTOM.value, erc20ABI,))]

  for thread in threads:
    thread.start()

  for thread in threads:
    thread.join()



