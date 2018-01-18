from selenium import webdriver


import bs4 , requests 

loginId = 'f20160126'
password = ''  #ENTER PASSWORD

browser = webdriver.Firefox() 
browser.get('http://10.1.0.10:8090/')

# Clicking on username and typing
username = browser.find_element_by_id('usernametxt')
username.click()
username.send_keys(loginId)

# Clicking on password and typing
passwd = browser.find_element_by_name('password')
passwd.click()
passwd.send_keys(password) 

#Clicking on Login 
login = browser.find_element_by_name('btnSubmit')
login.click() 

browser.quit()