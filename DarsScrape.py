from urllib.request import urlopen
#get the beautifulSoup module and name as soup
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def DarsScrape():

	returnList = []
	#driver = webdriver.Chrome(ChromeDriverManager().install())  
	#use the above this if you are having trouble adding web driver to path variable
	driver = webdriver.Chrome()

	driver.get("http://dars.temple.edu")

	#tuName = sys.argv[1]
	#passW = sys.argv[2]
	# wait for elements to load
	driver.implicitly_wait(6)
	userLogin = driver.find_element_by_id('username')
	passLogin = driver.find_element_by_id('password')

	# add you TU login and pass here. we will need to get this from the user and pass it here
	userLogin.send_keys("tuk85386")
	passLogin.send_keys("!Alamo2020")

	driver.find_element_by_name("_eventId_proceed").click()
	# wait for elements to load
	driver.implicitly_wait(6)
	# try and enter two factor auth if needed
	try:
		#there is another doc embedded inside the main html doc, its inside an html iframe
	    iframe = driver.find_element_by_xpath("//iframe[1]")
		#switch to that doc
	    driver.switch_to_frame(iframe)
	    driver.find_element_by_xpath("//form[1]/div/fieldset/div/button").click()
	    driver.switch_to.default_content()
	except:
	    pass
	# wait for elements to driver.switch_to.default_content()

	#driver.switch_to.default_content()
	runAudit = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.ID, "runAudit")))
	#runAudit = driver.find_element_by_id('runAudit')
	runAudit.click()
	driver.implicitly_wait(6)
	# get in to actual DARS data display page, we can scrape after this
	driver.find_element_by_xpath("//tbody[1]/tr[2]/td[10]/a").click()

	driver.implicitly_wait(2)
	# wait for url to load and get current url
	source = driver.page_source
	# copy page reached from selenium 
	page_soup = soup(source,"html.parser")
	# grab all rows of all courses taken, there are duplicates here
	# im thinking one way we could do this is remove duplicates then compare against reqs
	tableRows = page_soup.findAll("tr",{"class":"takenCourse"})

	# initialize empty list to hold courses
	courseList = []

	# add each course taken to a list
	for table in tableRows:
	    tmp = table.td.next.next.next.next
	    courseList.append(tmp)

	#function to remove duplicates
	def Remove(duplicate): 
	    final_list = [] 
	    for num in duplicate: 
	        if num not in final_list: 
	            returnList.append(num)
	            final_list.append(num) 
	    return final_list 
	#print(Remove(courseList)) 

	removedList = []
	removedList = Remove(courseList)

	# print list with duplicates removed
	for course in removedList:
	    print(course)


	#example of picking just one course and getting its data.
	#exampleCourse = tableRows[20]
	#someCourse = exampleCourse.td.next.next.next.next
	#print(someCourse)
	print("number of courses completed: " + str(len(removedList)))
	#close page connection
	driver.close()
	return removedList