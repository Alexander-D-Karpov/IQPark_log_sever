import socket

sock = socket.socket()

while True:
    sock.bind(('', 7777))
    sock.listen(1)
    conn, addr = sock.accept()
    print('connected:', addr)
    conn.send('Ok'.encode()) #sends key
    id = conn.recv(1024).decode() #gets encoded id
    send_to_log(id, addr)
    conn.close()

def send_to_log(id, adr):
    sock.connect(('localhost', 4040))
    data = sock.recv(1024).decode() # recev key
    string = 'Error with ' + str(id) + ' in ' + str(adr) 
    if adr == 'park ip':
        string = 'Entered: ' + str(id) + ' from park'
    elif adr == 'enter ip':
        string = 'Entered: ' + str(id) + ' from enter'
    sock.send(string.encode())
    sock.close()
    return 0