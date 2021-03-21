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
    '1' : ['Саша Карпов', '69', 'одноразовый'],
    '2' : ['Илья Василенко', '68', 'персонал'],
    '3' : ['Артем Заборщиков', '67', 'персонал'],
    '4' : ['Георгий Аюпов', '66', 'временный'],
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
        adr = 'со входа'
    else:
        adr = 'с парка'
    data = users[id]
    name = data[0]
    age = data[1]
    role = data[2]
    #data = graphql_con(int(id))
    string = '{} - {}({}) зашёл {}. Тип пропуска: {}'.format(datetime.datetime.now().time(), name, id, str(adr), role)
    logging.info(string)
    conn.close()
