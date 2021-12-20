import queue
import socket
import threading

HOST = "127.0.0.1"
PORT = 9782


def client_handler(client_socket, broadcast_queue, client_list):
    while True:
        try:
            # Get data from client, BLOCKING
            message = client_socket.recv(1024)
            message = message.decode('utf-8')
            print("Got message", message)
            message_dict = {
                "sender_socket": client_socket,
                "message": message
            }
            broadcast_queue.put(message_dict)
        except ConnectionRefusedError:
            print("Client left the chat")
            client_list.remove(client_socket)
        break


def broadcast(client_list, broadcast_queue):
    print("Broadcast started")
    while True:
        message_dict = broadcast_queue.get()
        print("Broadcast got a message to send")
        for client in client_list:
            if client != message_dict["sender_socket"]:
                client.send(message_dict["message"])


def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))

    server_socket.listen()
    # Create list of all connected clients
    client_list = []

    broadcast_queue = queue.Queue()

    broadcast_thread = threading.Thread(target=broadcast, args=(client_list, broadcast_queue))
    broadcast_thread.start()

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Client connect from {client_address}')
        client_thread = threading.Thread(target=client_handler, args=(client_socket, broadcast_queue, client_list))
        # Add the new client_socket to the list of clients
        client_list.append(client_socket)
        client_thread.start()

    server_socket.close()

if __name__ == '__main__':
    main()