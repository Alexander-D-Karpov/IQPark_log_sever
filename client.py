import socket

sock = socket.socket()

sock.connect(('localhost', 4545))
data = sock.recv(1024).decode() # recev key
sock.send(str(1).encode())
sock.close()