import socket
from Seq import Seq
IP = "172.17.0.1"
PORT = 8081

while True:
    sequence = input("Introduce a valid sequence:")
    s1 = Seq(sequence)
    s2 = s1.complement()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(s2.strbases))
    msg = s.recv(2048).decode("utf-8")
    print(msg)
    s.close()