import requests
from bs4 import BeautifulSoup

def priceChecker():

    url = input('Please provide the link to your amazon wishlist: ')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    prices = soup.find_all('span', class_='a-offscreen')

    cleaned_prices = []
    for price in prices:
        cleaned_price = price.string
        cleaned_prices.append(float(cleaned_price[1:]))
        
    print(sum(cleaned_prices))

priceChecker()
