from web3 import Web3
import json
import time
from web3.middleware import geth_poa_middleware



w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

with open('./panABI.json') as file:
  panABI = json.load(file)

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

bscScanLink = 'https://www.bscscan.com/address/'
pooCoinLink = 'https://poocoin.app/tokens/'


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
  for i in hashes:
    tx = w3.eth.get_transaction_receipt(i)
    contract = w3.eth.contract(address = tx.contractAddress, abi = panABI)
    try:
      print(contract.functions.name().call())
      print(contract.functions.symbol().call())
      print(tx.contractAddress)
      print(bscScanLink+tx.contractAddress)
      print(pooCoinLink+tx.contractAddress)
    except Exception as e:
      print(e)
      print(tx.contractAddress)


while True:
  checkTx()
  time.sleep(3)



