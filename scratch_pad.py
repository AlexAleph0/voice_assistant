from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

s = Service('/usr/local/bin/chromedriver')
# driver = webdriver.Chrome(service=s)

# Using Selenium
def google_search(search_term):
    browser = webdriver.Chrome(service=s)
    browser.get('http://www.google.com')
    search = browser.find_element(By.NAME, 'q')
    search.send_keys(search_term)
    search.send_keys(Keys.RETURN)
    
    
google_search('Fender Strat HSS')



