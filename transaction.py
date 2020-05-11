from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import binascii

class Transaction:
    def __init__(self, source, destinations):
        self.source_pbl = source.public_key
        self.source_pbl_str = source.getPBL()
        self.destinations = destinations # key = public_addres, value = amount of btc
        self.signature = None

    def sign(self, sourcePVT):
        signer = PKCS1_v1_5.new(sourcePVT)
        hash_code = SHA256.new(self.to_string().encode())
        self.signature = signer.sign(hash_code)

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
        return  ret

