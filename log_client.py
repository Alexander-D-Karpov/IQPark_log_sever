import socket
#from python_graphql_client import GraphqlClient
import logging
import datetime
from os import listdir
from os.path import isfile, join
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

sock = socket.socket()
sock.bind(('', 3333))
sock.listen(1)
onlyfiles = [f for f in listdir('logs/') if isfile(join('logs/', f))]

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

def graphql_con(id):
    client = GraphqlClient(endpoint)
    query = """
    query countryQuery($user_data: String) {
        user_data(id:$id) {
            id
            name
            role
        }
    }
    """
    variables = {"id": id}

    data = client.execute(query=query, variables=variables)
    return data 

while True:
    if not datetime.datetime.now().date() in onlyfiles:
        logging.basicConfig(filename='logs/{}.log'.format(datetime.datetime.now().date()), level=logging.INFO)
    else:
        logging.config.fileConfig(filename='logs/{}.log'.format(datetime.datetime.now().date()), level=logging.INFO)
    conn, addr = sock.accept()

    keyPair = RSA.generate(1024)
    pubKey = keyPair.publickey()
    exportedPubKey = pubKey.exportKey(format='PEM')
    conn.send(exportedPubKey) #sends key

    encrypted = conn.recv(2048) #gets encoded data
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    inf = decrypted.decode()

    lst = inf.split('; ')
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
    #data = graphql_con(int(id))
    string = '{} - {}({}) entered {}. He is {}'.format(datetime.datetime.now().time(), name, id, str(adr), role)
    logging.info(string)
    conn.close()
