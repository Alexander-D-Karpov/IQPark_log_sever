import socket
from send_to_log import send_to_log as messeger 

sock = socket.socket()
sock.bind(('', 7777))

while True:
    sock.listen(1)
    conn, addr = sock.accept()
    print('connected:', addr)
    conn.send('Ok'.encode()) #sends key
    us_id = int(conn.recv(1024).decode()) #gets encoded id
    messeger(us_id, addr)
    conn.close()

