# Programming our first client.
import socket
#Create a socket for communicating with the server.


print("Socket created.")
PORT = 8082
IP = "212.128.253.101"

#Connect to the server
while True:
    message= input("Introduce:")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(message))
    msg = s.recv(2048).decode("utf-8")
    print("Message from the server")
    print(msg)
    s.close()


print("The end")