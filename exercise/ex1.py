from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

'''
This exercise shows to do a automatic google search !!
'''

driver = webdriver.Firefox(executable_path=r'/home/surya/Downloads/geckodriver')
# geckodriver is for moxilladuck
driver.get("https://www.google.com/")
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("what is selenium")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
#driver.close()
