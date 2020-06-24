from selenium import webdriver
from time import sleep
import random

"""
Auto-tweeting program.

"""

tweets = ["#hello world","#GordonRamsay .","Github.org ", "Spam Tweet"]    #List of desired tweets to send
alreadyTweetedStrings = []      

class Twitter:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\dylan\Desktop\303q\chromedriver.exe") #path to your chrome driver
        self.driver.maximize_window()
    def login(self):
        self.driver.get("https://twitter.com")
        sleep(2)
        try:                
            emailInputBox = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[1]/div/label/div/div[2]/div/input')
            emailInputBox.send_keys("email")
            passwordInputBox = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[2]/div/label/div/div[2]/div/input')
            passwordInputBox.send_keys("password")
            loginButton = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[3]/div')
            loginButton.click()
            sleep(2)
        except:                       
            print("EXCEPTION IN LOGIN")        #sometimes initial login button is moved, and this exception executes
            emailInputBox = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/form/div/div[1]/div/label/div/div[2]/div/input')
            emailInputBox.send_keys("email")
            passwordInputBox = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/form/div/div[2]/div/label/div/div[2]/div/input')
            passwordInputBox.send_keys("password")
            loginBTN = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/form/div/div[3]/div')
            loginBTN.click()
            sleep(2)
    def send_tweet(self,index):
        textInput = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        if not tweets[index] in alreadyTweetedStrings:
            textInput.send_keys(tweets[index])
            alreadyTweetedStrings.append(tweets[index])
            tweetButton = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
            tweetButton.click()
            sleep(1)
        else:
            tweets[index] = tweets[index] + str(random.randint(1,11))        #if tweet has been sent already, add random number to it and send again
            textInput.send_keys(tweets[index])
            alreadyTweetedStrings.append(tweets[index])
            tweetButton = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
            tweetButton.click()
            sleep(1)
    def quit(self):
        self.driver.quit()

t = Twitter()
t.login()
while True:
    i = random.randint(0,len(tweets)-1)         
    t.send_tweet(i)
t.quit()
