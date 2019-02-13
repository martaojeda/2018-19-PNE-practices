import socket

IP = "192.168.56.1"
PORT = 8083

while True:
    sequencia = input("Write a sequence:")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(sequencia))
    msg = s.recv(2048).decode("utf-8")
    print("This is the information from the server: \n {}".format(msg))
    s.close()