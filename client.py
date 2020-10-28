import socket
import sys

HOST = '127.0.0.1'
PORT = 5050
BUFFER_SIZE = 10  # BYTES
ENCODING_METHOD = "UTF-8"
HEADER_SIZE = 10


def conct():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        conn = sock.connect((HOST, PORT))
        full_message = ""
        msg_size = 0
        new_msg = True
        while True:
            # get the data from the server, of buffer size
            data = sock.recv(BUFFER_SIZE)
            # data = data.decode(encoding=ENCODING_METHOD)
            # if server has send and empty string , then server has probally closed the connection
            if data.decode(ENCODING_METHOD) == "":
                break

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
                new_msg = True
                print(full_message[HEADER_SIZE:])
                full_message = ""

                reply = input("Do you want to reply : Type n or type your message : \n")
                if reply != "n":
                    send_msg(sock, reply)
                else:
                    send_msg(sock, 'c') # c means continue


def send_msg(connection, msg):

    msg = f"{len(msg)  : < {HEADER_SIZE}}" + msg
    connection.send(bytes(msg, encoding=ENCODING_METHOD))
    return


if __name__ == '__main__':
    conct()
