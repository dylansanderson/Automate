from time import sleep
import bs4 as BeautifulSoup
import urllib.request
import statistics
import matplotlib.pyplot as plt
import numpy as np
import time



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

def average(listOfPrices):
    total = 0
    for i in listOfPrices:
        total += i
    return total/len(listOfPrices)

inputList = []


searchQuery = input("enter an item to search for on eBay")
searchQuery = searchQuery.replace(' ','+')      #replace spaces with '+' to feed into url request
print(searchQuery)
discardedResults = []
listOfPrices = []
pageNumber = 1
now = time.time()
while pageNumber < 3:
    url = urllib.request.urlopen('https://www.ebay.com/sch/i.html?_nkw=' + searchQuery + '&rt=nc&LH_Sold=1&LH_Complete=1&_blrs=spell_check&_pgn='+str(pageNumber)).read()  #ebay url of search query
    soup = BeautifulSoup.BeautifulSoup(url,'lxml')
    prices = soup.find_all('span',class_='s-item__price')     #find the price of each item on the page
    for p in prices:
        priceString = p.get_text()
        priceString = priceString.replace('$','')         #remove dollar sign before storing as float
        priceString = priceString.replace(',','')      #remove comma if in the string
        if not ' ' in priceString:           # if the price is a range, i.e. "$19.99-$49.99", do not include it in the listOfPrices
            priceString = float(priceString)
            listOfPrices.append(priceString)
        else:
            discardedResults.append(priceString)          
    pageNumber += 1

runTime = time.time() - now


for i in range(int(len(listOfPrices)/5)):
    listOfPrices.remove(max(listOfPrices))           #for better precision, remove the max and min of the list n times before calculating avg. and median
    listOfPrices.remove(min(listOfPrices))

for i in range(0,len(listOfPrices)):
    inputList.append(i)

print(discardedResults)
print("Runtime: " + str(runTime))
median = str(statistics.median(listOfPrices))
print("Found "+str(len(listOfPrices)) +" recently completed/sold transactions for "+ searchQuery + " on eBay: " + "\n")
print(listOfPrices)
print("\n")
print("Average price of " +searchQuery + ": $" +str(average(listOfPrices)) + "\n")
print("Median Price of " + searchQuery + ": $" + median)


#find Mean Average Deviation
yIncrement = np.mean(np.absolute(listOfPrices-np.mean(listOfPrices)))
yTickList = np.arange(min(listOfPrices) - min(listOfPrices)/10,max(listOfPrices) + max(listOfPrices)/10,yIncrement)
searchQuery = searchQuery.replace('+',' ') 
plt.plot(inputList,listOfPrices,'r^')
plt.ylim(0.95*min(listOfPrices),max(listOfPrices))
plt.yticks(yTickList)
plt.xlabel("search result number")
plt.ylabel("Price of " + searchQuery + " ($)")
plt.title("Graph of " + searchQuery + "\n" + "Median Price: $" + median + "\n" + "Average Price: $" + str(average(listOfPrices)))
plt.grid(True,axis = 'y',alpha = 0.75, ds = 'steps-pre')
plt.show()

