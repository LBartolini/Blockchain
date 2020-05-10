from block import *

class Blockchain:

    maxNonce = 2**32

    def __init__(self, diff):
        self.tail = Block()  # last block of the chain
        self.head = self.tail  # first block of the chain
        self.diff = diff
        self.target = 2 ** (256 - self.diff)

    def add(self, block):
        block.previous_hash = self.tail.hash()
        block.bnumber = self.tail.bnumber + 1
        block.valid = True

        self.tail.next = block
        self.tail = self.tail.next

    def mine(self, block, verbose=False):
        if len(block.transactions) >= Block.min_transactions:
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
            print(tmp.print_values())
            tmp = tmp.next
