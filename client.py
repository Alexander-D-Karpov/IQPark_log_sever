import socket
import random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

sock = socket.socket()
def connect():
    sock.connect(('localhost', 9999))
    exportedPubKey = sock.recv(4096)
    keys = RSA.importKey(exportedPubKey)
    encryptor = PKCS1_OAEP.new(keys)
    encrypted = encryptor.encrypt(str(random.randint(1, 4)).encode())
    sock.send(encrypted)
    sock.close()

connect()