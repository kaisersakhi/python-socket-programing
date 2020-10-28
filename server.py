import socket
import sys
from threading import Thread

HOST = '127.0.0.1'
PORT = 5050
ENCODING_METHOD = "UTF-8"
HEADER_SIZE = 10
BUFFER_SIZE = 20  # BYTES


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
                # conn.send(bytes("hello world", encoding=ENCODING_METHOD))
                # Thread(target=comncat, args=[conn]).start()
                comncat(conn)
                conn.close()


def comncat(conn):
    print("Type 'exit' for exit\n")

    while True:
        # get the message from the console
        msg = input("Type messages : ")
        # attach the header with the message
        msg1 = f"{len(msg) : < {HEADER_SIZE}}" + msg
        # if user has entered exit , then close the socket
        if str.lower(msg) == "exit":
            print("--> Chat Ended!\n")
            return
        # else if there is something in the msg then send it over the client
        elif len(msg) > 0:
            conn.send(bytes(msg1, encoding=ENCODING_METHOD))
            recived_msg = recive_msg(conn)
            if recived_msg == "d":
                conn.close()
                return
            else:
                print("Client :-> "+recived_msg[HEADER_SIZE:])
            continue


def recive_msg(sock):
    full_message = ""
    new_msg = True
    msg_size = 0
    while True:
        # get the data from the server, of buffer size
        data = sock.recv(BUFFER_SIZE)
        # data = data.decode(encoding=ENCODING_METHOD)
        # if server has send and empty string , then server has probally closed the connection
        if data.decode(ENCODING_METHOD) == "":
            return "d" # d means client is dead

        # just a flag , run this 'if' for the first time to recive on full message
        if new_msg:
            # get the size of the message
            msg_size = int(((data.decode(encoding=ENCODING_METHOD))[:HEADER_SIZE]).strip())
            # set this bool to false , as i've recived the header
            new_msg = False
        # print(f"the header size is {data[:HEADER_SIZE].strip()}")

        # concatinate everytime , while the loop is running
        full_message += data.decode(encoding=ENCODING_METHOD)

        # check if the size of the full message is wqual the the msg_size that i've recived with the header
        # if so , that means i've recived the full message
        if len(full_message) - HEADER_SIZE == msg_size:
            # print(full_message[HEADER_SIZE:])
            # set this bool to false , to let the 'if' run above so that it can get the header of the new
            # message
            # print the full message
            # set this to emptyString as i dont want it to concatinate with the new message
            return full_message


if __name__ == "__main__":
    createSock()
