import socket
from Seq_new import Seq
import termcolor


# Configure the Server's IP and PORT
PORT = 8084
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5

def validSequence(s):
    bases_valid = 'ACTG'
    for letter in s:
        if letter not in bases_valid:
            return False
    return True

def calculator(s1, comando):
    print("Doing command", comando)
    if (comando=="len"):
        return s1.length()
    elif (comando=="complment"):
        sequence = s1.complement().getBase()
        print(sequence)
        return sequence
    elif (comando=="reverse"):
        return s1.reverse().getBase()
    elif (comando=="count_A"):
        return s1.count('A')
    elif (comando=="count_T"):
        return s1.count('T')
    elif (comando == "count_G"):
        return s1.count('G')
    elif (comando == "count_C"):
        return s1.count('C')
    elif (comando=="perc_A"):
        return s1.perc("A")
    elif (comando=="perc_T"):
        return s1.perc("T")
    elif (comando=="perc_G"):
        return s1.perc("G")
    elif (comando=="perc_C"):
        return s1.perc("C")
    else:
        return "Error"
def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")
    #For printing the words in colors.
    termcolor.cprint(msg, 'red')

    response = ""
    if msg=='\n':
        response = "ALIVE"
    else:
        separate = msg.split('\n')
        print("Attending", separate[0])
        if (validSequence(separate[0])):
            response = 'OK\n'

            s1 = Seq(separate[0])

            for i in range(1,len(separate)-1):
                print("Tratando el comando", i, separate[0])
                r = calculator(s1, separate[i])
                response = response + str(r)+'\n'
        else:
            response = 'ERROR'


    # Send the msg back to the client
    cs.send(str.encode(response))


    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)