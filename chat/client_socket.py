import socket
import threading

HOST = "127.0.0.1"
PORT = 9870


def init_socket(client_socket, name):
    print(name)
    print("connected")
    input("Client input")



def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    message = input("Enter something> ")
    client_socket.send(message.encode("utf-8"))
    message = client_socket.recv(1024)
    message = message.decode("utf-8")
    print(message)




if __name__ == "__main__":
    main()
