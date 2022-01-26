from web3 import Web3

# Taking the infura url
infura_url="https://mainnet.infura.io/v3/54a1745e87ac4f6d96e389df32b5ddc3"

# Creating a web3 connection
web3=Web3(Web3.HTTPProvider(infura_url))

# Check if it's connected
print(web3.isConnected())

# Current block number
block_num=web3.eth.blockNumber
print(block_num)

# Get balance
brave_walltet_id="0xc4582d1D4fD36f2BC6B1F5C820a321a100AeDeD9"
current_balance=web3.eth.get_balance(brave_walltet_id)
print(current_balance)

# in-case the balance shows sth creepy(huge)
balance_correct_form=web3.fromWei(current_balance,"ether")
print(balance_correct_form)

