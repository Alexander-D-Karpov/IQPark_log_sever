import socket
import random

sock = socket.socket()

sock.connect(('localhost', 4545))
data = sock.recv(1024).decode() # recev key
sock.send(str(random.randint(1, 13)).encode())
sock.close()