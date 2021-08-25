import requests
from selenium import webdriver
import random
import string
import urllib3
from bs4 import BeautifulSoup
import re

driver = webdriver.FirefoxProfile()
#downloads the website html file so that we are able to read the source code per line, this would allow for us to check the payeeID to see if the url is valid, then records it
urltester = ("https://www.dentrix.com/products/eservices/eclaims/payor-search?start=0&keyword=")
pull = requests.get(urltester)
print(pull.text)
with open ("QA Test file.txt", 'w') as f:
    f.write(pull)

payeeID = []
with open("QA Test file.txt") as f:
    while ( line := f.readLine().rstrip()):
        if ('/products/eservices/eclaims/payor-search?start=0&keyword=' in line):
            payee = payeeID.append(re.search('*">(.*)</a></td*', line)) #parses and appends payeeID to a list

#script enters the payeeid through the search bar to see if its valid
for i in payeeID:
    urltester = ("https://www.dentrix.com/products/eservices/eclaims/payor-search?start=0&keyword="+payeeID[i])
    pull = requests.get(urltester)
    print(pull.text)

    driver.get("https://www.dentrix.com/products/eservices/eclaims/payor-search?start=0&keyword=")
    searchbar= driver.find_element_by_css_selector('keyword')
    searchbar.send_keys(payeeID[i])
    page = driver.page_source
    if pull.text != page :
        print("Issue found with payeeID: " + payeeID[i])
        i = 700
    #tests the page with the auto entered one to see if it works and is reliable
