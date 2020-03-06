from selenium import webdriver
from time import sleep


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\dylan\Desktop\303q\chromedriver.exe")        #enter the path of your driver here
        sleep(1)

    def login(self):
        self.driver.get('https://tinder.com')
        sleep(3)
        try:
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')    #login button
            fb_btn.click()
            
        except Exception:
            sleep(1)
            print("except")
            fb_btn2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]')
            fb_btn2.click()
        
        base_window = self.driver.window_handles[0]
        try:
            self.driver.switch_to_window(self.driver.window_handles[1])  #switch to login window
        except Exception:
            self.driver.refresh()
            sleep(3)
            moreOptions = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
            moreOptions.click()
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')              
            fb_btn.click()
            self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')  #email query (facebook)
        email_in.send_keys("Your Email")

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')  #password query (facebook)
        pw_in.send_keys("YOUR PASSWORD HERE")

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]') #Login Button
        login_btn.click()

        self.driver.switch_to_window(base_window)           #switch out of login screen, into main screen
        sleep(5)
        
        
    def scrollTest(self):
        self.close_popup()
        sleep(1)
        self.close_popup()
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0,500)")
        

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()
        

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()
    def sendToRandom(self):
        try:
            self.close_popup()
            sleep(1)
            self.close_popup()
            self.driver.maximize_window()
        except Exception:
            pass
        iconPic = self.driver.find_element_by_xpath('//*[@id="matchListNoMessages"]/div[35]/div[4]/a/div[1]')
        iconPic.click()
    def sendMessagesToMessaged(self,numMessages,message):
        index = 70
        try:
            self.close_popup()
            sleep(1)
            self.close_popup2()
            sleep(1)
        except Exception:
            pass
        cookiePopUp = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/button')
        cookiePopUp.click()
        matchesButton = self.driver.find_element_by_xpath('//*[@id="messages-tab"]')
        matchesButton.click()
        for i in range(0,numMessages):
            enterMessageButton = self.driver.find_element_by_xpath('//*[@id="matchListWithMessages"]/div[2]/a[' + str(index) + ']/div[2]/div[1]/div/h3')
            enterMessageButton.click()
            sleep(1)
            typeMessage = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
            sleep(1)
            typeMessage.send_keys(message)
            submit = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')
            submit.click()
            index += 1




    def sendMessagesToUnmessaged(self,numMessages,message):
        try:
            self.close_popup()
            sleep(1)
            self.close_popup2()
            sleep(1)
        except Exception:
            pass
        cookiePopUp = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/button')
        cookiePopUp.click()
        index = 2
        for i in range(0,numMessages):
            thumbnail = self.driver.find_element_by_xpath('//*[@id="matchListNoMessages"]/div[1]/div[' + str(index) +']/a/div[1]')
            thumbnail.click()
            sleep(3)
            textArea = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
            textArea.send_keys(message)
            sleep(1)
            submit = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')
            submit.click()
            sleep(1)
            matchesButton = self.driver.find_element_by_xpath('//*[@id="match-tab"]')
            matchesButton.click()
            sleep(1)

    def auto_swipe(self):
        self.close_popup()
        sleep(1)
        self.close_popup2()
        while True:
            try:
                self.like()
            except Exception:
                try:
                    self.closeHomeScreenPopUp()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        self.closeEmailPopUp()

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
