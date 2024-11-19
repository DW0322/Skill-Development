import requests
from bs4 import BeautifulSoup
import time

def priceChecker():
    url = input('Please provide the link to your amazon wishlist: ')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    base_url = "https://www.amazon.co.uk" #change this to your countries corresponding url

    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if 'dp_it_im' in href:
            links.append(base_url + href)

    total = 0
    for link in links:
        time.sleep(2)  # Rate-limiting to avoid scraper limiting
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        price_text = soup.find('span', class_='a-offscreen')
        if price_text:
            try:
                price_float = float(price_text.text.replace('£', '').replace(',', '')) #change £ sign to your countries corresponding url
                total += price_float
            except ValueError:
                print(f"Error parsing price for {link}")
    print(f"Total: {total}")

priceChecker()
