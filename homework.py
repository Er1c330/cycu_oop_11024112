import requests
from bs4 import BeautifulSoup

def fetch_tvbs_news():
    url = 'https://news.tvbs.com.tw/'
    response = requests.get(url)
    response.raise_for_status()  # 確保請求成功

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h2', class_='news_title')

    for index, headline in enumerate(headlines, start=1):
        print(f"{index}. {headline.get_text(strip=True)}")

if __name__ == "__main__":
    fetch_tvbs_news()
    