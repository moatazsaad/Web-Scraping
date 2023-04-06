# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 22:09:43 2023

@author: ahmed
"""

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


curr_page = 1
data = []

while True:
    
    print(curr_page)
    
    url = f'https://diwanegypt.com/product-category/books/arabic-books/page/{curr_page}/'
    
    driver.get(url)
    
    books_links = driver.find_elements(By.XPATH, '//a[contains(@class, "woocommerce-LoopProduct-link woocommerce-loop-product__link")]')
    
    
    
    books_titles = driver.find_elements(By.XPATH, '//h2[contains(@class, "woocommerce-loop-product__title")]')
    
    
    
    
    
    books_authors = driver.find_elements(By.XPATH, '//span[contains(@class, "author")] ')

    
    
    
    
    
    
    books_prices = driver.find_elements(By.XPATH, '//span[contains(@class, "woocommerce-Price-amount amount")]')

    
    
    
    books_imgs_urls = driver.find_elements(By.XPATH, '//img[contains(@class, "attachment-woocommerce_thumbnail")]')
    
    for i in range(len(books_links)):
        try:
            book_link = books_links[i].get_attribute('href')
            book_title = books_titles[i].text
            book_author = books_authors[i].text    
            book_price = books_prices[i].text    
            book_img_url = books_imgs_urls[i].get_attribute('src')
            data.append([book_link, book_title, book_author, book_price, book_img_url])    
        except:
            pass
            
        
    
    last_page = driver.find_elements(By.XPATH, '//a[contains(@class, "page-numbers")] ')[-2].text
    
    last_page = int(last_page)
    
    if last_page == curr_page:
        break
    
    
    curr_page += 1
    
    
with open('data.csv', 'w') as fid:
    writer = csv.writer(fid)
    writer.writerow(['book_link', 'book_title', 'book_author', 'book_price', 'book_img_url'])
    writer.writerows(data)
    
    
driver.close()    
    
    
    
    
