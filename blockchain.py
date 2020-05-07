from block import *

class Blockchain:

    maxNonce = 2**32

    tail = Block("Genesis") # last block of the chain
    head = tail # first block of the chain

    def __init__(self, diff):
        self.diff = diff
        self.target = 2 ** (256 - self.diff)

    def add(self, block):
        block.previous_hash = self.tail.hash()
        block.bnumber = self.tail.bnumber + 1
        block.valid = True

        self.tail.next = block
        self.tail = self.tail.next

    def mine(self, block, verbose=False):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                if verbose: print(block)
                break
            else:
                block.nonce += 1

    def printAll(self):
        tmp = self.head
        while tmp is not None:
            print(tmp)
            tmp = tmp.next
