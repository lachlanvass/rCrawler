
from RandomWebPageCrawler import RandomWebPageCrawler
import pyodbc
import requests

server = "scrapedemailserver.database.windows.net"
database = "emailDatabase"
username = "lachybalboa"
password = "Zooba22#"
driver = "{ODBC Driver 13.1 for SQL Server}"

connectionString = "Driver={ODBC Driver 13 for SQL Server};Server=tcp:scrapedemailserver.database.windows.net,1433;Database=emailDatabase;Uid=lachybalboa@scrapedemailserver;Pwd={Zooba22#};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

class EmailRandomWebPageCrawler(RandomWebPageCrawler):

    def __init__(self, startingUrlAddress, regexToFind):
        super(EmailRandomWebPageCrawler, self).__init__(startingUrlAddress, regexToFind)
        self.cnxn = pyodbc.connect(connectionString)
        self.cursor = self.cnxn.cursor()
        #row = self.cursor.fetchone()


    # Override insertIntoDB method which will be called in the crawl method
    def insertIntoDB(self, emailAddress, fromWebsite):
        query = "INSERT INTO Entries VALUES ('{}', '{}')".format(emailAddress, fromWebsite)
        print(query)
        self.cursor.execute(query)
        self.cnxn.commit()


emailCrawler = EmailRandomWebPageCrawler("www.achieve3000.com/contact-us/", r'[\w\.-]+@[\w\.-]+')
while True:
    emailCrawler.crawl(verbose=True, insertIntoDB=True)
