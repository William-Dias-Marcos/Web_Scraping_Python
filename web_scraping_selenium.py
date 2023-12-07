import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service = service, options = options)

url = 'https://books.toscrape.com/'

try:
 
    driver.get(url)

    titleElements = driver.find_elements(By.TAG_NAME, 'a')[54:94:2]

    titleList = [title.get_attribute('title') for title in titleElements]

    stockList = []
    priceList = []
    for title in titleElements:
    
        title.click()
    
        qtdStock = int(driver.find_element(By.CLASS_NAME, 'instock').text.replace('In stock (', '').replace(' available)', ''))
        stockList.append(qtdStock)

        price = driver.find_element(By.CLASS_NAME, 'price_color').text
        priceList.append(qtdStock)

        driver.back()

    dictDF = {'title': titleList,
              'price': priceList,
              'stock': stockList}

    print(pd.DataFrame(dictDF))

except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()