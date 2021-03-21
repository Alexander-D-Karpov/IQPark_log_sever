import socket
from send_to_log import send_to_log as messeger 
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

sock = socket.socket()
sock.bind(('', 9999))
sock.listen(1)


while True:
    conn, addr = sock.accept()
    keyPair = RSA.generate(1024)
    pubKey = keyPair.publickey()
    exportedPubKey = pubKey.exportKey(format='PEM')

    print('connected:', addr)
    conn.send(exportedPubKey) #sends key

    encrypted = conn.recv(2048)
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    us_id = int(decrypted.decode()) #gets encoded id

    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    messeger(us_id, addr)
    conn.close()

