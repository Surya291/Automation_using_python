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
time.sleep(10)

Academic = driver.find_element_by_xpath('//span[@title="Academic"]').click()
View_my_course = driver.find_element_by_xpath('//span[@title = "View My Courses"]').click()


#driver.implicitly_wait(5)
#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.SHIFT + 'k')

#Academic = driver.find_element_by_xpath("//*[contains(text(), 'Student')]")
#actions.send_keys(Keys.COMMAND + Keys.ALT + 'k')
#WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_tag_name("body")).send_keys(Keys.CONTROL + Keys.SHIFT + 'k')

point1 = '''
// ==UserScript==
// @name        GPA meter
// @namespace   http://192.168.0.103:9090
// @description A user script to show GPA on aims page
// @include     http://192.168.0.103:9090/aims/courseReg/myCrsHistoryPage?*
// @version     1
// @grant       none
// ==/UserScript==

var exclude_list = [
  'Minor Core',
  'Honors Core',
  'Honours project',
  'Honours coursework',
  'FCC',
  'Additional'
];
var grade_values = {
  'A+': 10,
  'A': 10,
  'A-': 9,
  'B': 8,
  'B-': 7,
  'C': 6,
  'C-': 5,
  'D': 4,
  'FR': 0,
  'FS': 0
};
'''

point2= '''
console.log(studentId);
append_checkbox = function(parent, is_checked){
	parent.append("<input class=\"cgpa_cal_check\" type=\"checkbox\" "+(is_checked?"checked":"")+" />");
}
'''

point3 = '''
add_checkboxes = function(){
	var courses_checked = new Set();

	$(".cgpa_cal_check").remove();

	elems = $(".hierarchyLi.dataLi").not(".hierarchyHdr, .hierarchySubHdr");

	elems.each(function(i){
		var course_id = $(this).children(".col1").html().trim();
		if (courses_checked.has(course_id)){
			append_checkbox($(this).children(".col1"), false);
			return;
		}
		is_checked = true;
		type = $(this).children(".col5").html().trim().slice(6);
		grade = $(this).children(".col8").html().trim().slice(6);
		console.log(grade, grade.length);
		if (exclude_list.indexOf(type) > -1 || grade == "" || grade == "I")
			is_checked = false;
		if (is_checked)
			courses_checked.add(course_id);
		append_checkbox($(this).children(".col1"), is_checked);
	});
}
'''
point4 = '''
show_total_gpa = function(){
	$('#gpa_button').val('Calculating');
 	$('#gpa_bar').remove();
 	total_grades = 0;
 	total_credits = 0;
 	if ($(".cgpa_cal_check").length==0)
 		add_checkboxes();
 	elems = $(".hierarchyLi.dataLi").not(".hierarchyHdr, .hierarchySubHdr");
 	elems.each(function(i){
 		if ($(this).find(".cgpa_cal_check:checked").length == 0 )
 			return;
 		grade = $(this).children(".col8").html().trim().slice(6);
 		credits = $(this).children(".col3").html().trim().slice(6);
 		if (!(grade in grade_values))
 			return;
 		grade = grade_values[grade];
 		credits = Number(credits);
 		total_grades += credits * grade;
 		total_credits += credits;
 	});

 	console.log(total_grades, total_credits);
 	var gpa = (total_grades / total_credits).toFixed(2);
 	$('#gpa_button').val('Show Gpa');
	$('#courseHistoryUI .clear').after('<ul id="gpa_bar" class="subCnt"><li class="hierarchyLi dataLi hierarchyHdr changeHdrCls"><span class="col"> TOTAL GPA </span></li><li class="hierarchyLi dataLi"><span class="col1 col">&nbsp;</span><span class="col2 col">Total GPA of graded courses</span><span class="col3 col">&nbsp;</span><span class="col4 col">&nbsp;</span><span class="col5 col">&nbsp;</span><span class="col6 col">&nbsp;</span><span class="col7 col">&nbsp;</span><span class="col4 col">' + gpa + '</span></li></ul>');
}

'''

point5 = '''
if (!(typeof unsafeWindow === 'undefined')) {
  unsafeWindow.show_total_gpa = show_total_gpa;
  unsafeWindow.exclude_list = exclude_list;
  unsafeWindow.add_checkbox = add_checkbox;
  unsafeWindow.grade_values = grade_values;
}
$('#studentCourseSearch').before('<input id="gpa_button" class="btn" value="Peekav" style="width:75px; margin-right:10px; opacity:1;" type="button" onclick="show_total_gpa();"></input>');
'''


time.sleep(5)

WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_tag_name("body")).send_keys(Keys.CONTROL + Keys.SHIFT + 'k')
'''
driver.execute_script(point1)
driver.execute_script(point2)
driver.execute_script(point3)
driver.execute_script(point4)
driver.execute_script(point5)
'''
