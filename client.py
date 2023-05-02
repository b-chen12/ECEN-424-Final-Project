import socket

if __name__ == "__main__":
	HOST = input("Server IP: ")
	PORT = int(input("Server Port: "))
	print("Type 'quit' to exit.")


	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))

		while (True):
			query = input("\nWhat are you looking for? ")

			if (query == 'quit'):
				break

			s.sendall(bytes(query, 'utf-8'))

			reply = s.recv(1024)
			print('\n' + reply.decode('utf-8'))

	print("\nGoodbye!")
