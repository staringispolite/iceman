#!/usr/bin/python
import argparse
from ImageDefender import PageChecker

parser = argparse.ArgumentParser(description='Check a URL for backlinks')
parser.add_argument('--canonical-url', dest='canonicalurl',
    help="The fully qualified URL of yours you expect to find a backlink for")
parser.add_argument('--target-url', dest='targeturl',
    help="The fully qualified URL to check for backlinks")
parser.add_argument('--brandname', dest='brandname',
    help="The word or phrase you expect in a mention of you/your org")
args = parser.parse_args()

canonicalURL = args.canonicalurl
targetURL = args.targeturl
brandname = args.brandname

print "Analyzing '%s'" % targetURL
checker = PageChecker(canonicalURL, brandname)
checker.checkURL(targetURL)
mentions = checker.getMentions()
backlinks = checker.getBacklinks()

print "\nSearching for mentions of \"%s\"..." % brandname
print "Found %s" % len(mentions)
for mention in mentions:
  print "-- %s" % mention.getSnippet()

print "\nSearching for backlinks to \"%s\"..." % canonicalURL
print "Found %s" % len(backlinks)
for link in backlinks:
  print "-- %s" % link.getHTML()
