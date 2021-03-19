import socket

sock = socket.socket()
sock.bind(('', 7777))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    conn.send('Ok'.encode()) #sends key
    inf = conn.recv(8192).decode() #gets encoded information
    print(inf)
    conn.close()