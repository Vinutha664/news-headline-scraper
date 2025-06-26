import requests
from bs4 import BeautifulSoup

url = "https://www.hindustantimes.com/latest-news"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h3')

    with open("top_headlines.txt", "w", encoding='utf-8') as file:
        for index, headline in enumerate(headlines, 1):
            text = headline.get_text(strip=True)
            if text:
                print(f"{index}. {text}")
                file.write(f"{index}. {text}\n")
else:
    print("Failed to fetch the website. Status code:", response.status_code)