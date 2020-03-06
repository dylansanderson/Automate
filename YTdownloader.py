from selenium import webdriver
from time import sleep
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
""" 
1) input song into yt search bar
2) click on first result
3 copy current url, then driver.get("(downloader website)")
4) Enter the video link into query, click convert
5) once download option is displayed, click and let video download


"""
driver = webdriver.Chrome(executable_path = r'C:\Users\dylan\Desktop\303q\chromedriver.exe')
songs =["Enter song choice here"]   #enter song(s) desired into this list
count = 0
while count < len(songs):
    driver.get("https://www.YouTube.com")
    searchBar = driver.find_element_by_name("search_query")
    searchBar.send_keys(songs[count])
    searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
    searchButton.click()
    sleep(2)
    firstVid = driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
    firstVid.click()
    sleep(2)
    vidURL = str(driver.current_url)
    driver.get("https://ytmp3.cc/en13/")
    vidEntry = driver.find_element_by_name("video")
    vidEntry.send_keys(vidURL)
    convertButton = driver.find_element_by_xpath('//*[@id="submit"]')
    convertButton.click()
    wait = WebDriverWait(driver,60)
    element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="buttons"]/a[1]')))
    element.click()
    print("CLICKED")
    driver.switch_to_window(driver.window_handles[0])
    sleep(2)
    count += 1

sleep(10)
driver.close()

