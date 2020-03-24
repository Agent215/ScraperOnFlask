
#Abraham Schultz
#This is the test script for a proposed webscraper
#The webscraper will try and scrape course requirements for temple CIS

# get the request module and name it as uReq for future use
from urllib.request import urlopen
#get the beautifulSoup module and name as soup
from bs4 import BeautifulSoup as soup


def testScrape():

	returnList = []

	my_url ="https://bulletin.temple.edu/undergraduate/science-technology/computer-information-science/computer-science-bs/#requirementstext"
	#opening up connection and grabbing the page
	uClient = urlopen(my_url)
	# read page html content to variable 
	page_html = uClient.read()
	#close page connection
	uClient.close()

	# html parsing 
	page_soup = soup(page_html,"html.parser")
	# grabs each course requirment. does not grab the 
	# or requirements. will do later
	containers = page_soup.findAll("tr",{"class":"even"})

	# for now just grab one course
	# we will create a loop later that grabs all
	contain = containers[20]

	crn = contain.td.div.a["title"]
	name = contain.next.next.next.next.next.next
	#print out the course number!
	print(crn)
	#this is stupid for now but shows you what we could do
	#prints out the name of the course
	print(name)

	returnList.append(crn)
	returnList.append(name)

	return returnList
	print (len(containers))

if __name__ == "__main__":
    print(testScrape())