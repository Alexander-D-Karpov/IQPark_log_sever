import socket
from python_graphql_client import GraphqlClient
import logging
import datetime
from tkinter import *
import time

sock = socket.socket()
sock.bind(('', 3333))
sock.listen(1)

file = open('users.log', 'r')
lines = file.read().splitlines()
file.close()


logging.basicConfig(filename='users.log', level=logging.DEBUG)
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
    root = Tk()
    for x in lines:
        t.insert(END, x + '\n')
    t = Text(root)
    conn, addr = sock.accept()
    conn.send('Ok'.encode()) #sends key
    inf = conn.recv(1024).decode() #gets encoded id
    lst = inf.split('(')
    id = lst[0]
    adr = lst[1].split(', ')
    adr = adr[0]
    if str(adr) == '127.0.0.1':
        adr = 'enterance'
    else:
        adr = 'park'
    data = users[id]
    name = data[0]
    age = data[1]
    role = data[2]
    string = '{} - {} entered {}. He is {}'.format(datetime.datetime.now(), name, str(adr), role)
    t.insert(END, string + '\n')
    logging.debug(string)
    conn.close()
    root.mainloop()
