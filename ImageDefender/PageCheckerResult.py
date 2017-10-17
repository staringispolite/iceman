#!usr/bin/python

class PageCheckerResult:
  '''Used by PageChecker to create read-only results for its checks
  '''
  url = None
  backlinks = []
  domainBacklinks = []
  canonicalBacklinks = []
  mentions = []
  successful = None

  def __init__(self, url, backlinks, mentions, successful):
    self.url = url
    # Initialize new objects so they don't carry over
    self.backlinks = []
    self.domainBacklinks = []
    self.canonicalBacklinks = []
    self.mentions = []
    self.successful = successful

    # Add links to each
    for link in backlinks:
      self.backlinks.append(link)
      if link.isCanonicalLink():
        self.canonicalBacklinks.append(link)
      elif link.isDomainLink():
        self.domainBacklinks.append(link)
    for mention in mentions:
      self.mentions.append(mention)
    #print "%d links total" % self.numBacklinks()
    #print "%d domain" % self.numDomainLinks()
    #print "%d canonical" % self.numCanonicalLinks()

  def getURL(self):
    return self.url

  def getMentions(self):
    return self.mentions

  def getBacklinks(self):
    return self.backlinks

  def getCanonicalLinks(self):
    return self.canonicalBacklinks

  def getDomainLinks(self):
    return self.domainBacklinks

  def numBacklinks(self):
    return len(self.backlinks)

  def numCanonicalLinks(self):
    return len(self.canonicalBacklinks)

  def numDomainLinks(self):
    return len(self.domainBacklinks)

  def wasSuccessful(self):
    return self.successful
