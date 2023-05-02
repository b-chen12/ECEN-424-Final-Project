import socket
import requests
from bs4 import BeautifulSoup

def get_amazon_link(search_term):
    base_url = "https://www.amazon.com"
    search_url = f"{base_url}/s?field-keywords={search_term}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "TE": "Trailers",
    }

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    search_result = soup.find("div", {"data-index": "5"})
    if search_result:
        link = search_result.find("a", class_="a-link-normal")
        if link:
            return base_url + link["href"]
    return None

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    HOST = str(s.getsockname()[0])
    PORT = int(input("What port should the server use? "))
    print("\nServer Details:")
    print("---------------")
    print(f"Server IP: {HOST}")
    print(f"Port: {PORT}\n")
    s.close()

    print("Waiting for connections...")
    print("---------------------------")

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()

            conn, addr = s.accept()
            with conn:
                print(f"\nConnected with {addr}")

                while True:
                    data = conn.recv(1024)

                    if not data:
                        break

                    search_term = data.decode('utf-8')
                    link = get_amazon_link(search_term)
                    if link:
                        response_msg = f"Amazon link for {search_term}: {link}"
                    else:
                        response_msg = f"No link found for query: {search_term}"

                    print(f"Received query: {search_term}")
                    print(f"Sending response: {response_msg}")

                    conn.sendall(bytes(response_msg, 'utf-8'))
