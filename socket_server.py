import socket 
def server_send(server_msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.1.10', 1234))
    s.listen(5)
    while True:
        clientsocket,addr = s.accept()
        msg = clientsocket.recv(1024)
        print(msg.decode("utf-8"))
        print(f"Connection from {addr} has been established!")
        clientsocket.send(bytes (server_msg,"utf-8"))

server_send("hi")