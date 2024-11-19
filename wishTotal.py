import requests
from bs4 import BeautifulSoup

# Function to calculate the total price of an Amazon wishlist (might not work for non-UK amazon)
def priceChecker():
    # Get the Amazon wishlist URL from the user
    url = input('Please provide the link to your Amazon wishlist: ')

    # Set headers to mimic a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Fetch the wishlist page
    response = requests.get(url, headers=headers)

    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all elements containing prices
    prices = soup.find_all('span', class_='a-offscreen')

    # Convert the prices to floats and store them
    cleaned_prices = []
    for price in prices:
        cleaned_prices.append(float(price.string[1:]))  # Remove the currency symbol and convert to float
        
    # Print the total sum of all prices
    print(sum(cleaned_prices))

# Run the priceChecker function
priceChecker()






