import socket
import sys
from threading import Thread

HOST = '127.0.0.1'
PORT = 5050
ENCODING_METHOD = "UTF-8"


def createSock():
    """
        The arguments passed to socket() specify the address family and
        socket type. AF_INET is the Internet address family for IPv4.
        SOCK_STREAM is the socket type for TCP,
        the protocol that will be used to transport our messages in the network.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # bind() is used to associate the socket with a specific network interface and port number
        sock.bind((HOST, PORT))
        sock.listen(5)
        print("Listening! \n")
        while True:
            conn, addrss = sock.accept()
            # print("Hello")
            if conn is not None:
                print(conn)
                # conn.accept()

                print("Connection Accepted!")
                conn.send(bytes("hello world", encoding=ENCODING_METHOD))
                # Thread(target=comncat, args=[conn]).start()
                comncat(conn)
                conn.close()


def comncat(conn):
    print("Type 'exit' for exit\n")
    while True:
        cmnd = input("Type messages : ")
        if str.lower(cmnd) == "exit":
            print("--> Chat Ended!\n")
            return
        elif len(cmnd) > 0:
            conn.send(bytes(cmnd, encoding=ENCODING_METHOD))
            continue


if __name__ == "__main__":
    createSock()
