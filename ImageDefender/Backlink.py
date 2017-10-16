#!/usr/bin/python

class Backlink:
  # @string - the fully qualified URL we found this mention on
  fromURL = None

  # @bool - Whether this backlink was to the correct domain.
  isCorrectDomain = False

  # @bool - Whether this backlink was to the proper URL we want (not just proper domain).
  isCanonicalURL = False

  # @string - the HTML of the anchor tag containing the backlink
  html = ""

  def __init__(self, fromURL, isCorrectDomain, isCanonicalURL, html):
    '''
    Initialize as read-only
    '''
    # TODO: Add the URL of this link itself or just make it an ElementTree
    self.fromURL = fromURL
    self.html = html
    # Not just setting directly from input, in case it's not boolean
    # Probably best to actually check and throw InputExceptions
    if isCorrectDomain:
      self.isCorrectDomain = True
    if isCanonicalURL:
      self.isCanonicalURL = True

  def getFromURL(self):
    return self.fromURL

  def isCorrectDomain(self):
    return self.isCorrectDomain

  def isCanonicalURL(self):
    return self.isCanonicalURL

  def getHTML(self):
    return self.html
