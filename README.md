# Books to Scrape Web Scraper

This project uses Selenium and BeautifulSoup to scrape book titles and prices from the "Books to Scrape" website. The project retrieves book titles and prices from a specified category and obtains detailed information for a specific book.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup4
- requests
- Chrome WebDriver

## Installation

To install the required libraries, run the following command:
bash
pip install selenium beautifulsoup4 requests

##Usage

The project has two main functions:

get_category_detail_urls(category): Retrieves book titles and prices for a specified category.
get_product_detail(book_name): Retrieves detailed information for a specified book (price, stock status, star rating, description, etc.).
Example Usage
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException

ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument("--start-maximized")
driver_path = "C:/Users/USER/Desktop/Other Works/Web_Scraping/chromedriver-win64/chromedriver-win64/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path, options=ChromeOptions)
driver.get("https://books.toscrape.com/")

category = "Travel"
book_title, book_price = get_category_detail_urls(category)

get_product_detail("Soul Reader")


## License
This project is licensed under the MIT License.

csharp
Kodu kopyala

This README file provides an overview of the project, its requirements, installation steps, and usage i