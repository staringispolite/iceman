#!usr/bin/python
import csv
from ImageDefender import PageChecker

class col:
  '''CSV file column definitions
  '''
  ORIGINAL_URL = 1
  BRAND_NAMES = 1
  HOST = 0
  DISCOVERED_PAGE_URL = 1
  DISCOVERED_IMAGE = 2
  SOURCE_IMAGE = 3
  SOURCE_ENGINE = 4
  DATE = 5
  WIDTH = 6
  HEIGHT = 7

  def __init__(self):
    pass

class CSVTask:
  '''A reader/writer of the format ImageDefender uses. Example:
  '''
  
  canonicalURL = None
  brandNames = []
  discoveredURLs = []

  def __init__(self, filename):
    '''Load from CSV file
    Original Url, http://www.target.com/blog/post/1044
    Brand name, "Target"

    Host, Discovered Page URL, Discovered Image, Source Image, Source Engine, Date, Width, Height
    [rows]
    '''
    with open(filename, 'rb') as csvfile:
      reader = csv.reader(csvfile)
      i = 0
      for row in reader:
        if i == 0:
          # Row for original URL
          self.canonicalURL = row[col.ORIGINAL_URL]
        elif i == 1:
          # Brand name row
          brandNames = row[col.BRAND_NAMES]
          self.brandNames = brandNames.split(",")
        elif (i == 2) or (i == 3):
          # 2 is a blank row, 3 is the column headers
          pass
        else:
          # URL row
          self.discoveredURLs.append(row[col.DISCOVERED_PAGE_URL])
        i += 1

  def getCanonicalURL(self):
    return self.canonicalURL

  def getBrandNames(self):
    return self.brandNames

  def getDiscoveredURLs(self):
    return self.discoveredURLs
  
  def writePageCheckerResultsToFile(self, pageChecker, outfile):
    '''Write an array of PageChecker results to CSV file. Example:
    Original Url, http://www.target.com/blog/post/1044
    Brand name, "Target"

    Discovered URL, Successful?, # Backlinks, # Direct, # Domain-only, # Mentions, Domain Pagerank
    [rows]
    @array pageCheckers - an array of PageChecker objects that've run already
    @string outfile - the full or relative path for a file to write
    '''
    with open(outfile, 'wb') as csv_file:
      canonicalURL = pageChecker.getCanonicalBacklink()
      csvwriter = csv.writer(csv_file)
      csvwriter.writerow(["Canonical URL", canonicalURL])
      csvwriter.writerow(["Brand name(s)", pageChecker.getBrandName()])
      csvwriter.writerow([])
      csvwriter.writerow(["Discovered URL", "Successful?", "# Backlinks", "# Direct",
        "# Domain-only", "# Mentions", "Domain Pagerank"])
      for result in pageChecker.getResults():
        if result.wasSuccessful():
          csvwriter.writerow([result.getURL(), result.wasSuccessful(),
              result.numBacklinks(), result.numCanonicalLinks(),
              result.numDomainLinks(), len(result.getMentions()), ''])
        else:
          csvwriter.writerow([result.getURL(), result.wasSuccessful(),
              "N/A", "N/A", "N/A", "N/A", ""])

