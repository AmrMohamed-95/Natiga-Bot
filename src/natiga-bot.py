from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import datetime
import sys

def get_result(result_no):
	
	# open academy site in firefox	
	print 'Opening firefox........'	
	br = webdriver.Firefox()
	br.maximize_window()
	br.get('http://engmet.org/stdlogin.aspx?st=s&url=/students/natigaterm2.aspx')
	

	# fill fields with data
	time.sleep(1)
	print 'Filling data........'
	time.sleep(1)
	username = br.find_element_by_id('username')
	password = br.find_element_by_id('password')
	
	username.send_keys('6676') # my id
	password.send_keys('amrmohamedelsaid95') # my password
	
	# click login	
	time.sleep(1)
	print 'Logging in..........'
	time.sleep(1)
	login_btn = br.find_element_by_id('btnlogin')
	login_btn.click()
	
	# take a screenshot
	time.sleep(1)
	print 'Taking screenshot..........'
	br.save_screenshot('photo_' + str(result_no) + '_1.png')
	time.sleep(1)
	br.execute_script("window.scrollTo(0, 300)") 
	br.save_screenshot('photo_' + str(result_no) + '_2.png')
	br.execute_script("window.scrollTo(200, 300)") 	
	br.save_screenshot('photo_' + str(result_no) + '_3.png')
	br.execute_script("window.scrollTo(100, 800)") 	
	br.save_screenshot('photo_' + str(result_no) + '_4.png')
	
	
	# closing browser
	time.sleep(1)
	print 'Closing firefox..........'	
	time.sleep(1)
	br.quit()

result_no = 1
print '\n\nStarting program'
while True:
	try:
		while True:
			# stop the script if time is after 4pm
			now = datetime.datetime.now()
			if now.hour >= 16:
				print '\n\nExiting program'			
				sys.exit(0)

			if now.hour < 14:
				print '\nWaiting 30 mins to check again if it is 2'
				time.sleep(1800)
			else:
				print '\n\n*****Getting a result*****'	
				get_result(result_no)	
				# time to wait until taking the next result
				print '\nWaiting 20 mins before getting the next result'			
				time.sleep(1200) # every 20 mins
				result_no += 1

	except Exception as e:
		print '\nError: Something went wrong'
		print e
		pass
