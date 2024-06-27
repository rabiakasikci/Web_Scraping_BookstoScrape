# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 15:10:45 2024

@author: Rabia KAŞIKCI
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




def get_category_detail_urls(category):
    travel_element = driver.find_element(By.XPATH, f"//a[contains(text(),'{category}')]")
    travel_element_href = travel_element.get_attribute("href")
    print(travel_element_href)
    driver.get(travel_element_href)
    
    book_title = []
    book_price = []
    try:
        next_page = driver.find_element(By.XPATH, "//li[@class = 'next']")
        print("Element exists.")
        # Locate the <a> element with the text "next"
        next_page_element = driver.find_element(By.XPATH, "//a[text()='next']")
        href_value = next_page_element.get_attribute("href")[:-6]
        print(href_value)
        for i in range(1,999):
            print(i)
            driver.get(href_value+str(i)+".html")
            time.sleep(5)
            list_of_books=  driver.find_elements(By.XPATH, "//h3/a[@title]")
            if len(list_of_books) <= 0 :
                driver.get(href_value+str(i-1)+".html")
                break
            for book in list_of_books:
                    print("Title:", book.get_attribute("title"))
                    book_title.append(str(book.get_attribute("title")))
                    

            list_of_books_price = driver.find_elements(By.XPATH, "//div[@class='product_price']/p[@class='price_color']")
            for price in list_of_books_price:
                    print("Price:", price.text)
                    book_price.append(str(price.text))
        
    except NoSuchElementException:
        print("Element does not exist.")
        list_of_books =  driver.find_elements(By.XPATH, "//h3/a[@title]")
        for book in list_of_books:
                print("Title:", book.get_attribute("title"))
                book_title.append(book.get_attribute("title"))

        list_of_books_price = driver.find_elements(By.XPATH, "//div[@class='product_price']/p[@class='price_color']")
        for price in list_of_books_price:
                print("Price:", price.text)
                book_price.append(price.text)
                
    return book_title, book_price
        
        
        

def get_product_detail(book_name):
    for i in range(1, 51):  # Assuming there are 50 pages in total
        url = f"https://books.toscrape.com/catalogue/page-{i}.html"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Failed to retrieve page {i}")
            continue
        
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article', class_='product_pod')
        
        for book in books:
            title = book.h3.a['title']
            
            if title.lower() == book_name.lower():
                print(f"Book found: {title} on page {i}")
                url_book = book.h3.a['href']
                url = f"https://books.toscrape.com/catalogue/{url_book}"
                response = requests.get(url)
                html_content = response.text
                soup = BeautifulSoup(html_content, 'html.parser')
                content_div = soup.find('div', class_='col-sm-6 product_main')
                
                price_element = content_div.find('p', class_='price_color')
                print(price_element.text.strip())
                
                stok_element = content_div.find('p', class_='instock availability')
                print(stok_element.text.strip())
                
                star_rating_tag = soup.find('p', class_='star-rating')
                if star_rating_tag:
                    star_rating = star_rating_tag['class'][-1]  # Son sınıfı yani derecelendirmeyi alır
                    print('Star Rating:', star_rating)
                else:
                    print('Star Rating not found')
                    
                description = soup.find('div', class_='content')
                description_xpath= description.find('p')
                product_description = soup.find('div', id='product_description').find_next_sibling('p').text.strip()
                print(product_description)
                
                table = soup.find('table', class_='table table-striped')


                if table:
                    rows = table.find_all('tr')
                    for row in rows:
                        th = row.find('th').text.strip()
                        td = row.find('td').text.strip()
                        print(f"{th}: {td}")
                else:
                    print("Table not found or structure is not as expected.")
                
                return
    
    print("Book not found")
 




ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument("--start-maximized")
driver_path = "C:/Users/USER\Desktop/Diğer Çalışmalar/Web_Scraping/chromedriver-win64/chromedriver-win64/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path ,options=ChromeOptions)
driver.get("https://books.toscrape.com/")



category = "Travel"
book_title , book_price = get_category_detail_urls(category)




get_product_detail("Soul Reader")
