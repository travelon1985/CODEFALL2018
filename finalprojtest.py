import csv
from itertools import islice

file = pickAFile()
print file
openFile = open(file, 'r')
reader = csv.reader(openFile)


def implied():
  counter = 0
  
  for row in islice(reader, 1, None):
    if counter < 100:
      homeImpliedProbability = 1 / float(row[14])
      awayImpliedProbability = 1 / float(row[15])
      drawImpliedProbability = 1 / float(row[16])
      row.append(round(homeImpliedProbability,2))
      row.append(round(awayImpliedProbability,2))
      row.append(round(drawImpliedProbability,2))
      counter = counter + 1
      print counter
      print row
      
  return reader



favoriteMatrix = [[0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0]]

def countBinner(reader):
  counter = 0
  matchCounter = 0
  for row in islice(reader, 1, None):
    if counter < 100:
      #homes greater with a 538 prediction > .5
      if row[6] > .5:
        counter = counter + 1
        print "rows counted: " + str(counter)
        if row[6] > .5 and row[6] < .6:
          print "rows counted second level: " + str(counter)
          if row[18] > .3 and row[17] < .4:
            favoriteMatrix[6][0] = favoriteMatrix[6][0] + 1
          if row[18] > .39 and row[17] < .5:
            favoriteMatrix[5][0] = favoriteMatrix[5][0] + 1
          if row[18] > .49 and row[17] < .6:
            favoriteMatrix[4][0] = favoriteMatrix[4][0] + 1
          if row[18] > .59 and row[17] < .7:
            favoriteMatrix[3][0] = favoriteMatrix[3][0] + 1
          if row[18] > .69 and row[17] < .8:
            favoriteMatrix[2][0] = favoriteMatrix[2][0] + 1
          if row[18] > .79 and row[17] < .9:
            favoriteMatrix[1][0] = favoriteMatrix[1][0] + 1 
          if row[18] > .89 and row[17] < 1:
            favoriteMatrix[0][0] = favoriteMatrix[0][0] + 1   
  print favoriteMatrix
          
      #away
      #if row[7] > .5:
        
homeFiveThirtyEightProb = {}
homeImpliedProb = {}


def edgeDictionary():
  print "hit"
  counter = 0
  for row in islice(reader, 1, None):
    uniqueKey = row[0]
    homeFiveProb = row[6]
    homeImpliedProbability = row[17]
    homeFiveThirtyEightProb[uniqueKey] = homeFiveProb
    homeImpliedProb[uniqueKey] = homeImpliedProbability


    
    
    
    
def edgeCalculator(dict1, dict2):
  homeEdge = {}
  print "hit2"
  counter = 0
  for item in dict1:
    fiveThirtyProb = dict1[item]
    impliedProb = dict2[item]
    homeEdge[item] = round(float(fiveThirtyProb) - float(impliedProb),2)
  return homeEdge
  
def edgeBinner(dict1):
  edgeBins = {}
  for item in homeEdge:
    initialFloor = -.29
    if homeEdge[item] >= initialFloor and < initialFloor + .01:
      edgeBins
      
    
                

def setup():
  #implied()
  #countBinner(reader)
  edgeDictionary()
  edgeCalculator(homeFiveThirtyEightProb, homeImpliedProb)
    

  
setup()
