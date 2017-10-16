#!/usr/bin/python

class Mention:
  # @string - the fully qualified URL we found this mention on
  fromURL = None

  # @bool - Whether this mention was part of a link or regular text
  isLinked = False

  # @string - a snippet of the text surrounding the mention
  snippet = ""

  def __init__(self, fromURL, isLinked, snippet):
    '''
    Initialize as read-only
    '''
    self.fromURL = fromURL
    self.snippet = snippet
    # Not just setting directly from input, in case it's not boolean
    # Probably best to actually check and throw InputExceptions
    if isLinked:
      self.isLinked = True

  def getFromURL():
    return fromURL

  def isLinked():
    return isLinked

  def getSnippet():
    return snippet
