import socket
from python_graphql_client import GraphqlClient

sock = socket.socket()
sock.bind(('', 7777))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    conn.send('Ok'.encode()) #sends key
    inf = conn.recv(1024).decode() #gets encoded id
    adr = conn.recv(1024).decode() #gets encoded adress
    graphql_connect(id)
    conn.close()

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
