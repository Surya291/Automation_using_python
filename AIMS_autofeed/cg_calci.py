#### Program : Find_my_GPA
#### Version : 01
#### By : K.Surya Prakash
#### Date : Jan, 9 2020
#### update 01: 9 Jan 2020



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd



########################################
###   Functions reqd.

def letter_2_digit(letter):
	if(letter == ' A+'):
		return 10
	elif(letter == ' A'):
		return 10
	elif(letter == ' A-'):
		return 9
	elif(letter == ' B'):
		return 8
	elif(letter == ' B-'):
		return 7
	elif(letter == ' C'):
		return 6
	elif(letter == ' C-'):
		return 5
	elif(letter == ' D'):
		return 4
	else:
		return 0
		
#####################################



#### Opening my courses : 

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
LOGIN = str("ee18btech11026")							#### User Id
PWD = str("keA5nv4g")								#### Pwd

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
SEM_list = []


sems = driver.find_elements_by_xpath('//*[@class="subCnt"]')

Major_C,Major_P = 0,0
Minor_C,Minor_P = 0,0

for i in sems:
	
	SC,SP = 0,0
	
	courses = i.find_elements_by_tag_name('li')
	
	for crs in courses[1:] : 
		grade = (crs.find_elements_by_xpath('.//span[@class = "col8 col"]')[0].text)
		
		if(grade!=' S' and grade!=' '):
			name = 	(crs.find_elements_by_xpath('.//span[@class = "col2 col"]')[0].text)
			creds = float(crs.find_elements_by_xpath('.//span[@class = "col3 col"]')[0].text)
			
			
			SC = SC + creds
			SP = SP +  creds*letter_2_digit(grade)

	
	if(SC!=0):
		SPA  = SP/SC
		
		if 'Minor' in courses[0].text : 
			Minor_C+=SC
			Minor_P+=SP
		else :
			Major_C+=SC
			Major_P+=SP
		
		print('--------------------------------------\n')
		print(courses[0].text )
		print(" SPA :", round(SPA,2)  )
		print('\n--------------------------------------\n')
		print('\n')
		
		
print("<><><><><><><><><><><><><><><><><><><><><>\n")
Major_CG = Major_P/Major_C
print("Major CGPA : ", round(Major_CG,2))
print("\n<><><><><><><><><><><><><><><><><><><><><>\n")

if(Minor_C>0):
	print("<><><><><><><><><><><><><><><><><><><><><>\n")
	Minor_CG = Minor_P/Minor_C
	print("Minor CGPA : ", round(Minor_CG,2))
	print("\n<><><><><><><><><><><><><><><><><><><><><>\n")
	
	
print("")
driver.quit()
