#!/usr/bin/env python

from RandomWebPageCrawler import RandomWebPageCrawler
import argparse
from sys import argv
from math import inf

helpString = ''' rCrawler - crawl the web by following random webpages 
                This is a web crawler built in Python. 
                Use the -w option to select a starting website to crawl.
                Use -re to select a regular expression to search for. 
                If a match is found it will be outputted to the console.
                Use -f to select a file to output results to.  '''
# Configure cmdline arg parser
parser = argparse.ArgumentParser(description=helpString)
parser.add_argument("-v", help="Verbose output mode", default=True)
parser.add_argument("-r", type=int, help="How many websites you want to crawl")
parser.add_argument("-f", help="Output file path.")
parser.add_argument("-w", help="Starting website")
parser.add_argument("-re", help="Regex to match")

argList = parser.parse_args()

starterUrl = argList.w
patternToMatch = argList.re

verboseArg = argList.v
fileArg = argList.f
repsArg = argList.r
pageCrawler = RandomWebPageCrawler(starterUrl, patternToMatch)

print(argv)
print("Beginning crawl...")

if repsArg != None:
    print("Will crawl " + str(repsArg) + " websites.")

if repsArg == None:
    # infinite loops
    repsArg = inf

counter = 0
while counter < repsArg:
    if fileArg != None:
        pageCrawler.crawl(outputToFile=True, outputPath=fileArg)
    elif fileArg != None and verboseArg != None:
        pageCrawler.crawl(outputToFile=True, outputPath=fileArg, verbose=True)
    elif verboseArg != None:
        pageCrawler.crawl(verbose=True)

    if repsArg != None:
        # increase counter if n repeitions are chosen
        # else it is an infinite loop
        counter += 1


print("Crawl finished. Exiting")
