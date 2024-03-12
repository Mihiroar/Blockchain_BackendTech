# import hashlib

# def hashGenerator(data):
#     result=hashlib.sha256(data.encode())
#     return result.hexdigest()

# class Block:
#     def __init__(self,data,hash,prev_hash):
#         self.data=data
#         self.hash=hash
#         self.prev_hash=prev_hash

# class Blockchain:
#     def __init__(self):
#       hashLast=hashGenerator('gen_last')
#       hashStart=hashGenerator('gen_hash')

#       genesis=Block('gen-data',hashStart,hashLast)
#       self.chain=[genesis]

#     def add_block(self,data):
#         prev_hash=self.chain[-1].hash
#         hash=hashGenerator(data+prev_hash)
#         block=Block(data,hash,prev_hash)
#         self.chain.append(block)

# bc=Blockchain()
# bc.add_block('1')
# bc.add_block('2')
# bc.add_block('3')

# for block in bc.chain:
#     print(block.__dict__)

# import hashlib
# import time

# def hashGenerator(data):
#     result = hashlib.sha256(data.encode())
#     return result.hexdigest()

# class Block:
#     def __init__(self, index, data, prev_hash, timestamp, nonce):
#         self.index = index
#         self.data = data
#         self.timestamp = timestamp
#         self.prev_hash = prev_hash
#         self.nonce = nonce
#         self.hash = self.calculate_hash()

#     def calculate_hash(self):
#         data = str(self.index) + self.data + str(self.timestamp) + self.prev_hash + str(self.nonce)
#         return hashGenerator(data)

# class Blockchain:
#     def __init__(self):
#         self.chain = [self.create_genesis_block()]
#         self.difficulty = 4  # Adjust the difficulty level for mining

#     def create_genesis_block(self):
#         return Block(0, "Genesis Block", "0", int(time.time()), 0)

#     def get_latest_block(self):
#         return self.chain[-1]

#     def mine_block(self, data):
#         prev_block = self.get_latest_block()
#         index = prev_block.index + 1
#         timestamp = int(time.time())
#         nonce = 0
#         new_block = Block(index, data, prev_block.hash, timestamp, nonce)

#         while not new_block.hash.startswith('0' * self.difficulty):
#             nonce += 1
#             new_block.timestamp = int(time.time())
#             new_block.nonce = nonce
#             new_block.hash = new_block.calculate_hash()

#         self.chain.append(new_block)

# bc = Blockchain()
# bc.mine_block('1')
# bc.mine_block('2')
# bc.mine_block('3')

# for block in bc.chain:
    # print(f"Block #{block.index}")
    # print("Data:", block.data)
    # print("Timestamp:", block.timestamp)
    # print("Previous Hash:", block.prev_hash)
    # print("Nonce:", block.nonce)
    # print("Hash:", block.hash)
    # print()
    
    
import hashlib
import time
from prettytable import PrettyTable

def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:
    def __init__(self, index, data, prev_hash, timestamp, nonce):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + self.data + str(self.timestamp) + self.prev_hash + str(self.nonce)
        return hashGenerator(data)

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0", int(time.time()), 0)

    def get_latest_block(self):
        return self.chain[-1]

    def mine_block(self, data):
        prev_block = self.get_latest_block()
        index = prev_block.index + 1
        timestamp = int(time.time())
        nonce = 0
        new_block = Block(index, data, prev_block.hash, timestamp, nonce)

        while not new_block.hash.startswith('0' * self.difficulty):
            nonce += 1
            new_block.timestamp = int(time.time())
            new_block.nonce = nonce
            new_block.hash = new_block.calculate_hash()

        self.chain.append(new_block)

    def display_chain(self):
        table = PrettyTable()
        table.field_names = ["Index", "Data", "Timestamp", "Previous Hash", "Nonce", "Hash"]
        
        for block in self.chain:
            table.add_row([block.index, block.data, block.timestamp, block.prev_hash, block.nonce, block.hash])
        
        print(table)

bc = Blockchain()
bc.mine_block('1')
bc.mine_block('2')
bc.mine_block('3')

bc.display_chain()
  

