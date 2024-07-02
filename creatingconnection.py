from web3 import Web3
import json
infura_url = "https://mainnet.infura.io/v3/3ba213d92fba47c9ad19e8c997499ce2"
web3 = Web3(Web3.HTTPProvider(infura_url))
latest_block_number = web3.eth.block_number
latest_block = web3.eth.get_block(latest_block_number)
block_details = dict(latest_block)
with open('latest_block.json', 'w') as json_file:
    json.dump(block_details, json_file, default=str, indent=4)