#### Program : AutoFeed "Automatic feedback giving bot for slothbears like you"
#### Version : 01
#### By : K.Surya Prakash
#### Date : Nov, 6 2020
#### update 01: 10 DEC 2020

'''
Current job : Gives feedback for the courses , which are due . Your user Id and pwd is given in the script itself. Need to input the 2 stage captcha manually in the cmd line.
Thats all you have to do. Autofeed finds the courses whose feedback is due, and gives feedback.
'''


#### TODO : 
'''
Need to figure out a way to solve captcha , to do the whole task in one click.
'''


#### Code : 

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

######## feedback starts here.. choosing the single button and choosing options is taken cate by this code part

def select_options():
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
			time.sleep(0.1)
			try:
				driver.find_element_by_xpath(generate_xpath(i,j)).click()
			except:### when we get to the end of the page and want to scrool..
				### typically needs twp scrolls for a full page...

				driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
				
				time.sleep(2)
				driver.find_element_by_xpath(generate_xpath(i,j)).click()
	driver.find_element_by_id('savefb').click()
	WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "back" ))).click()
	
	

###########################################################


driver_options = Options()
driver = webdriver.Firefox(
    options=driver_options,

		## ******************** IMPORTANT ************************
    executable_path=r'/home/surya/Downloads/geckodriver')   			#### Path for the geckodriver. 


# geckodriver is for moxilladuck
driver.get("https://aims.iith.ac.in/aims/") 					#### website URL
print(driver.title)

#### IMP : 

############################################  SETUP... detatils input...
		## ******************** IMPORTANT ************************
LOGIN = str("ee18btech*****")							#### User Id
PWD = str("**********")								#### Pwd

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

delay = 9

time.sleep(3)

driver.maximize_window()			## maximises the window...
driver.implicitly_wait(5)
## clicks Academic and opens My Courses
Academic = driver.find_element_by_xpath('//span[@title="Academic"]').click()
View_my_course = driver.find_element_by_xpath('//span[@title = "View My Courses"]').click()
time.sleep(5)
lists = []

##### Tries to extract the list of feedbacks to be given...
try : 
	### returns a list of elements which match the proporties of the icon whose feedback is open.
	lists = driver.find_elements_by_xpath('//*[@class="fb_status_change_icon"][@title = "Give Feedback"]')
except :
	driver.quit()	### window closes at the end..
	
print(len(lists))


############################# Choosing icons with feedback to be given..

while (len(lists)>0) :    ### iterating through lists one by one.
	i = lists[0]
	time.sleep(3)
	
	driver.execute_script("arguments[0].click()", i)
	time.sleep(2)

	WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,  '//*[@class = "fb_status_change_icon"]'  ))).click()
	time.sleep(3)
	select_options()
	lists = driver.find_elements_by_xpath('//*[@class="fb_status_change_icon"][@title = "Give Feedback"]')
	print(len(lists))
	

driver.quit()


