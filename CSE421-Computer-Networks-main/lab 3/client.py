

import socket

SERVER = socket.gethostbyname(socket.gethostname())
HEADER=64
PORT = 5050
ADDR = (SERVER,PORT)
FORMAT="utf=8"
DISCONNECT_MSG="End"
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(msg)
    send_length=str(msg_length).encode(FORMAT)
    send_length+=b" "*(HEADER-len(send_length))
    
    client.send(send_length)
    client.send(message)
    
    print(client.recv(2048).decode(FORMAT))
    
msg=f"The hostname of client is {socket.gethostname()} and the IP is {SERVER}"

send(msg)
send(DISCONNECT_MSG)

