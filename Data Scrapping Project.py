import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Define the URL of the website to scrape
url = 'http://books.toscrape.com/catalogue/page-{}.html'

# Initialize empty lists to store data
titles = []
prices = []
ratings = []
availabilities = []
links = []

# Loop through the pages (this site has 50 pages in total)
for page in range(1, 51):
    response = requests.get(url.format(page))
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the data for each book
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        # Title
        title = book.h3.a['title']
        titles.append(title)

        # Price
        price = book.find('p', class_='price_color').text
        prices.append(price)

        # Rating
        rating = book.p['class'][1]
        ratings.append(rating)

        # Availability
        availability = book.find('p', class_='instock availability').text.strip()
        availabilities.append(availability)

        # Book link
        link = book.h3.a['href']
        links.append(f"http://books.toscrape.com/catalogue/{link}")

    # Add a delay to avoid overloading the server
    time.sleep(1)

    # Stop after getting 250 rows
    if len(titles) >= 250:
        break

# Create a DataFrame to store the data
books_df = pd.DataFrame({
    'Title': titles[:250],
    'Price': prices[:250],
    'Rating': ratings[:250],
    'Availability': availabilities[:250],
    'Link': links[:250]
})

# Export the DataFrame to an Excel file
books_df.to_excel('books_data.xlsx', index=False)

print("Data has been successfully scraped and saved to 'books_data.xlsx'")
