from time import sleep
import bs4 as BeautifulSoup
import urllib.request
import matplotlib.pyplot as plt
import time
import re
import random

"""
This program uses beautifulsoup to fetch MLB data on various MLB hitting/pitching stats. Top 50 players in each catergory are recorded. Results graphed with Matplotlib
"""


colors = ["red","blue","green",'black','orange','purple']


def playerListChange(my_list):
    my_list = re.findall(r'\d+.*?(?=\d+|$)', my_list[0]) #uses a regex to alter list. ex) "['1Mike TroutLAA2Byron BuxtonMIN3Yermin MercedesCHW4Jesse..."] to ['1Mike TroutLAA' , '2Byron BuxtonMIN', '3Yermin MercedesCHW',...]
    return my_list

def getStrikeOutToAtBatRatio(lst):
    strikeOuttoAtBatList = []
    for x in range(0,len(lst)):
        strikeOuttoAtBatList.append(float(int(lst[x][12])/int(lst[x][2]))) #12th element/2nd element = S/O to BB ratio
    return strikeOuttoAtBatList

def getStrikeOutToAtWalkRatio(lst):
    strikeOutToWalkList = []
    for x in range(0,len(lst)):
        strikeOutToWalkList.append(float(int(lst[x][14])/int(lst[x][13])))
    return strikeOutToWalkList

def getHRtoAtBatRatio(lst):
    HRtoAtBatList = []
    for x in range(0,len(lst)):
        HRtoAtBatList.append(float(int(lst[x][8])/int(lst[x][2])))
    return HRtoAtBatList

def getPitchersERA(lst):
    ERAList = []
    for x in range(0,len(lst)):
        ERAList.append(float(float(lst[x][4])))  #grab the 4th item in the statslist, which is the ERA
    return ERAList

def getBattingAVG(lst):
    baList = []
    for x in range(0,len(lst)):
        baList.append(float(lst[x][5]))
    return baList



def statsListChange(data_list):  #this function changesa long, single-item list into a multi item list
    result =[]
    i=0
    while i <(len(data_list)-2):
        result.append(data_list[i:i+18])
        i+=18
    return result

pitcherStats = []
pitchersERA = []
pitchersSOtoBBratioList = []
pitcherNames = []
playerStats = []
playerNames = []
strikeOutToAtBatList = []
homeRunToAtBatList = []
battingAverageList = []


url = urllib.request.urlopen("https://www.espn.com/mlb/stats/player/_/view/batting") # Here, we pull up batting stats, and put data into lists for graphing later
soup = BeautifulSoup.BeautifulSoup(url,"lxml")
playerNameTable = soup.find_all("table")[0]
playerStatTable = soup.find_all("table")[1]
cols = playerStatTable.find_all("td")
tableColumns = playerStatTable.find_all("tr")
for name in playerNameTable:
    playerNames.append(name.get_text())
playerNames.remove(playerNames[0])
playerNames.remove(playerNames[0])
for t in cols:
    playerStats.append(t.get_text())
playerStats = statsListChange(playerStats)
playerNames = playerListChange(playerNames)
battingAverageList = getBattingAVG(playerStats)
strikeOutToAtBatList = getStrikeOutToAtBatRatio(playerStats)
homeRunToAtBatList = getHRtoAtBatRatio(playerStats)



url = urllib.request.urlopen("https://www.espn.com/mlb/stats/player/_/view/pitching") # Here, we pull up pitching stats, and put data into lists for graphing later
soup = BeautifulSoup.BeautifulSoup(url,"lxml")   
pitcherNameTable = soup.find_all("table")[0]     
pitcherStatTable = soup.find_all("table")[1]     
cols = pitcherStatTable.find_all("td")
for stat in cols:
    pitcherStats.append(stat.get_text())
for n in pitcherNameTable:
    pitcherNames.append(n.get_text())
for i in range(0,2):
    pitcherNames.remove(pitcherNames[0])
pitcherNames = playerListChange(pitcherNames)
pitcherStats = statsListChange(pitcherStats)
pitchersERA = getPitchersERA(pitcherStats)
pitchersSOtoBBratioList = getStrikeOutToAtWalkRatio(pitcherStats)



plt.figure(0)
plt.grid(True)
plt.subplots_adjust(bottom = 0.2)
plt.bar(playerNames,strikeOutToAtBatList,color = random.choice(colors))
plt.title("StrikeOuts/At-Bat ratio (Top 50 Hitters in MLB) - Lower = better")
plt.xticks(rotation = 87,fontsize = 12)
ymin = min(strikeOutToAtBatList)
xpos = strikeOutToAtBatList.index(ymin)
xmax = playerNames[xpos]
plt.annotate(str(playerNames[xpos]), xy=(xmax, ymin), xytext=(xmax, ymin-(ymin/5)),
            arrowprops=dict(facecolor='black'),
            )



plt.figure(1)
plt.grid(True)
plt.subplots_adjust(bottom = 0.2)
plt.bar(playerNames,battingAverageList,color = random.choice(colors))
plt.title("Best Batting Averages in MLB (Top 50 players)")
plt.xticks(rotation = 87,fontsize = 12)



plt.figure(2)
plt.grid(True)
plt.subplots_adjust(bottom = 0.2)
plt.bar(playerNames,homeRunToAtBatList,color = random.choice(colors))
plt.title("Ratio of Homeruns per At-Bat - (Top 50 Hitters in MLB) Higher = Better")
plt.xticks(rotation = 87,fontsize = 12)
ymax = max(homeRunToAtBatList)
xpos = homeRunToAtBatList.index(ymax)
xmax = playerNames[xpos]
plt.annotate(str(playerNames[xpos]), xy=(xmax, ymax), xytext=(xmax, ymax-(ymax/5)),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )




plt.figure(3)
plt.subplots_adjust(bottom = 0.2)
plt.title("Best Pitcher ERAs in MLB")
plt.xticks(rotation = 87,fontsize = 12)
plt.bar(pitcherNames,pitchersERA,color = random.choice(colors))
plt.grid(True)



plt.figure(4)
plt.title("Best StrikeOut to Walk Ratios - Higher = Better")
plt.grid(True)
plt.subplots_adjust(bottom = 0.2)
plt.bar(pitcherNames,pitchersSOtoBBratioList,color = random.choice(colors))
plt.xticks(rotation = 87,fontsize = 12)
ymax = max(pitchersSOtoBBratioList)
xpos = pitchersSOtoBBratioList.index(ymax)
xmax = pitcherNames[xpos]
plt.annotate(str(pitcherNames[xpos]), xy=(xmax, ymax), xytext=(xmax, ymax-(ymax/5)),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.show()

