#Imports
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

#Given range
a = [i for i in range(873,1695)]

#Counter that will count the amount of time Pennsylvania is found in tables
counter = 0

#Initiate driver
chromedriver = 'C:/Users/Henry/Desktop/chromedriver'
driver = webdriver.Chrome(chromedriver)

#Loop through pages
for i in a:
    url = 'https://www.marijuanadoctors.com/user/admin/report/appointment_requests?page=' + str(i)
    #Driver get url
    driver.get(url)
    #Gives the program time for elements to load
    time.sleep(3)
    #Exception handle for popup message
    try:
        popUpRadio = driver.find_element_by_id('is21')
        popUpRadio.click()
        submit = driver.find_element_by_id('submitAgeGate')
        submit.click()
    except NoSuchElementException as exception:
        print("")
    #Log in only once
    try:
        userName = driver.find_element_by_id('qf_login_full__fields__email')   
        userName.send_keys('')#Blank for security  
        pw = driver.find_element_by_id('qf_login_full__fields__password')
        pw.send_keys('')#Blank for security
        logIn = driver.find_element_by_id('qf_login_full__submit')
        logIn.click()
    except NoSuchElementException as exception:
        print("")        
    time.sleep(2)
    #Data holds all table data
    data = driver.find_elements_by_tag_name('td')
    #b holds extracted text from web elements
    b = []
    for i in data:
        b.append(i.text)
    #Loop through extracted text to find Pennsylvania within table data
    for i in b:
        #if elements extracted equals given state increment counter by 1
        if i == 'Pennsylvania':#<------------------Change to state you wish to count
            counter += 1
driver.quit()