from block_module import *

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 4

# Create the blockchain and add the genesis block
# blockchain is an array of Block objects
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print_block(block_to_add);
