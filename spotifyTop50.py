from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

"""
This program retrieves the top 50 spotify songs, and downloads them 1 by 1 via YouTube to MP3. Uses the selenium WebDriver module.
"""


driver = webdriver.Chrome(executable_path = r'C:\Users\dylan\Desktop\chromedriver.exe') #enter PATH of your driver here
songList = []
driver.get("https://spotifycharts.com/regional") #List of top 200 Spotify songs
sleep(2)
for i in range(1,51):
    song = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/span/table/tbody/tr[' +str(i) + ']/td[4]/strong').text #find each song title on page
    songList.append(str(song)) #add each song title to songList
print("TOP 50 SONGS: " + "\n")
print(songList)
count = 0
while count < len(songList):
    driver.get("https://www.YouTube.com")
    searchBar = driver.find_element_by_name("search_query")
    searchBar.send_keys(songList[count]+ " song")
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
    wait = WebDriverWait(driver,30) #wait for the conversion to complete and download to be ready. Wait for 30 seconds Max
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="buttons"]/a[1]')))
        element.click()
        print("DOWNLOADED " + songList[count])
        driver.switch_to_window(driver.window_handles[0])
        sleep(2)
        count += 1
    except Exception:
        print("RETRYING DOWNLOAD OF " + str(songList[count])) #try again, after having waited some time (30 seconds). Sometimes when downloading too many videos in a row, the website makes you wait.
                   
sleep(10)
driver.close()
driver.quit()
