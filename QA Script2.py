from typing import Text
import requests
from selenium import webdriver
import random
import string
import urllib3
from bs4 import BeautifulSoup
import re

Driver_path = 'C:/Users/Khoa Ng/Documents/GitHub/chromedriver'
driver = webdriver.Chrome(executable_path=Driver_path)
#downloads the website html file so that we are able to read the source code per line, this would allow for us to check the payor name to see if the url is valid, then records it
urltester = ("https://www.dentrix.com/products/eservices/eclaims/payor-search?start=0&keyword=")
pull = requests.get(urltester)
print(pull.text)
with open ("C:/Users/Khoa Ng/Documents/GitHub/QATestfile.txt", 'w') as f:
    f.write(pull.text)

payorName = []
with open("C:/Users/Khoa Ng/Documents/GitHub/QATestfile.txt") as f:
    while ( line := f.readline().rstrip()):
        if ('//products//eservices//eclaims//payor-search?start=0&keyword=' in line):
            payor = payorName.append(re.search('*<//td><td>(.*)<//td><td*>', line)) #parses and appends payor name to a list
            
#script enters the payor name through the search bar to see if its valid
for i in payorName:
    urltester = ("https://www.dentrix.com/products/eservices/eclaims/payor-search?start=0&keyword="+payorName[i])
    pull = requests.get(urltester)
    

    driver.get("https://www.dentrix.com/products/eservices/eclaims/payor-search?start=0&keyword=")
    searchbar= driver.find_element_by_css_selector('keyword')
    searchbar.send_keys(payorName[i])
    page = driver.page_source
    if pull.text != page :
        print("Issue found with Payor Name: " + payorName[i])
        break
    #tests the page with the auto entered one to see if it works and is reliable



















