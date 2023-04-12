import requests
from bs4 import BeautifulSoup

def get_amazon_link(search_term):
    base_url = "https://www.amazon.com"
    search_url = f"{base_url}/s?field-keywords={search_term}"

    # Replace the YOUR_USER_AGENT_HERE with a valid user agent string for your browser
    headers = {
        "User-Agent": "YOUR_USER_AGENT_HERE",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "TE": "Trailers",
    }


    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    # Find the first search result
    search_result = soup.find("div", {"data-index": "5"})
    if search_result:
        link = search_result.find("a", class_="a-link-normal")
        if link:
            return base_url + link["href"]
    return None

if __name__ == "__main__":
    search_term = "apple pen"
    link = get_amazon_link(search_term)
    if link:
        print(f"Amazon link: {link}")
    else:
        print("No link found.")
