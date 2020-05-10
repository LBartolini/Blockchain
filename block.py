from Crypto.Hash import SHA256
import datetime

class Block:

    max_transactions = 10
    min_transactions = 5

    def __init__(self):
        self.nonce = 0
        self.time = datetime.datetime.now()
        self.bnumber = 0

        self.transactions = []
        self.next = None
        self.previous_hash = 0x0

    def hash(self):
        data = str(self.nonce) + str(self.previous_hash) + str(self.time) + str(self.bnumber)

        for trans in self.transactions:
            data += trans.to_string()

        return SHA256.new(data.encode()).hexdigest()

    def add_transaction(self, transaction):
        if len(self.transactions) < self.max_transactions and transaction.signature is not None:
            #TODO: check if sender has enough money
            self.transactions.append(transaction)

    def print_values(self):
        ret = "-------"
        ret += "\nBlock number: " + str(self.bnumber) + "\nTime: " + str(self.time) + "\nNonce: " + str(self.nonce)
        ret += "\nPrevious Hash: " + str(self.previous_hash) + "\nHash: " + str(self.hash())
        ret += "\nTransactions count: " + str(len(self.transactions))
        return ret