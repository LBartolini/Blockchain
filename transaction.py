from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import binascii

class Transaction:
    def __init__(self, source, destinations, blockchain):
        self.blockchain = blockchain
        self.source_pbl = source.public_key
        self.source_pvt = source.private_key
        self.source_pbl_str = source.getPBL()
        self.destinations = destinations # key = public_address, value = amount of btc
        self.signature = None
        self.balances = {}

    def getWallets(self):
        out = [self.source_pbl_str]
        for dest in self.destinations:
            if dest != self.source_pbl_str:
                out.append(dest)

        return out


    def confirmBalances(self):
        out = sum([self.destinations[i] for i in self.destinations])
        source_balance = self.blockchain.getBalance(self.source_pbl_str)
        if self.source_pbl_str != self.blockchain.admin.getPBL() and out > source_balance:
            return False
        else:
            if self.source_pbl_str == self.blockchain.admin.getPBL():
                self.balances[self.source_pbl_str] = 0
            else:
                self.balances[self.source_pbl_str] = (source_balance - out)

            for dest in self.destinations:
                if dest != self.source_pbl_str:
                    self.balances[dest] = self.blockchain.getBalance(dest) + self.destinations[dest]
            return True

    def sign(self):
        if self.confirmBalances():
            signer = PKCS1_v1_5.new(self.source_pvt)
            hash_code = SHA256.new(self.to_string().encode())
            self.signature = signer.sign(hash_code)
            return True
        return False

    def check(self):
        if self.signature is None:
            return False
        elif PKCS1_v1_5.new(self.source_pbl).verify(SHA256.new(self.to_string().encode()), self.signature):
            return True
        else:
            return False

    def to_string(self):
        ret = self.source_pbl_str
        for dest in self.destinations:
            ret += str(dest) + str(self.destinations[dest])

        for new_balance in self.balances.values():
            ret += str(new_balance)

        return  ret

