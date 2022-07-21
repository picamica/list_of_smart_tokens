from web3 import Web3
import json
from web3.middleware import geth_poa_middleware


w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

with open('./panABI.json') as file:
  panABI = json.load(file)
panrouter = w3.toChecksumAddress('0x10ED43C718714eb63d5aA57B78B54704E256024E')
factoryAddress = w3.toChecksumAddress('0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73')
contract = w3.eth.contract(address=factoryAddress, abi=panABI)

methodIds = ['0x60806040',
'0x60a06040',
'0x69d3c21b',
'0x6818ce40',
'0x60e06040',
'0x60c06040',
'0x61010060',
'0x61016060',
'0x210f5dda']


pendingBlock = w3.eth.getBlock('pending', full_transactions = True)
for i in pendingBlock['transactions']:
  if i['input'][0:10] in methodIds:
    print(i)


# tx = w3.eth.getTransaction('0x1a9a79cfb4dfe5a7419fec6d52bba7c1802e06a218686cd8249d331cdc9585fd').input

# print(tx[0:10])
# print(methodIds)

# if tx[0:10] in methodIds:
#   print('as axuenas')
# else:
#   print('huh?')
