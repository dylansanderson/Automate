from selenium import webdriver
from time import sleep
import random

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\dylan\Desktop\chromedriver.exe")        #enter the path of your driver here
        sleep(1)

    def login(self):
        self.driver.get('https://tinder.com')
        sleep(3)
        loginBTN = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        loginBTN.click()
        sleep(2)
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]')    #facebook login button
        fb_btn.click()
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])  #switch to login window
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')  #email query (facebook)
        email_in.send_keys("email")
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')  #password query (facebook)
        pw_in.send_keys("password")
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]') #Login Button
        login_btn.click()
        self.driver.switch_to_window(base_window)           #switch out of login screen, into main screen
        sleep(3)

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()
        
    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def sendBioInReverse(self,numMessages):
        try:
            self.close_popup()
            sleep(1)
            self.close_popup2()

        except Exception:
            pass
        try:
            cookiePopUp = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
            cookiePopUp.click()
        except:
            pass
        self.driver.maximize_window()
        for i in range(0,numMessages):
            thumbnail = self.driver.find_element_by_xpath('//*[@id="matchListNoMessages"]/div[1]/div[2]/a/div[1]')
            thumbnail.click()
            sleep(3)
            try:
                bio = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]')
                message = bio.text
            except:
                message = "(empty bio)"
            message = message[::-1]
            if len(message) == 1 or len(message) == 0:
                message = "your bio is short"
            textArea = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
            try:
                textArea.send_keys(message)
            except:
                message = "Hello"
                textArea.send_keys(message)
            sleep(2)
            submit = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')
            submit.click()
            sleep(3)
            matchesButton = self.driver.find_element_by_xpath('//*[@id="match-tab"]')
            matchesButton.click()
            sleep(3)

    def sendMessagesToMessaged(self,numMessages,message):
        self.driver.maximize_window()
        try:
            self.close_popup()
            sleep(1)
            self.close_popup2()
            sleep(1)
        except Exception:
            pass
        try:
            cookiePopUp = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
            cookiePopUp.click()
        except:
            pass
        sleep(1)
        matchesButton = self.driver.find_element_by_xpath('//*[@id="messages-tab"]')
        matchesButton.click()
        for i in range(0,numMessages):
            enterMessageButton = self.driver.find_element_by_xpath('//*[@id="matchListWithMessages"]/div[2]/a[7]/div[2]/div[1]')
            enterMessageButton.click()
            sleep(1)
            typeMessage = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
            sleep(1)
            typeMessage.send_keys(message)
            submit = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')
            submit.click()
        sleep(3)

    def sendMessagesToUnmessaged(self,numMessages,message):
        self.driver.maximize_window()
        sleep(1)
        try:
            self.close_popup()
            sleep(1)
            self.close_popup2()
            sleep(1)
        except Exception:
            pass
        try:
            cookiePopUp = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
            cookiePopUp.click()
        except:
            pass
        for i in range(0,numMessages):
            try:
                thumbnail = self.driver.find_element_by_xpath('//*[@id="matchListNoMessages"]/div[1]/div[4]/a')                       #find thumbnail, click
                thumbnail.click()
                sleep(3)
                textArea = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
                textArea.send_keys(message)
                sleep(1)
                submit = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')    #submit
                submit.click()
                sleep(1)
                matchesButton = self.driver.find_element_by_xpath('//*[@id="match-tab"]')                                        #click matches button
                matchesButton.click()
                sleep(1)
            except Exception:
                self.driver.refresh()
                sleep(3)

    def auto_swipe(self):
        sleep(2)
        try:
            self.close_popup()                 #close potential pop-ups
            sleep(1)
            self.close_popup2()
        except:
            pass
        try:
            cookiePopUp = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
            cookiePopUp.click()
        except:
            pass
        while True:
            try:
                sleep(0.3)
                self.like()
            except Exception:
                try:
                    self.closeHomeScreenPopUp()          
                except Exception:                                 #handle potential pop-ups with try-except statements
                    try:
                        self.close_match()
                    except Exception:
                        try:                  
                            self.closeEmailPopUp()
                        except Exception:
                            print("Sleeping for 1 min...")
                            sleep(60)
                            self.driver.refresh()            
                           

    def closeEmailPopUp(self):
        remindMeLater = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/button[2]')
        remindMeLater.click()
            
    def closeHomeScreenPopUp(self):
        sleep(2)
        pop = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        pop.click()   

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_3.click()
        sleep(3)

    def close_popup2(self):
        popup1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup1.click()
        sleep(2)
    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()
bot.auto_swipe()
bot.driver.close()
bot.driver.quit()

