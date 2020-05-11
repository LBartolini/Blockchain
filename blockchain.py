from block import *

class Blockchain:

    maxNonce = 2**32

    def __init__(self, diff, admin):
        self.tail = Block(self)  # last block of the chain GENESIS
        self.head = self.tail  # first block of the chain
        self.diff = diff
        self.target = 2 ** (256 - self.diff)
        self.admin = admin # admin public key

    def add(self, block):
        block.prev = self.tail
        block.bnumber = self.tail.bnumber + 1
        block.valid = True

        self.tail.next = block
        self.tail = self.tail.next

    def getBalance(self, public_key):
        tmp = self.tail
        while tmp is not None:
            for trans in tmp.transactions:
                if public_key in trans.balances:
                    return trans.balances[public_key]
            tmp = tmp.prev

        return 0

    def mine(self, block, verbose=False):
        if len(block.transactions) >= Block.min_transactions:
            for n in range(self.maxNonce):
                if int(block.hash(), 16) <= self.target:
                    self.add(block)
                    if verbose: print(block)
                    break
                else:
                    block.nonce += 1

    def printTail(self, number=50):
        tmp = self.tail
        i = number
        while tmp is not None and i > 0:
            print(tmp.print_values())
            tmp = tmp.prev
            i -= 1
