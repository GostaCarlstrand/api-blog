import socket
import threading

HOST = '127.0.0.1'
PORT = 9782


def input_handler(client_socket):
    while True:
        try:
            # Get user message - BLOCKING
            message = input()
            # Send the message
            client_socket.send(message.encode('utf-8'))
        except UnicodeDecodeError:
            print("Unicode error")
        break


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    input_thread = threading.Thread(target=input_handler, args=(client_socket,))
    input_thread.start()
    while True:
        # Receive message from server - BLOCKING
        message = client_socket.recv(1024)
        message = message.decode('utf-8')
        print(message)


if __name__ == '__main__':
    main()