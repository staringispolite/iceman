#!/usr/bin/python
from ImageDefender import Mention
from ImageDefender import Backlink

# Adapted from http://docs.python-guide.org/en/latest/scenarios/scrape/
from lxml import html
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
        # TODO: Just store the ElementTree object?
        elementHTML = element.tostring()
        # Create Backlink object
        backlink = Backlink(url, isDomain, isCanonical, elementHTML)
        # Store in class's object for later
        self.backlinks.append(backlink)
    # Process mentions
      # Find tect matches for mentions of self.brandname
      # Create a Mention object
      # Store in class's object for later
    pass

  def getMentions(self):
    return self.mentions

  def getBacklinks(self):
    return self.backlinks

  def getDomain(self):
    return canonicalBacklink.hostname

  def getCanonicalBacklink(self):
    return canonicalBacklink.geturl()


    
