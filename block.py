import hashlib
import datetime

class Block:

    nonce = 0
    time = datetime.datetime.now()
    bnumber = 0
    data = None
    next = None
    hash = None
    previous_hash = 0x0

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
                str(self.nonce).encode() +
                str(self.data).encode() +
                str(self.previous_hash).encode() +
                str(self.time).encode() +
                str(self.bnumber).encode()
                )

        return h.hexdigest()

    def __str__(self):
        return "Previous Hash: " + str(self.previous_hash) + "\nBlock Hash: " + str(
                self.hash()) + "\nBlock Number: " + str(self.bnumber) + "\nNonce: " + str(
                self.nonce) + "\nData: " + str(self.data) + "\n-----------"