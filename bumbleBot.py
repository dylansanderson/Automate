from selenium import webdriver
from time import sleep
import random

""" Made for educational/experimental purposes only!"""



driver = webdriver.Chrome(executable_path=r"C:\Users\dylan\Desktop\303q\chromedriver.exe")         #enter path of your chrome driver
driver.get('https://bumble.com')
signInButton = driver.find_element_by_xpath('//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
signInButton.click()
sleep(1)
fbSignIn = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[1]/div')
fbSignIn.click()
main_window = driver.window_handles[0]
driver.switch_to_window(driver.window_handles[1])                        #switch to login screen

usernameIn = driver.find_element_by_xpath('//*[@id="email"]')
usernameIn.send_keys("ENTER YOUR USERNAME HERE")
pIn = driver.find_element_by_xpath('//*[@id="pass"]')                      #handle login-screen
pIn.send_keys("ENTER YOUR PASSWORD HERE")
LoginBtn = driver.find_element_by_xpath('//*[@id="u_0_0"]')
LoginBtn.click()

driver.switch_to_window(main_window)             #switch back to main screen
sleep(3)  #allow time for page content to load
while True:
    try:
        likeBTN = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/span/span')
        likeBTN.click()
    except Exception:
        try:
            keepSwiping = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div/div[2]/div')      #if match occurs, press keep swiping
            keepSwiping.click()
        except Exception:
            try:
                xbutton = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[2]')                       #additonal possible pop-up
                xbutton.click()
            except Exception:
                driver.close()
quit()