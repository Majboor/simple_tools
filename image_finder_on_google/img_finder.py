# Import the libraries.
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time
from selenium.webdriver.chrome.options import Options
chrome_options = Options()

#welcome page
print("""
-------------------------------
welcome to Waleed's project
-------------------------------
\n\n\n""")
def get_image(product, required_img)
 url = ("https://www.google.com/search?q={s}&tbm=isch&source=hp&biw=1366&bih=603&ei=7HtuY_DEJ4eQgQaGiYGAAg&iflsig=AJiK0e8AAAAAY26J_I4ZiDh4liFEWI79Ek_-oQV4j1cm&ved=0ahUKEwjw6r7Tyab7AhUHSMAKHYZEACAQ4dUDCAc&uact=5&oq=t&gs_lcp=CgNpbWcQA1C7RFi7RGDhRWgAcAB4AIABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nsAEA&sclient=img")
 chrome_options.add_argument("--headless")
 PATH = "/usr/bin/chromedriver"
 driver = webdriver.Chrome(PATH, options=chrome_options)
 driver.implicitly_wait(5)
 driver.get(url)
 print(driver.title)

# Create url variable containing the webpage for a Google image search.

# Launch the browser and open the given url in the webdriver.

# product = str(input("what is your product (name)\n:-"))
# required_img = str(input("how many images do you want to load (more images increase accuracy) default[10]\n:-"))



 driver.get(url.format(s=(product)))
# Scroll down the body of the web page and load the images.
 driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
 time.sleep(5)
# Find the images.
 imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'Q4LuWd')]")
# Access and store the scr list of image url's.
 src = []
 for img in imgResults:
     src.append(img.get_attribute('src'))
# Retrieve and download the images.
 for i in range(10):    urllib.request.urlretrieve(str(src[i]),"./images/pets{}.jpg".format(i))
