#!/usr/bin/python
from ImageDefender import Mention
from ImageDefender import Backlink

# Adapted from http://docs.python-guide.org/en/latest/scenarios/scrape/
from lxml import html
import re
import requests
from urlparse import urlparse

class PageChecker:
  # urlparse object, the canonical URL we're looking for.
  canonicalBacklink = None;
  # String, the org we're looking for references of.
  brandname = None;
  # Array of Backlink objects
  backlinks = []
  # Array of Mention objects
  mentions = []
  # HTML elements to ignore the contents of
  blacklistTags = ['script']

  def __init__(self, canonicalBacklink, brandname):
    '''
    @string canonicalBacklink - Canonical URL of the page people should link back to
    @string brandname - The word or phrase you expect people to use when referring to you
    '''
    self.canonicalBacklink = urlparse(canonicalBacklink)
    self.brandname = brandname

  def checkURL(self, url):
    '''
    Checks the URL given for references to your brand or links to your site.
    @string url - fully qualified URL of a webpage that contains your IP
    '''
    # Request contents of the page.
    # TODO: cache these.
    page = requests.get(url)
    tree = html.fromstring(page.content)
    anchorTags = tree.xpath('a')
    # Process URLs (using XPATH to pull <a> tags)
    for (element, attribute, link, pos) in tree.iterlinks():
      # Check each URL for either domain or full match 
      #print "found a link for %s" % link
      checkingURL = urlparse(link)
      isCanonical = (self.canonicalBacklink.geturl() == checkingURL.geturl())
      isDomain = (self.canonicalBacklink.hostname == checkingURL.hostname)
      #print "--your domain: %s" % isDomain
      #print "--canonical: %s" % isCanonical
      if isDomain:
        # Create Backlink object
        backlink = Backlink(url, isDomain, isCanonical, element)
        # Store in class's object for later
        self.backlinks.append(backlink)
    # Find text matches for mentions of self.brandname
    for element in tree.iter():
      if element.tag not in self.blacklistTags:
        isLinked = (element.tag == "a")
        innerText = "%s" % element.text
        mentions = [m.start() for m in re.finditer(self.brandname, innerText)]
        for startIndex in mentions:
          # Create a Mention object
          snippetPadding = 20  # How many chars on each side to show
          snippetStart = max(0, startIndex - snippetPadding)
          snippetEnd = min(len(innerText), startIndex + len(self.brandname) + snippetPadding)
          snippet = innerText[snippetStart:snippetEnd]
          snippet = snippet.replace('\n', '')
          mention = Mention(url, isLinked, snippet)
          self.mentions.append(mention)

  def getMentions(self):
    return self.mentions

  def getBacklinks(self):
    return self.backlinks

  def getDomain(self):
    return canonicalBacklink.hostname

  def getCanonicalBacklink(self):
    return canonicalBacklink.geturl()


    
