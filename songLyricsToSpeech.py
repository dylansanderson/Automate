from gtts import gTTS 
import bs4 as BeautifulSoup
import urllib.request
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

"""
Lyric Scraper + text to speech generator

1) Go to website 'AZLyrics.com'
2) Find search bar, enter song, click search
3) Using bs4, extract song lyrics and put into a string, print the string to console
4) create text to speech object, passing in the string. Save this as an mp3 file
5) repeat until no more songs


"""



def shorten(s, subs):
    i = s.index(subs)      #function to shorten string pulled from html
    return s[:i+len(subs)]


initialURL = 'https://www.azlyrics.com/'
songs = ["soulja boy whats hannenin"]
songIndex = 0
language = ['en-US','en-GB']


driver = webdriver.Chrome(executable_path = r'C:\Users\dylan\Desktop\303q\chromedriver.exe')  #enter path of your chrome driver here
driver.get(initialURL)
sleep(2)
while songIndex < len(songs):
    searchBar = driver.find_element_by_xpath('//*[@id="q"]')
    searchBar.send_keys(songs[songIndex])                                                                                          #find searchbar, enter song, click 'search', then wait
    searchBTN = driver.find_element_by_xpath('//*[@id="search-collapse"]/form/div/span/button')
    searchBTN.click()
    sleep(3)
    try:                                                                                                                             #two possible xpaths for the first result of the search query
        firstResult = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/table/tbody/tr[1]/td/a/b')           
    except Exception:
        try:
            print("exception occured")
            firstResult = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/table/tbody/tr[2]/td/a/b')            
        except Exception:                 #if all else fails, go to next song in list                                         
            songIndex += 1                                 
            searchBar = driver.find_element_by_xpath('//*[@id="q"]')      
            for i in range(len(songs[songIndex-1])): #remove previous text from search bar
                searchBar.send_keys(Keys.BACKSPACE)                                                
            searchBar.send_keys(songs[songIndex])
            searchBTN = driver.find_element_by_xpath('//*[@id="search-collapse"]/form/div/span/button')   
            searchBTN.click()
            sleep(4)
            firstResult = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/table/tbody/tr[2]/td/a/b')
            

    firstResult.click()
    sleep(2)
    driver.close()                                       #close initial window
    driver.switch_to_window(driver.window_handles[0])    
    pageContent = ""
    currentURL = driver.current_url
    url = urllib.request.urlopen(currentURL).read()               #request the currentURL
    soup = BeautifulSoup.BeautifulSoup(url,'lxml')                #parse html with beautiful soup
    lyrics = soup.find_all('div',class_='col-xs-12 col-lg-8 text-center')               #find the div with the lyrics
    for lyric in lyrics:
        pageContent += lyric.get_text()
    pageContent = shorten(pageContent,'if  ')    # after the song lyrics, we always see an if statement, delete everything after it from our 'pageContent' string
    pageContent = pageContent[:-4]            #remove last 4 characters, which are 'if  ', from the pageContent string
    print(pageContent)
    myobj = gTTS(text=pageContent, lang=random.choice(language), slow=False)      #create text to speech object
    myobj.save(str(songs[songIndex])+"-T2S.mp3")                    #save as mp3 file
    songIndex += 1

driver.close()
