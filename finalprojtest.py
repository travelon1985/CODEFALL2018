import csv
from itertools import islice

file = pickAFile()
print file
openFile = open(file, 'r')
reader = csv.reader(openFile)


def implied():
  counter = 0
  
  for row in islice(reader, 1, None):
    #if counter < 100:
      homeImpliedProbability = 1 / float(row[14])
      awayImpliedProbability = 1 / float(row[15])
      drawImpliedProbability = 1 / float(row[16])
      row.append(round(homeImpliedProbability,2))
      row.append(round(awayImpliedProbability,2))
      row.append(round(drawImpliedProbability,2))
      counter = counter + 1
      print counter
      print row
      
  



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
  rowCounter = 0
  for row in islice(reader, 1, None):
    if counter < 500:
      #homes greater with a 538 prediction > .5
      if float(row[6]) > 0.5:
        counter = counter + 1
        print "rows counted: " + str(counter)
        if float(row[6]) > .5 and float(row[6]) < .6:
          print "rows counted second level: " + str(counter)
          
          #less than 1 so .99 and greater than .89 so .90
          if float(row[17]) < 1 and float(row[17]) > 0.89:
            favoriteMatrix[0][0] = favoriteMatrix[0][0] + 1
            
          #less than .90 so .89 and greater than .79 so .80
          elif float(row[17]) < 0.90 and float(row[17]) > .79:
            favoriteMatrix[1][0] = favoriteMatrix[1][0] + 1
            
          elif float(row[17]) < 0.80 and float(row[17]) > .69:
            favoriteMatrix[2][0] = favoriteMatrix[2][0] + 1
            
          elif float(row[17]) < 0.70 and float(row[17]) > .59:
            favoriteMatrix[3][0] = favoriteMatrix[3][0] + 1
            
          elif float(row[17]) < 0.60 and float(row[17]) > .49:
            favoriteMatrix[4][0] = favoriteMatrix[4][0] + 1
            
          elif float(row[17]) < 0.50 and float(row[17]) > .39:
            favoriteMatrix[5][0] = favoriteMatrix[5][0] + 1
          
          elif float(row[17]) < 0.40 and float(row[17]) > .29:
            favoriteMatrix[6][0] = favoriteMatrix[6][0] + 1
            
        
        if float(row[6]) > .59 and float(row[6]) < .7:
          print "rows counted second level: " + str(counter)
          
          #less than 1 so .99 and greater than .89 so .90
          if float(row[17]) < 1 and float(row[17]) > 0.89:
            favoriteMatrix[0][1] = favoriteMatrix[0][1] + 1
            
          #less than .90 so .89 and greater than .79 so .80
          elif float(row[17]) < 0.90 and float(row[17]) > .79:
            favoriteMatrix[1][1] = favoriteMatrix[1][1] + 1
            
          elif float(row[17]) < 0.80 and float(row[17]) > .69:
            favoriteMatrix[2][1] = favoriteMatrix[2][1] + 1
            
          elif float(row[17]) < 0.70 and float(row[17]) > .59:
            favoriteMatrix[3][1] = favoriteMatrix[3][1] + 1
            
          elif float(row[17]) < 0.60 and float(row[17]) > .49:
            favoriteMatrix[4][1] = favoriteMatrix[4][1] + 1
            
          elif float(row[17]) < 0.50 and float(row[17]) > .39:
            favoriteMatrix[5][1] = favoriteMatrix[5][1] + 1
          
          elif float(row[17]) < 0.40 and float(row[17]) > .29:
            favoriteMatrix[6][1] = favoriteMatrix[6][1] + 1
        
        if float(row[6]) > .69 and float(row[6]) < .8:
          print "rows counted second level: " + str(counter)
          
          #less than 1 so .99 and greater than .89 so .90
          if float(row[17]) < 1 and float(row[17]) > 0.89:
            favoriteMatrix[0][2] = favoriteMatrix[0][2] + 1
            
          #less than .90 so .89 and greater than .79 so .80
          elif float(row[17]) < 0.90 and float(row[17]) > .79:
            favoriteMatrix[1][2] = favoriteMatrix[1][2] + 1
            
          elif float(row[17]) < 0.80 and float(row[17]) > .69:
            favoriteMatrix[2][2] = favoriteMatrix[2][2] + 1
            
          elif float(row[17]) < 0.70 and float(row[17]) > .59:
            favoriteMatrix[3][2] = favoriteMatrix[3][2] + 1
            
          elif float(row[17]) < 0.60 and float(row[17]) > .49:
            favoriteMatrix[4][2] = favoriteMatrix[4][2] + 1
            
          elif float(row[17]) < 0.50 and float(row[17]) > .39:
            favoriteMatrix[5][2] = favoriteMatrix[5][2] + 1
          
          elif float(row[17]) < 0.40 and float(row[17]) > .29:
            favoriteMatrix[6][2] = favoriteMatrix[6][2] + 1
            
        if float(row[6]) > .79 and float(row[6]) < .9:
          print "rows counted second level: " + str(counter)
          
          #less than 1 so .99 and greater than .89 so .90
          if float(row[17]) < 1 and float(row[17]) > 0.89:
            favoriteMatrix[0][3] = favoriteMatrix[0][3] + 1
            
          #less than .90 so .89 and greater than .79 so .80
          elif float(row[17]) < 0.90 and float(row[17]) > .79:
            favoriteMatrix[1][3] = favoriteMatrix[1][3] + 1
            
          elif float(row[17]) < 0.80 and float(row[17]) > .69:
            favoriteMatrix[2][3] = favoriteMatrix[2][3] + 1
            
          elif float(row[17]) < 0.70 and float(row[17]) > .59:
            favoriteMatrix[3][3] = favoriteMatrix[3][3] + 1
            
          elif float(row[17]) < 0.60 and float(row[17]) > .49:
            favoriteMatrix[4][3] = favoriteMatrix[4][3] + 1
            
          elif float(row[17]) < 0.50 and float(row[17]) > .39:
            favoriteMatrix[5][3] = favoriteMatrix[5][3] + 1
          
          elif float(row[17]) < 0.40 and float(row[17]) > .29:
            favoriteMatrix[6][3] = favoriteMatrix[6][3] + 1
            
        if float(row[6]) > .89 and float(row[6]) < 1:
          print "rows counted second level: " + str(counter)
          
          #less than 1 so .99 and greater than .89 so .90
          if float(row[17]) < 1 and float(row[17]) > 0.89:
            favoriteMatrix[0][4] = favoriteMatrix[0][4] + 1
            
          #less than .90 so .89 and greater than .79 so .80
          elif float(row[17]) < 0.90 and float(row[17]) > .79:
            favoriteMatrix[1][4] = favoriteMatrix[1][4] + 1
            
          elif float(row[17]) < 0.80 and float(row[17]) > .69:
            favoriteMatrix[2][4] = favoriteMatrix[2][4] + 1
            
          elif float(row[17]) < 0.70 and float(row[17]) > .59:
            favoriteMatrix[3][4] = favoriteMatrix[3][4] + 1
            
          elif float(row[17]) < 0.60 and float(row[17]) > .49:
            favoriteMatrix[4][4] = favoriteMatrix[4][4] + 1
            
          elif float(row[17]) < 0.50 and float(row[17]) > .39:
            favoriteMatrix[5][4] = favoriteMatrix[5][4] + 1
          
          elif float(row[17]) < 0.40 and float(row[17]) > .29:
            favoriteMatrix[6][4] = favoriteMatrix[6][4] + 1
       
            
          
            
  print favoriteMatrix
          
      #away
      #if row[7] > .5:
        
homeFiveThirtyEightProb = {}
homeImpliedProb = {}
homeEdge = {}

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
  
  print "hit2"
  counter = 0
  for item in dict1:
    fiveThirtyProb = dict1[item]
    impliedProb = dict2[item]
    homeEdge[item] = round(float(fiveThirtyProb) - float(impliedProb),2)
  


edgeBins = {} 
def edgeBinner(dict1):
  
  for item in homeEdge:
    print "hit3"
    initialFloor = -.29
    adjuster = 0
    if (homeEdge[item] >= initialFloor + adjuster) and homeEdge[item] < (initialFloor + .02 + adjuster):
      edgeBins[item] = 0
      adjuster = adjuster + .02
      
  for item in homeEdge:
    print "hit4"
    initialFloor = -.29
    if (homeEdge[item] >= initialFloor) and homeEdge[item]< (initialFloor + .02):
      edgeBins[item] = edgeBins[item] + 1
      
                     

def setup():
  #implied()
  countBinner(reader)
  edgeDictionary()
  edgeCalculator(homeFiveThirtyEightProb, homeImpliedProb)
  edgeBinner(homeEdge)

  
setup()
