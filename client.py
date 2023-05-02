import socket

if __name__ == "__main__":
    print("Client Setup:")
    print("-------------")
    HOST = input("Server IP: ")
    PORT = int(input("Server Port: "))
    
    print("\nType 'quit' to exit.")
    print("---------------------")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            query = input("\nWhat are you looking for? ")

            if query == 'quit':
                break

            s.sendall(bytes(query, 'utf-8'))

            reply = s.recv(1024)
            print(f"\nReceived: {reply.decode('utf-8')}")

    print("\nGoodbye!")
