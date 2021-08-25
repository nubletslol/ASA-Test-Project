import requests
from selenium import webdriver
import random
import string
import urllib3
from bs4 import BeautifulSoup
import re

driver = webdriver.FirefoxProfile()
#downloads the website html file so that we are able to read the source code per line, this would allow for us to check the payor name to see if the url is valid, then records it
urltester = ("https://www.dentrix.com/products/eservices/eclaims/payor-search?start=0&keyword=")
pull = requests.get(urltester)
print(pull.text)
with open ("QA Test file.txt", 'w') as f:
    f.write(pull)

payorName = []
with open("QA Test file.txt") as f:
    while ( line := f.readLine().rstrip()):
        if ('/products/eservices/eclaims/payor-search?start=0&keyword=' in line):
            payor = payorName.append(re.search('*</td><td>(.*)</td><td*>', line)) #parses and appends payor name to a list

#script enters the payor name through the search bar to see if its valid
for i in payorName:
    urltester = ("https://www.dentrix.com/products/eservices/eclaims/payor-search?start=0&keyword="+payorName[i])
    pull = requests.get(urltester)
    print(pull.text)

    driver.get("https://www.dentrix.com/products/eservices/eclaims/payor-search?start=0&keyword=")
    searchbar= driver.find_element_by_css_selector('keyword')
    searchbar.send_keys(payorName[i])
    page = driver.page_source
    if pull.text != page :
        print("Issue found with Payor Name: " + payorName[i])
        i = 700
    #tests the page with the auto entered one to see if it works and is reliable







