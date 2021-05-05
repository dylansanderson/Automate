import bs4 as BeautifulSoup
import urllib.request
import matplotlib.pyplot as plt
from random import randint
def shortenName(s):
    if " " in s:
        spaceIndex = s.index(" ")
        return s[0] + "." + s[spaceIndex:]
    else:
        return s

"""
This program graphs the top scorers and assist-makers from 2007-current.
Choose the desired league with user input
This uses awful variable names, but it works

"""
try:
    choice = int(input("CHOOSE:" + "\n" + "1 for EPL" + "\n" + "2 for MLS" + "\n" + "3 for champions league" + "\n" + "4 for La Liga" + "\n" + "5 for Liga MX (Mexico Division 1)"))
except Exception:
    choice = randint(1,5)
    
SEASONS = [str(x) for x in range(2007,2021)]
GOALSSCORED, ASSISTS = [],[]
GOALSALLTIME, ASSISTSALLTIME = [],[]
TOPSCORERNAMES, TOPASSISTERNAMES = [],[]
CURRENTTOPSCORERS, CURRENTTOPASSISTERS = [],[]
for i in range(0,len(SEASONS)):
    if choice == 1:
        try:
            url = urllib.request.urlopen("https://www.espn.com/soccer/stats/_/league/ENG.1/season/"+ SEASONS[i] + "/view/scoring/english-premier-league")
        except Exception:
            url = urllib.request.urlopen("https://www.espn.com/soccer/stats/_/league/ENG.1/season/"+ SEASONS[i+1] + "/view/scoring/english-premier-league")
    elif choice == 2:
        try:
            url = urllib.request.urlopen("https://www.espn.com/soccer/stats/_/league/USA.1/season/"+SEASONS[i])
        except Exception:
            url = urllib.request.urlopen("https://www.espn.com/soccer/stats/_/league/USA.1/season/"+SEASONS[i+1])
    elif choice == 3:
        try:
            url = urllib.request.urlopen("https://www.espn.com/soccer/stats/_/league/UEFA.CHAMPIONS/season/"+SEASONS[i])
        except Exception:
            url = urllib.request.urlopen("https://www.espn.com/soccer/stats/_/league/UEFA.CHAMPIONS/season/"+SEASONS[i+1])
    elif choice == 4:
        try:
            url = urllib.request.urlopen("https://www.espn.com/soccer/stats/_/league/ESP.1/season/" + SEASONS[i])
        except Exception:
            url = urllib.request.urlopen("https://www.espn.com/soccer/stats/_/league/ESP.1/season/" + SEASONS[i+1])
    elif choice == 5:
        try:
            url = urllib.request.urlopen("https://www.espn.com/soccer/stats/_/league/MEX.1/season/" + SEASONS[i])
        except Exception:
            url = urllib.request.urlopen("https://www.espn.com/soccer/stats/_/league/MEX.1/season/" + SEASONS[i+1])
    soup = BeautifulSoup.BeautifulSoup(url,"html")
    firstTable = soup.find_all("table")[0]
    secondTable = soup.find_all("table")[1]
    firstTableTrees = firstTable.find_all("tr")
    secondTableTrees = secondTable.find_all("tr")
    for tr in firstTableTrees:
        spans = tr.find_all("span")
        CURRENTTOPSCORERS.append(str(spans[0].text))
        try:
            GOALSSCORED.append(int(spans[3].text))
        except:
            pass
    for tr in secondTableTrees:
        spans = tr.find_all("span")
        CURRENTTOPASSISTERS.append(str(spans[0].text))
        try:
            ASSISTS.append(int(spans[3].text))
        except:
            pass
    GOALSSCORED = GOALSSCORED[0:1]
    CURRENTTOPSCORERS = CURRENTTOPSCORERS[1:2]
    GOALSALLTIME.append(GOALSSCORED[0])
    TOPSCORERNAMES.append(CURRENTTOPSCORERS[0])
    ASSISTS = ASSISTS[0:1]
    CURRENTTOPASSISTERS = CURRENTTOPASSISTERS[1:2]
    ASSISTSALLTIME.append(ASSISTS[0])
    TOPASSISTERNAMES.append(CURRENTTOPASSISTERS[0])
    CURRENTTOPASSISTERS = []
    ASSISTS = []
    GOALSSCORED = []
    CURRENTTOPSCORERS = []
for x in range(0,len(TOPSCORERNAMES)):
    TOPSCORERNAMES[x] = shortenName(TOPSCORERNAMES[x])
    TOPSCORERNAMES[x] = TOPSCORERNAMES[x] + "-" +SEASONS[x]
for x in range(0,len(TOPASSISTERNAMES)):
    TOPASSISTERNAMES[x] = shortenName(TOPASSISTERNAMES[x])
    TOPASSISTERNAMES[x] = TOPASSISTERNAMES[x] + "-" +SEASONS[x]
plt.plot(TOPSCORERNAMES,GOALSALLTIME,'ro')
if choice == 1:
    plt.title("MOST GOALS - ENGLISH PREMIER LEAGUE - BY SEASON")
elif choice == 2:
    plt.title("MOST GOALS - MLS - BY SEASON")
elif choice == 3:
    plt.title("MOST GOALS - UEFA CHAMPIONS LEAGUE - BY SEASON")
elif choice == 4:
    plt.title("MOST GOALS - LA LIGA - BY SEASON")
elif choice == 5:
    plt.title("MOST GOALS - LIGA MX - BY SEASON")
plt.tick_params(axis='x', which='major', pad=-5)
plt.xticks(range(len(TOPSCORERNAMES)),TOPSCORERNAMES,rotation = 50,fontsize = 11.5)
plt.ylabel("GOALS",fontsize = 18)
plt.subplots_adjust(bottom = 0.25)
plt.grid(True)
plt.figure(2)
plt.plot(TOPASSISTERNAMES,ASSISTSALLTIME,'ro')
plt.tick_params(axis='x', which='major', pad=-5)
plt.xticks(range(len(TOPASSISTERNAMES)),TOPASSISTERNAMES,rotation = 50,fontsize = 11.5)
plt.grid(True)
plt.subplots_adjust(bottom = 0.25)
plt.ylabel("ASSISTS",fontsize = 18)
if choice == 1:
    plt.title("MOST ASSISTS - ENGLISH PREMIER LEAGUE - BY SEASON")
elif choice == 2:
    plt.title("MOSTS ASSISTS - MLS - BY SEASON")
elif choice == 3:
    plt.title("MOST ASSISTS - CHAMPIONS LEAGUE - BY SEASON")
elif choice == 4:
    plt.title("MOST ASSISTS - LA LIGA - BY SEASON")
elif choice == 5:
    plt.title("MOST ASSISTS - LIGA MX - BY SEASON")
plt.show()

