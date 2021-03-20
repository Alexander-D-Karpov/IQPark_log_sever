from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import socket

def send_to_log(us_id, adr):
    sock = socket.socket()
    sock.connect(('localhost', 3333))
    exportedPubKey = sock.recv(4096)
    keys = RSA.importKey(exportedPubKey)
    encryptor = PKCS1_OAEP.new(keys)
    encrypted = encryptor.encrypt('{}; {}'.format(us_id, adr).encode())
    sock.send(encrypted)
    sock.close()
    return 0
