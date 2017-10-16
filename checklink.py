#!/usr/bin/python
import argparse
from ImageDefender import PageChecker

canonicalURL = ""
targetURL = ""
domain = ""
brandname = ""

print "Analyzing '%s'" % targetURL
checker = PageChecker(canonicalURL, brandname)
backlinks = checker.getBacklinks()
mentions = checker.getMentions()

print "Searching for backlinks..."
print "Found %s" % len(backlinks)

print "Searching for mentions..."
print "Found %s" % len(mentions)


