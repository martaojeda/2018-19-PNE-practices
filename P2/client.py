import socket
from Seq import Seq
IP = "172.17.0.1"
PORT = 8081

while True:
    sequence = input("Introduce a valid sequence:")
    s1 = Seq(sequence)
    s2 = s1.complement()
    s3 = s1.reverse()
    send_1 = "The complement sequence is:" + s2.strbases
    send_2 = "\nThe reverse sequence is:" + s3.strbases
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(send_1))
    s.send(str.encode(send_2))


    msg = s.recv(2048).decode("utf-8")

    print("Message from server:{}".format(msg))

    s.close()