import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import binascii

class User:
    '''
    User(client) that is able to send money and mine blocks
    '''

    def __init__(self):
        self.public_key = None
        self.private_key = None

    def getPBL(self):
        return binascii.hexlify(self.public_key.exportKey(format('DER'))).decode('ascii')

    def getPVT(self):
        return binascii.hexlify(self.private_key.exportKey(format('DER'))).decode('ascii')

    def create_wallet(self):
        rnd = Random.new().read
        self.private_key = RSA.generate(1024, rnd)
        self.public_key = self.private_key.publickey()

    def send(self, destinations): # destinations: dictionary of wallet and amount
        pass