import hashlib as hasher
import datetime as date

# Define what a block is
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        # Some ways to iterate through an objects properties
        # 1) for att in dir(self):
            # print(att, getattr(self, att))
        # 2) print(self.__dict__)

        props = self.__dict__;
        sha = hasher.sha256()

        # sha.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.data).encode(
        #     'utf-8') + str(self.previous_hash).encode('utf-8'))
        sha.update(str(props).encode('utf-8'))
        return sha.hexdigest()


# -------------------------------------functions
# Generate genesis block
def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0")


# Generate all later blocks in the blockchain
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index) + ". Generated at " + str(this_timestamp)
    this_previous_hash = last_block.hash
    # the hash of the current block is calculated inside the constructor
    return Block(this_index, this_timestamp, this_data, this_previous_hash)

# Print out
def print_block(block):
    # Added parenthesis for Python3 compatibility
    print("Previous Hash {}".format(block.previous_hash))
    print("Block #{} has been added to the blockchain!".format(block.index))
    print("Data: {}".format(block.data))
    print("Hash: {}\n".format(block.hash))