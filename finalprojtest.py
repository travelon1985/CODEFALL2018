import csv
from itertools import islice

file = pickAFile()
print file
openFile = open(file, 'r')
reader = csv.reader(openFile)

def implied():
  for row in islice(reader, 1, None):
    homeImpliedProbability = 1 / float(row[14])
    awayImpliedProbability = 1 / float(row[15])
    drawImpliedProbability = 1 / float(row[16])
    row.append(round(homeImpliedProbability,2))
    row.append(round(awayImpliedProbability,2))
    row.append(round(drawImpliedProbability,2))
    print row
  return reader

implied()

def

  


    
    

  
  
