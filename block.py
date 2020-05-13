from Crypto.Hash import SHA256
import datetime

class Block:

    max_transactions = 10
    min_transactions = 1

    def __init__(self, blockchain):
        self.blockchain = blockchain

        self.nonce = 0
        self.time = datetime.datetime.now()
        self.bnumber = 0

        self.transactions = []
        self.next = None
        self.prev = None
        self.previous_hash = 0x0

    def create_data(self):
        data = str(self.nonce) + str(self.time) + str(self.bnumber)
        if self.bnumber > 0: data += str(self.prev.hash())

        for trans in self.transactions:
            data += trans.to_string()

        return data

    def check_hash(self):
        # TODO: check if hash is correct
        pass

    def hash(self):
        data = self.create_data()

        return SHA256.new(data.encode()).hexdigest()

    def add_transaction(self, transaction):
        if len(self.transactions) < self.max_transactions:
                self.transactions.append(transaction)
                return True
        return False

    def signAll(self):
        for trans in self.transactions:
            if not trans.sign():
                self.transactions.remove(trans)


    def print_values(self):
        ret = "-------"
        ret += "\nBlock number: " + str(self.bnumber) + "\nTime: " + str(self.time) + "\nNonce: " + str(self.nonce)
        ret += "\nHash: " + str(self.hash())
        if self.bnumber > 0: ret += "\nPrevious Hash: " + str(self.prev.hash())
        ret += "\nTransactions count: " + str(len(self.transactions))
        return ret