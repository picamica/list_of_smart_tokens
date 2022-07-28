from web3 import Web3
import json
import time
from web3.middleware import geth_poa_middleware
import datetime
import enum
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite3')
Base = declarative_base(engine)

w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

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
  POLYGON = 3
  FANTOM = 4


def loadSession():
  metadata = Base.metadata
  Session = sessionmaker(bind=engine)
  session = Session()
  return session

if __name__ == "__main__":
  bscScanLink = 'https://www.bscscan.com/address/'
  pooCoinLink = 'https://poocoin.app/tokens/'

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

  with open('./panABI.json') as file:
    panABI = json.load(file)

  #Scans method id's in the latest block and returns a list of transaction hashes
  def scan():
    hashes = []
    pendingBlock = w3.eth.getBlock('pending', full_transactions = True)
    for i in pendingBlock['transactions']:
      if i.input[0:10] in methodIds:
        hashes.append(w3.toHex(i.hash))
      else:
        continue
    return hashes

  def checkTx():
    hashes = scan()
    infoList = []
    for i in hashes:
      tx = w3.eth.get_transaction_receipt(i)
      contract = w3.eth.contract(address = tx.contractAddress, abi = panABI)
      try:
        infoList.extend([bscScanLink+tx.contractAddress, pooCoinLink+tx.contractAddress, contract.functions.name().call(), contract.functions.symbol().call(), tx.contractAddress])
        return infoList
      except Exception as e:
        print(e)
        continue


  while True:
    check = checkTx()
    if check == None:
      time.sleep(3)
      continue
    else:
      token = Tokens(check[0], check[1], check[2], check[3], check[4], 1)
      print(token)
      session = loadSession()
      session.add(token)
      session.commit()
      time.sleep(3)


