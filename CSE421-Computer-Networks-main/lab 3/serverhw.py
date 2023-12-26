import socket

HEADER = 16
PORT = 4040
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "End"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print("[SUCCESS]: Server is listening.....")
while True:
    conn, addr = server.accept()
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                conn.send("Client disconnected!".encode(FORMAT))
            else:
                hour = int(msg)
                if hour <= 40:
                    conn.send("[Received]: 200 TK".encode(FORMAT))
                elif hour > 40:
                    conn.send("[Received]: 8000 TK".encode(FORMAT))

    conn.close()