import socket

if __name__ == "__main__":
	HOST = input("Server IP: ")
	PORT = int(input("Server Port: "))

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))

		while (True):
			query = input("What are you looking for? ")

			if (query == 'q'):
				break

			s.sendall(bytes(query, 'utf-8'))

			reply = s.recv(1024)
			print(reply.decode('utf-8'))