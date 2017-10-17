#!/usr/bin/python
import argparse
from ImageDefender import PageChecker
from ImageDefender import CSVTask

parser = argparse.ArgumentParser(description='Check a URL for backlinks')
parser.add_argument('--csv-task', dest='csvFilename',
    help="The full path to a CSV PageChecker task")
parser.add_argument('-v', dest='verbose', default=False,
    action="store_true", help="Print details as it goes")
args = parser.parse_args()

csvTask = CSVTask(args.csvFilename)
canonicalURL = csvTask.getCanonicalURL()
discoveredURLs = csvTask.getDiscoveredURLs()
brandname = csvTask.getBrandNames()[0]  # For now, only do one brand mention search

checker = PageChecker(canonicalURL, brandname)
result = None
for targetURL in discoveredURLs:
  if args.verbose:
    print "Analyzing '%s'" % targetURL

  result = checker.checkURL(targetURL)
  if result.wasSuccessful():
    mentions = result.getMentions()
    backlinks = result.getBacklinks()

    if args.verbose:
      print "\nSearching for mentions of \"%s\"..." % brandname
      print "Found %s" % len(mentions)
      for mention in mentions:
        print "[...]%s[...]" % mention.getSnippet()
      print "\nSearching for backlinks to \"%s\"..." % canonicalURL
      print "Found %s" % len(backlinks)
      for link in backlinks:
        print "-- %s" % link.getHTML()
      print "\n"
  else:
    print "URL FAILED"

csvTask.writePageCheckerResultsToFile(checker, "output.csv")

