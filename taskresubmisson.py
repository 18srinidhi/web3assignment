from eth_account import Account
import json
acct = Account.create('sri nidhi')
private_key = acct._private_key.hex()
address = acct.address
wallet_data = {
    "address": address,
    "private_key": private_key
}
file_path = 'wallet.json'
with open(file_path, 'w') as json_file:
    json.dump(wallet_data, json_file, indent=4)



with open('wallet.json', 'r') as json_file:
    wallet_data = json.load(json_file)
address = wallet_data.get("address")
private_key = wallet_data.get("private_key")
print(address)
print(private_key)
