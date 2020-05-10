import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

class User:
    '''
    User(client) that is able to send money and mine blocks
    '''

    def __init__(self):
        self.public_key = None
        self.private_key = None

    def create_wallet(self):
        rnd = Random.new().read
        self.private_key = RSA.generate(1024, rnd)
        self.public_key = self.private_key.publickey()

    def send(self, destination, amount):
        #TODO: send a transaction to a specified node in the network
        pass