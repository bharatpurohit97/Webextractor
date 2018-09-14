



import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

driver = webdriver.Chrome(executable_path='/home/admin2/chromedriver') 
base_url = "https://en.wikipedia.org/wiki/E-commerce"
driver.get(base_url)
new_name = []
email=[]
text = driver.find_element_by_tag_name("body").get_attribute('innerHTML')
new_name.append(re.findall('http[.]?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',text))
new_name = list(set(sum(new_name,[])))
x=0
try:
    for p in new_name:
        p =str(p)
        driver.get(p)
        print (x, p)
        text = driver.find_element_by_tag_name("body").get_attribute('innerHTML')
        new_name.append(list(set(re.findall('http[.]?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',text))))
        email.append(re.findall(r'[\w\.-]+@[\w\.-]+',text))
        x = x+1
except:
    pass
driver.close()
