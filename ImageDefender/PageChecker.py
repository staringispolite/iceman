#!/usr/bin/python
from ImageDefender import Mention
from ImageDefender import Backlink

class PageChecker:
  # String, the canonical URL we're looking for.
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
    self.canonicalBacklink = canonicalBacklink
    self.brandname = brandname

  def checkURL(self, url):
    '''
    Checks the URL given for references to your brand or links to your site.
    @string url - fully qualified URL of a webpage that contains your IP
    '''
    # request contents of the page
    # Process URLs (using XPATH to pull <a> tags)
      # Check each URL for either domain or full match 
      # Create Backlink object
      # Store in class's object for later
    # Process mentions
      # Find tect matches for mentions of self.brandname
      # Create a Mention object
      # Store in class's object for later
    pass

  def getMentions(self):
    return self.mentions

  def getBacklinks(self):
    return self.backlinks


    
