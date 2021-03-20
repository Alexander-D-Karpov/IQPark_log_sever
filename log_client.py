import socket
from python_graphql_client import GraphqlClient
import logging
import datetime

sock = socket.socket()
sock.bind(('', 3333))
sock.listen(1)

logging.basicConfig(filename='logs/users.log', level=logging.INFO)
users = {
    '1' : ['Kasha Sarpov', '69', 'admin'],
    '2' : ['Kasha Sarpov', '68', 'user'],
    '3' : ['Kasha Sarpov', '67', 'noname'],
    '4' : ['Kasha Sarpov', '66', 'noname'],
    '5' : ['Kasha Sarpov', '65', 'user'],
    '6' : ['Kasha Sarpov', '64', 'noname'],
    '7' : ['Kasha Sarpov', '63', 'user'],
    '8' : ['Kasha Sarpov', '62', 'user'],
    '9' : ['Kasha Sarpov', '61', 'user'],
    '10' : ['Kasha Sarpov', '60', 'user'],
    '11' : ['Kasha Sarpov', '59', 'noname'],
    '12' : ['Kasha Sarpov', '58', 'noname'],
    '13' : ['Kasha Sarpov', '57', 'user']
}
while True:
    conn, addr = sock.accept()
    conn.send('Ok'.encode()) #sends key
    inf = conn.recv(1024).decode() #gets encoded data
    lst = inf.split('(')
    id = lst[0]
    adr = lst[1]
    if "127.0.0.1" in adr:
        adr = 'enterance'
    else:
        adr = 'park'
    data = users[id]
    name = data[0]
    age = data[1]
    role = data[2]
    string = '{} - {}({}) entered {}. He is {}'.format(datetime.datetime.now(), name, id, str(adr), role)
    logging.info(string)
    conn.close()
