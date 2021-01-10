from selenium import webdriver
from time import sleep
import random
import datetime
"""
Auto-tweeting program. Signs into account and tweets the current time 'HH:MM:SS', using datetime module

"""   

class Twitter:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\dylan\Desktop\chromedriver.exe") #path to your chrome driver
        self.driver.maximize_window()
    def login(self):
        self.driver.get("https://twitter.com")
        sleep(2)
        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]').click()             
        emailInputBox = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        emailInputBox.send_keys("email")
        passwordInputBox = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        passwordInputBox.send_keys("password")
        loginButton = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div')
        loginButton.click()
        sleep(2)
    def send_tweet(self):
        textInput = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        textInput.send_keys(str(datetime.datetime.now()))
        tweetButton = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweetButton.click()
        sleep(1)
       
    def quit(self):
        self.driver.quit()
        print("Closing Driver")

t = Twitter()
t.login()
while True:        
    t.send_tweet()
    sleep(random.randint(120,280))            # Give time in between tweets to avoid Twitter's spam detection 
t.quit()
