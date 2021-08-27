import requests
from selenium import webdriver
import random
import string
import urllib3
from bs4 import BeautifulSoup, element
from urllib.parse import urlparse, urljoin
# makes a random value the payeeID and searches through it to see if it is valid
# script then would use the webdriver to enter the value manually to the same link
# afterwords it would compare the html files if the values are the same. If it isnt then it would spit out a error with the payeeID and would stop the run
Driver_path = 'C:/Users/Khoa Ng/Documents/GitHub/chromedriver'
driver = webdriver.Chrome(executable_path=Driver_path)

for i in range (600):
    randomnumber = str(random.randint(0,99999));
    print(randomnumber)
    urls = 0
    urltester1 = ("https://www.dentrix.com/products/eservices/eclaims/payor-search?start=0&keyword="+randomnumber)
    print(urltester1)
    pull = requests.get(urltester1)
    soup = BeautifulSoup(requests.get(urltester1).content, "html.parser")
    for a in soup.find_all('a'):
        weblink = a.attrs.get("href")
        if weblink is not None:
            urls= urls+1
    print (urls)
   

    driver.get("https://www.dentrix.com/products/eservices/eclaims/payor-search?start=0&keyword="+randomnumber)
    searchbar= driver.find_element_by_xpath('//input')
    searchbar.send_keys(randomnumber)
    page_source = driver.current_url
    print(page_source)
    urls2=0
    
    pull = requests.get(page_source)
    soup = BeautifulSoup(requests.get(page_source).content, "html.parser")
    for a in soup.find_all('a'):
        weblink = a.attrs.get("href")
        if weblink is not None:
            urls2= urls2+1
    print (urls2)
    if urls != urls2 :
       print("Issue found with payeeID: " + randomnumber)
       break
    
    


