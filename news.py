from bs4 import BeautifulSoup
from urllib.request import urlopen
from pync import Notifier
import os
import time

def news(rssFeedUrl):
	count = 0

	parseFeedUrl = urlopen(rssFeedUrl)
	page = parseFeedUrl.read()
	parseFeedUrl.close()

	soupPage = BeautifulSoup(page, "xml")
	newsList = soupPage.find_all("item")
	
	for news in newsList:
		time.sleep(5) #Pauses system for 5 milliseconds
		if(count < 5): #Notifies you about the first 5 items on RSS Feed
			
			Notifier.notify('Tesla News', title = news.title.text, 
                    appIcon='/Users/joshuawelsh/Desktop/PythonScripts/TeslaNewsApp/App/newsIcon.png', open=news.link.text)
			Notifier.remove(os.getpid())
			
		count = count + 1
	
def indexes():
  NEWS_RSS_FEED = "http://finance.yahoo.com/rss/headline?s="
	print("Please enter stock indexes: \n")
	str = input()
	URL = NEWS_RSS_FEED + str
	print(URL)
	return URL

url = indexes()
print(url)
news(url)
