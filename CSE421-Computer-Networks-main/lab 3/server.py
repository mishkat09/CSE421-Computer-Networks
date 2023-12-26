

import socket

SERVER = socket.gethostbyname(socket.gethostname())
HEADER = 64
FORMAT="utf=8"
PORT = 5050
DISCONNECT_MSG="End"
ADDR = (SERVER,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
print("Server is starting")

server.listen()
print("SERVER is listening on",SERVER)

while True:
    conn,addr=server.accept()
    print("Connected to",addr)
    connected=True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg==DISCONNECT_MSG:
                connected = False
                conn.send(f"Terminating the connection with {addr}".encode(FORMAT))
            else:
                print(msg)
                conn.send("Message Recieved".encode(FORMAT))
    conn.close()          
                