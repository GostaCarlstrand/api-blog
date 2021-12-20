import socket
import threading
import client_socket



HOST = "127.0.0.1"
PORT = 9870

def server_thread():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    count = 0
    while True:
        print("Waiting for connection...")
        new_client_socket, client_address = server_socket.accept()
        threading.Thread(target=client_socket.init_socket, args=(new_client_socket, count)).start()
        print(f"Client connected from {client_address}")
        count = count + 1





def main():
    server_thread()




    while True:
        # Get data from the client, BLOCKING
        message = client_socket.recv(1024)
        message = message.decode("utf-8")
        print("Server message", message)
        return_message = "We got: " + message
        client_socket.send(return_message.encode("utf-8"))



if __name__ == "__main__":
    main()
