#!/usr/bin/env python

from RandomWebPageCrawler import RandomWebPageCrawler
import argparse
from sys import argv
from math import inf

# Configure cmdline arg parser
parser = argparse.ArgumentParser(description="Crawl the web and by following random webpages")
parser.add_argument("-v", help="Verbose output mode", default=True)
parser.add_argument("-r", type=int, help="How many websites you want to crawl")
parser.add_argument("-f", help="Output file path.")
parser.add_argument("-w", help="Starting website")
parser.add_argument("-re", help="Regex to match")

print(parser.parse_args())

argList = parser.parse_args()

starterUrl = argv[1]
patternToMatch = argv[2]

verboseArg = argList.v
fileArg = argList.f
repsArg = argList.r
pageCrawler = RandomWebPageCrawler(starterUrl, patternToMatch)

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


print("Exiting")
