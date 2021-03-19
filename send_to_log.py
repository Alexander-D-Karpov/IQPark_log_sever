def send_to_log(us_id, adr):
    import socket
    sock = socket.socket()
    sock.connect(('localhost', 5555))
    data = sock.recv(1024).decode() # recev key
    sock.send(str(us_id).encode())
    sock.send(str(adr).encode())
    sock.close()
    return 0
