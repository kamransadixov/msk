from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
import sys
import os

browser = webdriver.Firefox()

for url in range(1,126):
	for url2 in range(1,50):
		try:
			website = 'https://www.infocenter.gov.az/page/voters/?s='+ str(url) +'&sm='+ str(url2) +''
			browser.get(website)
			for divnumber in range(1,5000):
				try:
					fullname_html = browser.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[2]/div/div/div[3]/table/tbody/tr['+ str(divnumber) +']/td[4]')
					fullname = fullname_html.get_attribute("innerHTML")
					address_html = browser.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[2]/div/div/div[3]/table/tbody/tr['+ str(divnumber) +']/td[5]')
					address = address_html.get_attribute("innerHTML")
					yob_html = browser.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[2]/div/div/div[3]/table/tbody/tr['+ str(divnumber) +']/td[6]')
					yob = yob_html.get_attribute('innerHTML')
					if " KAMRAN " in fullname:
						print("|", fullname, " "*(40-len(fullname)),"|", address,  " "*(50-len(address)), "|", yob,  " "*(8-len(yob)), "|")
				except NoSuchElementException:
					pass
		except NoSuchElementException:
			pass
