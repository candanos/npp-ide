import requests 
from bs4 import BeautifulSoup
import sys
import csv
from pathlib import Path
resultFolder = Path("C:/Users/CY59857/Desktop/")
resultFl='playersLiverpool.csv' 
resultFl = resultFolder / resultFl
headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

page = "https://www.transfermarkt.co.uk/fc-liverpool/spielplan/verein/31/saison_id/2016"
pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
Matches = pageSoup.find_all("a", {"title": "Match sheet"})
#Let's look at the first name in the Players list.
baseUrl = "https://www.transfermarkt.co.uk"
lst = []
for link in Matches:
	matchUrl = link.get('href')
	page = baseUrl + matchUrl
	pageTree = requests.get(page, headers=headers)
	pageSoup = BeautifulSoup(pageTree.content, 'html.parser')	
	subMenus = pageSoup.find_all("a", {"name": "SubNavi"}, {"class": "megaMenu"})
	lineupUrl = subMenus[2].get('href')
	print(lineupUrl)	
	
	# Players = pageSoup.find_all("a", {"class": "wichtig"})
	# for link in Players:
		# playerUrl = link.get('href') 
		# lst.append(playerUrl)
		
# csv.register_dialect('semicol', delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')	
# with open(resultFl, 'w', newline='') as f:
    # writer = csv.writer(f, 'semicol')
    # writer.writerows(lst)

