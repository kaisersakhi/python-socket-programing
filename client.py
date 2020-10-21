import socket
import sys

HOST = '127.0.0.1'
PORT = 5050
BUFFER_SIZE = 1024  #BYTES
ENCODEING_METHOD = "UTF-8"


def conct():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        conn = sock.connect((HOST, PORT))
        while True:
            data = sock.recv(BUFFER_SIZE)
            if len(data) < 1:
                break
            print(data)


if __name__ == '__main__':
    conct()
