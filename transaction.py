from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import binascii

class Transaction:
    def __init__(self, source, destination, amount):
        self.source_pvt = source.private_key
        self.source_pbl = source.public_key
        self.destination = destination
        self.amount = amount
        self.signature = None

    def sign(self):
        signer = PKCS1_v1_5.new(self.source_pvt)
        hash = SHA256.new(self.to_string().encode())
        self.signature = binascii.hexlify(signer.sign(hash)).decode('ascii')

    def to_string(self):
        return str(self.source_pbl) + str(self.destination) + str(self.amount)

