import json
with open('latest_block.json', 'r') as json_file:
    block_details = json.load(json_file)
block_number = block_details.get("number")
block_hash = block_details.get("hash")
parent_hash = block_details.get("parentHash")
timestamp = block_details.get("timestamp")

print(block_number)
print(block_hash)
print(parent_hash)
print(timestamp)