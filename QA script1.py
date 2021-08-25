import requests
from selenium import webdriver
import random
import string
import urllib3
from bs4 import BeautifulSoup
# makes a random value the payorID and searches through it to see if it is valid
# script then would use the webdriver to enter the value manually to the same link
# afterwords it would compare the html files if the values are the same. If it isnt then it would spit out a error with the payorID and would stop the run

driver = webdriver.FirefoxProfile()

for i in range (0,600):
    randomnumber = str(random.randint(0,99999));
    i = i+1
    print(randomnumber)
    urltester = ("https://www.dentrix.com/products/eservices/eclaims/payor-search?start=0&keyword="+randomnumber)
    pull = requests.get(urltester)
    print(pull.text)

    driver.get("https://www.dentrix.com/products/eservices/eclaims/payor-search?start=0&keyword=")
    searchbar= driver.find_element_by_css_selector('keyword')
    searchbar.send_keys(randomnumber)
    page = driver.page_source
    if pull.text != page :
        print("Issue found with payorID: " + randomnumber)
        i = 700
    
    



