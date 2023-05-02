import socket
print("jsdfjdaj")
host = "127.0.0.1"
port = 50001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

message = input("Enter:")

while message.lower().strip()!="quit":
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print("response from server ", str(data))
    message = input("enter:")

client_socket.close()