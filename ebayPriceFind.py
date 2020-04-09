from selenium import webdriver
from time import sleep
import bs4 as BeautifulSoup
import urllib.request
import statistics
from selenium.webdriver.common.keys import Keys

"""
This program searches COMPLETED/SOLD listings only on eBay for your search query.
It adds the price of each item of search result into a list, then generates an average+median price for that item.

sample input:'modern warfare ps4'

sample output:

Found 60 recently completed/sold transactions for modern warfare ps4 on eBay. 

99, 39.79, 40.0, 41.0, 32.0, 44.99, 42.0, 30.0, 50.0, 44.0, 45.0, 39.99, 39.99, 40.0, 45.95, 40.0, 38.99, 36.99, 34.0, 41.0, 39.99, 50.0, 34.99, 36.0, 37.99, 49.0, 45.0, 33.0, 51.0]


Average price of modern warfare ps4: $42.42383333333332

Median Price of modern warfare ps4: $41.5


"""


def shorten(s, subs):
    i = s.index(subs)          #function to shorten string pulled from html
    return s[:i+len(subs)]


def average(listOfPrices):
    total = 0
    for i in listOfPrices:
        total += i
    return total/len(listOfPrices)

searchQuery = input("enter an item to search for on eBay")
searchQuery = searchQuery.replace(' ','+')      #replace spaces with '+' to feed into url request
print(searchQuery)

listOfPrices = []
pageNumber = 1

while pageNumber < 4:
    url = urllib.request.urlopen('https://www.ebay.com/sch/i.html?_nkw=' + searchQuery + '&rt=nc&LH_Sold=1&LH_Complete=1&_blrs=spell_check&_pgn='+str(pageNumber)).read()  #ebay url of search query
    soup = BeautifulSoup.BeautifulSoup(url,'lxml')
    prices = soup.find_all('span',class_='s-item__price')     #find the price of each item on the page
    for p in prices:
        priceString = p.get_text()
        priceString = priceString.replace('$','')         #remove dollar sign before storing as float
        try:
            priceString = priceString.replace(',','')       #if there is a comma in price, delete the comma
            priceString = shorten(priceString,' ')           #if the price is something like '$49.99 to $59.99' we shorten the string to include just first the number
            priceString = priceString[:-1]                   #remove the last character, ' '
        except:
            pass
        try:
            priceString = float(priceString)
            listOfPrices.append(priceString)
        except:
            pass                      
    pageNumber += 1



for i in range(int(len(listOfPrices)/5)):
    listOfPrices.remove(max(listOfPrices))           #for better precision, remove the max and min of the list n times before calculating avg. and median
    listOfPrices.remove(min(listOfPrices))


median = statistics.median(listOfPrices)
median = str(median)
searchQuery = searchQuery.replace('+',' ')   #switch '+' back to spaces
print("Found "+str(len(listOfPrices)) +" recently completed/sold transactions for "+ searchQuery + " on eBay: " + "\n")
print(listOfPrices)
print("\n")
print("Average price of " +searchQuery + ": $" +str(average(listOfPrices)) + "\n")
print("Median Price of " + searchQuery + ": $" + median)

