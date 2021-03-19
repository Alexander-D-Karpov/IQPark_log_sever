import socket
from python_graphql_client import GraphqlClient

sock = socket.socket()
sock.bind(('', 3333))
sock.listen(1)

users = {
    '1' : ['Kasha Sarpov', '69', 'admin']
}

while True:
    conn, addr = sock.accept()
    conn.send('Ok'.encode()) #sends key
    inf = conn.recv(1024).decode() #gets encoded id
    adr = conn.recv(1024).decode() #gets encoded adress
    data = users['1']
    name = data[0]
    age = data[1]
    role = data[2]
    print(name, 'entered', adr, 'He is', age, 'and', role)
    conn.close()
