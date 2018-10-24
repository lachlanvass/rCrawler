import requests
from random import randint
import re
class RandomWebPageCrawler():

    def __init__(self, startingUrlAddress:str, regexToFind):
        self.urlAddress = startingUrlAddress
        self.webText = self.getHTTPText() 
        self.pageData = []
        self.allData = {}
        self.links = []
        self.scrapedPages = []
        self.regexToFind = regexToFind

        # large websites to begin the crawler from in case it gets stuck
        self.backupAddresses = ["www.ign.com", "www.yahoo.com", 
        "www.bing.com", "www.mashable.com", "www.medium.com", 
        "www.youtube.com", "www.adobe.com", "www.google.com", 
        "www.reddit.com", "www.wikipedia.com", "www.amazon.com",
        "www.instagram.com", "www.stackoverflow.com"]

    def findData(self):
        data = re.findall(self.regexToFind, self.webText)
        self.pageData = data

    def findLinks(self):
        links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', self.webText)
        # filter some how to avoid following incorrect links
        self.links = links
    
    def crawl(self):
        webText = self.getHTTPText()
        self.findData()
        if self.pageData:
            for item in self.pageData:
                print(item)
        # keep record of all pages scraped
        self.scrapedPages.append(self.urlAddress)

        # keep record of all data found and from which web page
        self.allData.update({self.urlAddress:self.pageData})
        self.followRandomLink()

        # discard data from one page to gather new data in the next
        del self.pageData
    
    def followRandomLink(self):

        self.removeLinkDuplicates()
        try:
            randIndex = randint(0, len(self.links) - 1)
            self.urlAddress = self.links[randIndex]
            attemptedLink = self.urlAddress
        except ValueError:
            # No links on page. Follow backup address.
            print("No links found at this address. Trying a backup url.")
            randIndex = randint(0, len(self.backupAddresses) - 1)
            self.urlAddress = self.backupAddresses[randIndex]
        try:   
            self.webText = self.getHTTPText()
            print("Searchng: " + self.urlAddress)
        except requests.exceptions.ConnectionError:
            print("Connection error following link")
            print("Trying new link...")

            # remove link already attempted.
            self.links.remove(attemptedLink)
            # Call function again recusively.
            self.followRandomLink()


        
    def getHTTPText(self):
        # Remove redundant "http:// string from url"
        if (self.urlAddress.startswith("http://") or self.urlAddress.startswith("https://")):
            res = requests.get(self.urlAddress)
        else:
            res = requests.get("http://" + self.urlAddress)
        # add to scrapedPagesList to avoid scraping the same place twice
        #self.scrapedPages.append(self.urlAddress)
        return res.text

    def removeLinkDuplicates(self):
        self.links = set(self.links)
        self.links = list(self.links)

    # modify with functions to connect to DB, or harness data in some way.

# pageCrawler will find email addresses. 
pageCrawler = RandomWebPageCrawler("www.ign.com", r'[\w\.-]+@[\w\.-]+')
while True:
    pageCrawler.crawl()