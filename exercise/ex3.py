from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver_options = Options()
driver = webdriver.Firefox(
    options=driver_options,
    executable_path=r'/home/surya/Downloads/geckodriver')

actions = ActionChains(driver)
# geckodriver is for moxilladuck
driver.get("https://aims.iith.ac.in/aims/") 
print(driver.title)

'''
To find any element:
driver.find_element_by_xpath('//tagname[@ attributes = ]')
'''


LOGIN = str("ee18btech11026")
PWD = str("keA5nv4g")

Id = driver.find_element_by_id("uid")
Id.send_keys(LOGIN)

pwd = driver.find_element_by_id("pswrd")
pwd.send_keys(PWD)

CAP_1 = input("Enter the first Captcha : ")
cap_1 = driver.find_element_by_id("captcha")
cap_1.send_keys(CAP_1)

SignIn = driver.find_element_by_id("login")


SignIn.click()

CAP_2 = input("Enter the second Captcha : ")
cap_2 = driver.find_element_by_id("captcha")
cap_2.send_keys(CAP_2)

Submit = driver.find_element_by_id("submit")
Submit.click()

delay = 5

time.sleep(3)
Academic = driver.find_element_by_xpath('//span[@title="Academic"]').click()
View_my_course = driver.find_element_by_xpath('//span[@title = "View My Courses"]').click()

WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'feedback8572')))

Fb = driver.find_element_by_id("feedback8572" ).click()

WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'feedback_9433')))

	
driver.find_element_by_id('feedback_9433').click()


######## feedback starts here..
fb_R= WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'fbRemarks')))

remarks = str("great course!!")
fb_R.send_keys(remarks)


'''
Give the feedback on an overall scale : 

fb_scale ??

1 == 'SA'
2 == 'A'
3 == 'N'
4 == 'D'
5 == 'SD'
'''

fb_scale = 1
A = [9,12,15,18]
B = [range(1,5),range(1,10),range(1,5),range(1,4)]
	
def generate_xpath(i,j):
	prefix = str('/html/body/div[4]/div/div[1]/div[3]/div[1]/div[3]/')
	suffix = str('/div[1]/div[1]/div[2]/input[' + str(fb_scale) + ']')
	main = str('div[' + str(i) + ']/' + 'div[' + str(j) + ']' )
	return str(prefix + main + suffix)
	


for count in range(0,4):
	i = A[count]
	for j in B[count]:
		time.sleep(1)
		driver.find_element_by_xpath(generate_xpath(i,j)).click()
		
#driver.find_element_by_id('savefb').click()

'''


//*[@id="feedback8572"]
/html/body/div[4]/div[1]/div/div[3]/div[1]/div[3]/div[5]/div/ul[2]/li[2]/span[10]
/html/body/div[4]/div[1]/div/div[3]/div[1]/div[3]/div[5]/div/ul[2]/li[4]/span[10]

/html/body/div[4]/div[1]/div/div[3]/div[1]/div[3]/div[5]/div/ul[2]/li[1]/div[1]
'''
