Book Info Scraper

This project is a simple Python script that scrapes book information from the Books to Scrape website. It gathers details such as the title, price, rating, availability, and link for each book and exports the data to an Excel file.
Website

Data is scraped from the following website: Books to Scrape
Features

    Scrapes book details like title, price, rating, availability, and link.
    Collects a minimum of 250 rows of data with 5-7 columns.
    Exports the scraped data into an Excel file for easy access and analysis.

Requirements

To run this script, install the following Python libraries:

pip install requests beautifulsoup4 pandas openpyxl

Usage

    Clone this repository:

git clone https://github.com/your-username/Book-Info-Scraper.git
cd Book-Info-Scraper

Run the script:

    python book_scraper.py

    The scraped data will be saved as books_data.xlsx in the project directory.

Notes

    This script is for educational purposes. Please ensure you follow the website's robots.txt and terms of service.
    For large-scale or frequent scraping, consider adding additional delays to avoid overloading the server.

License

This project is licensed under the MIT License
