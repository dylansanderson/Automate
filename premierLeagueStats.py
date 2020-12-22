import bs4 as BeautifulSoup
import urllib.request
import matplotlib.pyplot as plt
import random

"""
This program uses bs4 to scrape team data of each English Premier League Soccer Team. Results are graphed with matplotlib.
To Run: >>pip install beautifulsoup4 OR pip3 install beautifulsoup4
        >>pip install urllib       OR   pip3 install urllib
        >>pip install matplotlib   OR   pip3 install matplotlib
"""


def Average(l):
    total = 0
    l = [i for i in l if i != 0]
    for x in l:
        total += x
    return round(total/len(l),2)

def getFirstName(s):
    for i in range(0,len(s)):
        if s[i].isdigit():
            digIndex = i
            return s[0:digIndex]

def getPosition(s):
    for i in range(0,len(s)):
        if s[i].isdigit():
            if s[i+1].isdigit():
                digIndex = i+1
            else:
                digIndex = i
            break
    return s[digIndex+1]
    
def getAge(s):
    for i in range(0,len(s)):
        if s[i].isdigit():
            if s[i+1].isdigit():
                digIndex = i+1
                break
            else:
                digIndex = i
            break
    return s[digIndex+2] + s[digIndex+3]
   

def getHeight(s):
    if '"' in s:
        apostrophe = s.index("'")
        quote = s.index('"')
        return s[apostrophe-1:quote+1]
    else:
        return 0

def getWeight(s):
    if "lbs" in s:
        ap = s.index('"')
        return s[ap+1:ap+4]
    else:
        return 0
def convertHeightToInches(s):
    try:
        feet = int(s[0])
        inches = int(s[s.index('"')-2] + s[s.index('"')-1])
        return (12 * feet) + inches
    except:
        return 0



    
urlIDs = ['375','360','361','367','364','359','363','376','398','383','370','331','357','371','382','380','384','368','362']     #ID of each premier league team, from ESPN website

random.shuffle(urlIDs)
WORDS = []
KEEPERS = []
HEIGHTS = []
WEIGHTS = []
AGES = []
POSITIONS = []
NAMES = []
for index in range(0,len(urlIDs)):
    url = urllib.request.urlopen("https://www.espn.com/soccer/team/squad/_/id/" + urlIDs[index])
    soup = BeautifulSoup.BeautifulSoup(url,'html')
    keeperTable = soup.find_all("table")[0]
    keeperRows = keeperTable.find_all("tr")
    outfieldTable = soup.find_all("table")[1]
    outfieldRows = outfieldTable.find_all("tr")
    clubName = soup.find("div",class_="flex justify-between mt3 mb3-mb4 items-center")
    for c in clubName:
        clubName = str(c.text)
    for t in outfieldRows:
        WORDS.append(t.text)
    for k in keeperRows:
        KEEPERS.append(k.text)
    KEEPERS.remove(KEEPERS[0])
    WORDS.remove(WORDS[0])
    WORDS = WORDS + KEEPERS
    for w in WORDS:
        print(w)
        NAMES.append(getFirstName(w))
        POSITIONS.append(getPosition(w))
        try:
            AGES.append(int(getAge(w)))
        except:
            AGES.append(0)
        HEIGHTS.append(convertHeightToInches(getHeight(w)))
        WEIGHTS.append(int(getWeight(w)))
    for n in range(0,len(NAMES)):
        NAMES[n] = NAMES[n] + " (" + POSITIONS[n] + ")" 
    
    print(HEIGHTS)
    plt.tick_params(axis='x', which='major', pad=-5)
    plt.plot(NAMES,AGES,'ro')
    plt.text(.1,(Average(AGES)-2),"TOTAL SENIOR SQUAD MEMBERS: " + str(len(NAMES)))
    plt.text(.1,(Average(AGES))-2.5,"FORWARDS: " + str(POSITIONS.count('F')))
    plt.text(.1,(Average(AGES)) -3,"MIDFIELDERS: " + str(POSITIONS.count('M')))
    plt.text(.1,(Average(AGES))- 3.5,"DEFENDERS: " + str(POSITIONS.count('D')))
    plt.text(.1,(Average(AGES)) -4,"GOALKEEPERS: " + str(POSITIONS.count('G')))
    plt.ylabel("AGE (Years)")
    plt.xticks(range(len(NAMES)),NAMES,rotation = 63,fontsize = 8.5)
    plt.axhspan(0.96*float(Average(AGES)), 1.04*float(Average(AGES)), color='yellow', alpha=0.6)
    plt.grid(True)
    plt.title(clubName + "\n" + "AVERAGE AGE: " + str(Average(AGES)))
    plt.figure(index+2)
    plt.tick_params(axis='x', which='major', pad=-5)
    plt.xticks(range(len(NAMES)),NAMES,rotation = 63,fontsize = 8.5)
    plt.axhspan(0.96*float(Average(WEIGHTS)), 1.04*float(Average(WEIGHTS)), color='yellow', alpha=0.6)
    plt.title(clubName+ ": WEIGHT PER PLAYER" + "\n" + "AVERAGE WEIGHT: " + str(Average(WEIGHTS)) + " lbs")
    plt.ylabel("Weight (lbs)")
    plt.grid(True)
    plt.plot(NAMES,WEIGHTS,'b^')
    ft = int(Average(HEIGHTS)//12)
    inches = round(Average(HEIGHTS)%12,2)
    plt.text(0,100,"AVERAGE HEIGHT: " + str(ft)+"ft "+ str(inches) + " in.",fontsize = 14)
    plt.show()
    WORDS = []
    KEEPERS = []
    HEIGHTS = []
    WEIGHTS = []
    AGES = []
    POSITIONS = []
    NAMES = []
    

