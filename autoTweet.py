from selenium import webdriver
from time import sleep
import random
import datetime
"""
Auto-tweeting program. Signs into account and tweets the current time 'HH:MM:SS', using datetime module
"""   

class Twitter:
    def __init__(self,email,password):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\dylan\Desktop\chromedriver.exe") #path to your chrome driver
        self.driver.maximize_window()
        self.email = email
        self.password = password
    def login(self):
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(2)
               
        emailInputBox = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        emailInputBox.send_keys(self.email)
        nextBTN = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div').click()
        sleep(1)
        try:
            PWentry = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(self.password)
            loginBTN = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div').click()
            sleep(1)
        except Exception: #exception if prompted for extra verification.. input phone number
            phoneInput = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys("XXX-XXX-XXXX")
            nextBTN = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div').click()
            sleep(2)
            PWentry = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(self.password)
            loginBTN = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div').click()
        sleep(2)
    def send_tweet(self):
        textInput = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        textInput.send_keys("The Current time is: " + str(datetime.datetime.now()))
        tweetButton = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweetButton.click()
        sleep(1)
       
    def quit(self):
        self.driver.quit()
        print("Closing Driver")

t = Twitter("email@domain.com","PASSWORD123")
t.login()
while True:        
    t.send_tweet()
    sleep(random.randint(200,1500))            # Give time in between tweets to avoid Twitter's spam detection 
