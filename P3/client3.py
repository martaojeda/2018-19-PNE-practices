import socket

# SERVER IP, PORT
IP = "127.0.0.1"
PORT = 8084

while True:
    send = ""
    msg = str(input('>'))
    while len(msg)>0:
        send = send + msg + '\n'
        msg = str(input(''))
    if (len(send)==0):
        send = '\n'


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))



# Send the request message to the server
    s.send(str.encode(send))

# Receive the servers respoinse
    response = s.recv(2048).decode()

# Print the server's response
    print("Response: {}".format(response))

s.close()