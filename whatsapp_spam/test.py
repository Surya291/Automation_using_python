'''
Reference article:
https://medium.com/dsc-srm/make-a-whatsapp-spammer-in-under-10-lines-of-python-code-b414024db8e
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path=r'/home/surya/Downloads/geckodriver')
# geckodriver is for moxilla
#driver.implicitly_wait(5) # delay for 5 sec
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 600)

def spammer():
    n = input("How many times should I bomb : ")
    delay = input("Delay btw msgs : ")
    driver.find_element_by_css_selector("span[title='" + input("Enter name to spam: ") + "']").click()
    inputString = input("Enter message to send: ")
    for i in range(int(n)):
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
        time.sleep(int(delay))
        print('done !!')
'''
def spammer():
    n = input("How many times should I bomb : ")
    delay = input("Delay btw msgs : ")
    target = input("Enter name to spam: ")
    string = input("Enter message to send: ")

    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()
    inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
    input_box = wait.until(EC.presence_of_element_located(( By.XPATH, inp_xpath)))

    for i in range(int(n)):
        input_box.send_keys(string + Keys.ENTER)
        time.sleep(int(delay))
        print('done !!')
'''




while(True):
    try:
        spammer()
    except:
        print("Sorry try other :(")
        spammer()
