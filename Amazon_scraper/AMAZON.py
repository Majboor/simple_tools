import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import shutil
from PIL import Image
import requests
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

PATH = "C:\Program Files\drivers\chromedriver_103.exe"
driver = webdriver.Chrome(PATH)

def amazon(product_name):
 driver.get("https://www.amazon.in")
 driver.maximize_window()

 wait = WebDriverWait(driver,10)

 search_box = driver.find_element(By.ID, "twotabsearchtextbox")
 search_box.clear()
#  que = str(input("enter:"))
 search_box.send_keys(product_name)
 driver.find_element(By.ID, "nav-search-submit-button").click()
 driver.find_element(By.XPATH, "//span[text()='Dell']").click()
 laptops = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

 laptop_name = []
 laptop_price = []
 no_reviews = []
 final_list = []

 for laptop in laptops:

     names = laptop.find_elements(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']")
     for name in names:
         laptop_name.append(name.text)

     try:
         if len(laptop.find_elements(By.XPATH, ".//span[@class='a-price-whole']")) > 0:
             prices = laptop.find_elements(By.XPATH, ".//span[@class='a-price-whole']")
             for price in prices:
                # print('the lenght is ===>',len(price.text))
                 laptop_price.append(price.text)
         else:
             laptop_price.append("0")
     except:
         pass
    # reviews = laptop.find_elements(By.XPATH,".//span[@class='a-size-base s-underline-text']")

     try:
         if len(laptop.find_elements(By.XPATH, ".//span[@class='a-size-base s-underline-text']")) > 0:
             reviews = laptop.find_elements(By.XPATH, ".//span[@class='a-size-base s-underline-text']")
             for review in reviews:
                 # print('the length is===>', len(review.text), review.text)
                 no_reviews.append(review.text)
         else:
             no_reviews.append("0")
     except:
         pass

 images_saree = []
 elements = driver.find_elements(By.XPATH, "//img[@class='s-image']")
 for i in elements:
     image = i.get_attribute('src')
     images_saree.append(image)

#creating array of product & saving product
 imag = []
 for img in images_saree:
     file_name = img.split('/')[-1]
     print(f"saving file:{file_name}")
     imag.append(file_name)
     r = requests.get(img, stream=True)
     if r.status_code == 200:
         with open(file_name, 'wb') as f:
             for chunk in r:
                 f.write(chunk)
     else:
         print('')

 print('total products==>', len(laptop_name))
 print('total prices==>', len(laptop_price))
 print('total views reviews==>', len(no_reviews))

 import pandas as pd


#product prompt
 image = mpimg.imread(f"./{imag[0]}")
 plt.imshow(image)
 plt.show()
 for img in images_saree:
     file_name = img.split('/')[-1]
     a = str(input(f"I found this on amazon\n is this your product?:\n{file_name}:"))
     if a == "n".casefold() or a == "no".casefold():
      image = mpimg.imread(f"./{file_name}")
      plt.imshow(image)
      plt.show()
     else:
         break

 print("making excel.......")

 df = pd.DataFrame(zip(laptop_name, laptop_price, no_reviews, imag), columns=['laptop_name', 'laptop_price', 'no_reviews', 'img'])

 df.to_excel(r"./laptops.xlsx", index=False)

 driver.quit()

amazon("laptop")