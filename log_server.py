from socket import *

sock = socket.socket(AF_INET,SOCK_STREAM)

def send_to_log(us_id, adr):
    sock.connect(('localhost', 4040))
    data = sock.recv(1024).decode() # recev key
    sock.send(us_id)
    sock.send(adr)
    sock.close()
    return 0


while True:
    sock.bind(('', 4545))
    sock.listen(1)
    conn, addr = sock.accept()
    print('connected:', addr)
    conn.send('Ok'.encode()) #sends key
    us_id = int(conn.recv(1024).decode()) #gets encoded id
    sock.close()
    send_to_log(us_id, addr)

