import csv
from itertools import islice
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username = "dataVisualizationTeam", api_key = "rjGVnSpfjvSwkrGU7nXd")

file = ("1finaldata.csv")
print (file)
openFile = open(file, 'r')
reader = csv.reader(openFile)

localCSV = []
betSize = 100

def createLocalCSV():
  for row in islice(reader,1,None):
    localCSV.append(row)

def profitCalculator(betSize):

  for row in localCSV:
      homeTeam = row[2]
      # homeTeam = str(homeTeam).upper()
      awayTeam = row[3]
      # awayTeam = str(awayTeam).upper()
      homeOdds = round(float(row[14]),2)
      awayOdds = round(float(row[15]),2)
      winner = row[13]
      # winner = str(winner).upper()

      if winner == homeTeam:
        homeBetResult = betSize * round(float(homeOdds),2)
        awayBetResult = betSize * -1
        
        row.append(round((homeBetResult),2))
        row.append(round((awayBetResult),2))
      elif winner == awayTeam:
        homeBetResult = betSize * -1
        awayBetResult = betSize * round(float(awayOdds),2)
        
        row.append(round((homeBetResult),2))
        row.append(round((awayBetResult),2))
      else:
        homeBetResult = betSize * -1
        awayBetResult = betSize * -1
        row.append(round(homeBetResult,2))
        row.append(round(awayBetResult,2))


def binner(reader, favoriteMatrix, awayMatrix):
  counterHome = 0
  counter = 0
  gamesHome = 0
  for row in localCSV:
      #homes greater with a 538 prediction > .5
      if float(row[6]) >= 0.5:
        counterHome = counterHome + 1
        gamesHome += 1
        # counterHome += 1
        print ("rows counted: " + str(counterHome))
        if float(row[6]) >= .5 and float(row[6]) <= .59:
          print ("rows counted second level: " + str(counterHome))
          
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
            
        
        if float(row[6]) >= .6 and float(row[6]) <= .69:
          print ("rows counted third level: " + str(counterHome))
          
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
        
        if float(row[6]) >= .70 and float(row[6]) <= 0.79:
          print ("rows counted fourth level: " + str(counterHome))
          
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
            
        if float(row[6]) >=.80 and float(row[6]) <= .89:
          print ("rows counted fifth level: " + str(counterHome))
          
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
            
        if float(row[6]) >= .90 and float(row[6]) <= 1:
          print ("rows counted sixth level: " + str(counterHome))
          
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
  print (gamesHome)
  for row in localCSV:
      #aways greater with a 538 prediction > .5
      if float(row[7]) > 0.5:
        counter = counter + 1
        print ("away rows counted: " + str(counter))
        if float(row[7]) >= .5 and float(row[7]) <= .59:
          print ("away rows counted second level: " + str(counter))
          
          #less than 1 so .99 and greater than .89 so .90
          if float(row[18]) < 1 and float(row[18]) > 0.89:
            awayMatrix[0][0] = awayMatrix[0][0] + 1
            
          #less than .90 so .89 and greater than .79 so .80
          elif float(row[18]) < 0.90 and float(row[18]) > .79:
            awayMatrix[1][0] = awayMatrix[1][0] + 1
            
          elif float(row[18]) < 0.80 and float(row[18]) > .69:
            awayMatrix[2][0] = awayMatrix[2][0] + 1
            
          elif float(row[18]) < 0.70 and float(row[18]) > .59:
            awayMatrix[3][0] = awayMatrix[3][0] + 1
            
          elif float(row[18]) < 0.60 and float(row[18]) > .49:
            awayMatrix[4][0] = awayMatrix[4][0] + 1
            
          elif float(row[18]) < 0.50 and float(row[18]) > .39:
            awayMatrix[5][0] = awayMatrix[5][0] + 1
          
          elif float(row[18]) < 0.40 and float(row[18]) > .29:
            awayMatrix[6][0] = awayMatrix[6][0] + 1
              
        if float(row[7]) >= .6 and float(row[7]) <= .69:
          print ("away rows counted third level: " + str(counter))
          
          #less than 1 so .99 and greater than .89 so .90
          if float(row[18]) < 1 and float(row[18]) > 0.89:
            awayMatrix[0][1] = awayMatrix[0][1] + 1
            
          #less than .90 so .89 and greater than .79 so .80
          elif float(row[18]) < 0.90 and float(row[18]) > .79:
            awayMatrix[1][1] = awayMatrix[1][1] + 1
            
          elif float(row[18]) < 0.80 and float(row[18]) > .69:
            awayMatrix[2][1] = awayMatrix[2][1] + 1
            
          elif float(row[18]) < 0.70 and float(row[18]) > .59:
            awayMatrix[3][1] = awayMatrix[3][1] + 1
            
          elif float(row[18]) < 0.60 and float(row[18]) > .49:
            awayMatrix[4][1] = awayMatrix[4][1] + 1
            
          elif float(row[18]) < 0.50 and float(row[18]) > .39:
            awayMatrix[5][1] = awayMatrix[5][1] + 1
          
          elif float(row[18]) < 0.40 and float(row[18]) > .29:
            awayMatrix[6][1] = awayMatrix[6][1] + 1
        
        if float(row[7]) >= .7 and float(row[7]) <= .79:
          print ("away rows counted fourth level: " + str(counter))
          
          #less than 1 so .99 and greater than .89 so .90
          if float(row[18]) < 1 and float(row[18]) > 0.89:
            awayMatrix[0][2] = awayMatrix[0][2] + 1
            
          #less than .90 so .89 and greater than .79 so .80
          elif float(row[18]) < 0.90 and float(row[18]) > .79:
            awayMatrix[1][2] = awayMatrix[1][2] + 1
            
          elif float(row[18]) < 0.80 and float(row[18]) > .69:
            awayMatrix[2][2] = awayMatrix[2][2] + 1
            
          elif float(row[18]) < 0.70 and float(row[18]) > .59:
            awayMatrix[3][2] = awayMatrix[3][2] + 1
            
          elif float(row[18]) < 0.60 and float(row[18]) > .49:
            awayMatrix[4][2] = awayMatrix[4][2] + 1
            
          elif float(row[18]) < 0.50 and float(row[18]) > .39:
            awayMatrix[5][2] = awayMatrix[5][2] + 1
          
          elif float(row[18]) < 0.40 and float(row[18]) > .29:
            awayMatrix[6][2] = awayMatrix[6][2] + 1
            
        if float(row[7]) >= .8 and float(row[7]) <= .89:
          print ("away rows counted fifth level: " + str(counter))
          
          #less than 1 so .99 and greater than .89 so .90
          if float(row[18]) < 1 and float(row[18]) > 0.89:
            awayMatrix[0][3] = awayMatrix[0][3] + 1
            
          #less than .90 so .89 and greater than .79 so .80
          elif float(row[18]) < 0.90 and float(row[18]) > .79:
            awayMatrix[1][3] = awayMatrix[1][3] + 1
            
          elif float(row[18]) < 0.80 and float(row[18]) > .69:
            awayMatrix[2][3] = awayMatrix[2][3] + 1
            
          elif float(row[18]) < 0.70 and float(row[18]) > .59:
            awayMatrix[3][3] = awayMatrix[3][3] + 1
            
          elif float(row[18]) < 0.60 and float(row[18]) > .49:
            awayMatrix[4][3] = awayMatrix[4][3] + 1
            
          elif float(row[18]) < 0.50 and float(row[18]) > .39:
            awayMatrix[5][3] = awayMatrix[5][3] + 1
          
          elif float(row[18]) < 0.40 and float(row[18]) > .29:
            awayMatrix[6][3] = awayMatrix[6][3] + 1
            
        if float(row[7]) >= .9 and float(row[7]) <= 1:
          print ("away rows counted sixth level: " + str(counter))
          
          #less than 1 so .99 and greater than .89 so .90
          if float(row[18]) < 1 and float(row[18]) > 0.89:
            awayMatrix[0][4] = awayMatrix[0][4] + 1
            
          #less than .90 so .89 and greater than .79 so .80
          elif float(row[18]) < 0.90 and float(row[18]) > .79:
            awayMatrix[1][4] = awayMatrix[1][4] + 1
            
          elif float(row[18]) < 0.80 and float(row[18]) > .69:
            awayMatrix[2][4] = awayMatrix[2][4] + 1
            
          elif float(row[18]) < 0.70 and float(row[18]) > .59:
            awayMatrix[3][4] = awayMatrix[3][4] + 1
            
          elif float(row[18]) < 0.60 and float(row[18]) > .49:
            awayMatrix[4][4] = awayMatrix[4][4] + 1
            
          elif float(row[18]) < 0.50 and float(row[18]) > .39:
            awayMatrix[5][4] = awayMatrix[5][4] + 1
          
          elif float(row[18]) < 0.40 and float(row[18]) > .29:
            awayMatrix[6][4] = awayMatrix[6][4] + 1
       
  print(awayMatrix)
  print (favoriteMatrix)

def profitBinner(reader, favoriteProfitMatrix, awayProfitMatrix):
  counterHome = 0
  counter = 0
  for row in localCSV:
      #homes greater with a 538 prediction > .5
    if float(row[6]) > 0.5:
      print (favoriteProfitMatrix)
      counterHome = counterHome + 1
      print ("rows counted: " + str(counterHome))
      if float(row[6]) > .5 and float(row[6]) < .6:
        print ("rows counted second level: " + str(counterHome))
        
        #less than 1 so .99 and greater than .89 so .90
        if float(row[17]) < 1 and float(row[17]) > 0.89:
          favoriteProfitMatrix[0][0] = favoriteProfitMatrix[0][0] + round(row[21],2)
          
        #less than .90 so .89 and greater than .79 so .80
        elif float(row[17]) < 0.90 and float(row[17]) > .79:
          favoriteProfitMatrix[1][0] = favoriteProfitMatrix[1][0] + round(row[21],2)
          
        elif float(row[17]) < 0.80 and float(row[17]) > .69:
          favoriteProfitMatrix[2][0] = favoriteProfitMatrix[2][0] + round(row[21],2)
          
        elif float(row[17]) < 0.70 and float(row[17]) > .59:
          favoriteProfitMatrix[3][0] = favoriteProfitMatrix[3][0] + round(row[21],2)
          
        elif float(row[17]) < 0.60 and float(row[17]) > .49:
          favoriteProfitMatrix[4][0] = favoriteProfitMatrix[4][0] + round(row[21],2)
          
        elif float(row[17]) < 0.50 and float(row[17]) > .39:
          favoriteProfitMatrix[5][0] = favoriteProfitMatrix[5][0] + round(row[21],2)
        
        elif float(row[17]) < 0.40 and float(row[17]) > .29:
          favoriteProfitMatrix[6][0] = favoriteProfitMatrix[6][0] + round(row[21],2)
          
      
      if float(row[6]) > .59 and float(row[6]) < .7:
        print ("rows counted third level: " + str(counterHome))
        
        #less than 1 so .99 and greater than .89 so .90
        if float(row[17]) < 1 and float(row[17]) > 0.89:
          favoriteProfitMatrix[0][1] = favoriteProfitMatrix[0][1] + round(row[21],2)
          
        #less than .90 so .89 and greater than .79 so .80
        elif float(row[17]) < 0.90 and float(row[17]) > .79:
          favoriteProfitMatrix[1][1] = favoriteProfitMatrix[1][1] + round(row[21],2)
          
        elif float(row[17]) < 0.80 and float(row[17]) > .69:
          favoriteProfitMatrix[2][1] = favoriteProfitMatrix[2][1] + round(row[21],2)
          
        elif float(row[17]) < 0.70 and float(row[17]) > .59:
          favoriteProfitMatrix[3][1] = favoriteProfitMatrix[3][1] + round(row[21],2)
          
        elif float(row[17]) < 0.60 and float(row[17]) > .49:
          favoriteProfitMatrix[4][1] = favoriteProfitMatrix[4][1] + round(row[21],2)
          
        elif float(row[17]) < 0.50 and float(row[17]) > .39:
          favoriteProfitMatrix[5][1] = favoriteProfitMatrix[5][1] + round(row[21],2)
        
        elif float(row[17]) < 0.40 and float(row[17]) > .29:
          favoriteProfitMatrix[6][1] = favoriteProfitMatrix[6][1] + round(row[21],2)
      
      if float(row[6]) > .69 and float(row[6]) < .8:
        print ("rows counted fourth level: " + str(counterHome))
        
        #less than 1 so .99 and greater than .89 so .90
        if float(row[17]) < 1 and float(row[17]) > 0.89:
          favoriteProfitMatrix[0][2] = favoriteProfitMatrix[0][2] + round(row[21],2)
          
        #less than .90 so .89 and greater than .79 so .80
        elif float(row[17]) < 0.90 and float(row[17]) > .79:
          favoriteProfitMatrix[1][2] = favoriteProfitMatrix[1][2] + round(row[21],2)
          
        elif float(row[17]) < 0.80 and float(row[17]) > .69:
          favoriteProfitMatrix[2][2] = favoriteProfitMatrix[2][2] + round(row[21],2)
          
        elif float(row[17]) < 0.70 and float(row[17]) > .59:
          favoriteProfitMatrix[3][2] = favoriteProfitMatrix[3][2] + round(row[21],2)
          
        elif float(row[17]) < 0.60 and float(row[17]) > .49:
          favoriteProfitMatrix[4][2] = favoriteProfitMatrix[4][2] + round(row[21],2)
          
        elif float(row[17]) < 0.50 and float(row[17]) > .39:
          favoriteProfitMatrix[5][2] = favoriteProfitMatrix[5][2] + round(row[21],2)
        
        elif float(row[17]) < 0.40 and float(row[17]) > .29:
          favoriteProfitMatrix[6][2] = favoriteProfitMatrix[6][2] + round(row[21],2)
          
      if float(row[6]) > .79 and float(row[6]) < .9:
        print ("rows counted fifth level: " + str(counterHome))
        
        #less than 1 so .99 and greater than .89 so .90
        if float(row[17]) < 1 and float(row[17]) > 0.89:
          favoriteProfitMatrix[0][3] = favoriteProfitMatrix[0][3] + round(row[21],2)
          
        #less than .90 so .89 and greater than .79 so .80
        elif float(row[17]) < 0.90 and float(row[17]) > .79:
          favoriteProfitMatrix[1][3] = favoriteProfitMatrix[1][3] + round(row[21],2)
          
        elif float(row[17]) < 0.80 and float(row[17]) > .69:
          favoriteProfitMatrix[2][3] = favoriteProfitMatrix[2][3] + round(row[21],2)
          
        elif float(row[17]) < 0.70 and float(row[17]) > .59:
          favoriteProfitMatrix[3][3] = favoriteProfitMatrix[3][3] + round(row[21],2)
          
        elif float(row[17]) < 0.60 and float(row[17]) > .49:
          favoriteProfitMatrix[4][3] = favoriteProfitMatrix[4][3] + round(row[21],2)
          
        elif float(row[17]) < 0.50 and float(row[17]) > .39:
          favoriteProfitMatrix[5][3] = favoriteProfitMatrix[5][3] + round(row[21],2)
        
        elif float(row[17]) < 0.40 and float(row[17]) > .29:
          favoriteProfitMatrix[6][3] = favoriteProfitMatrix[6][3] + round(row[21],2)
          
      if float(row[6]) > .89 and float(row[6]) < 1:
        print ("rows counted sixth level: " + str(counterHome))
        
        #less than 1 so .99 and greater than .89 so .90
        if float(row[17]) < 1 and float(row[17]) > 0.89:
          favoriteProfitMatrix[0][4] = favoriteProfitMatrix[0][4] + round(row[21],2)
          
        #less than .90 so .89 and greater than .79 so .80
        elif float(row[17]) < 0.90 and float(row[17]) > .79:
          favoriteProfitMatrix[1][4] = favoriteProfitMatrix[1][4] + round(row[21],2)
          
        elif float(row[17]) < 0.80 and float(row[17]) > .69:
          favoriteProfitMatrix[2][4] = favoriteProfitMatrix[2][4] + round(row[21],2)
          
        elif float(row[17]) < 0.70 and float(row[17]) > .59:
          favoriteProfitMatrix[3][4] = favoriteProfitMatrix[3][4] + round(row[21],2)
          
        elif float(row[17]) < 0.60 and float(row[17]) > .49:
          favoriteProfitMatrix[4][4] = favoriteProfitMatrix[4][4] + round(row[21],2)
          
        elif float(row[17]) < 0.50 and float(row[17]) > .39:
          favoriteProfitMatrix[5][4] = favoriteProfitMatrix[5][4] + round(row[21],2)
        
        elif float(row[17]) < 0.40 and float(row[17]) > .29:
          favoriteProfitMatrix[6][4] = favoriteProfitMatrix[6][4] + round(row[21],2)

  for row in localCSV:
    #aways greater with a 538 prediction > .5
    if float(row[7]) > 0.5:
      counter = counter + 1
      print ("away rows counted: " + str(counter))
      if float(row[7]) >= .5 and float(row[7]) <= .59:
        print ("away rows counted second level: " + str(counter))
        
        #less than 1 so .99 and greater than .89 so .90
        if float(row[18]) < 1 and float(row[18]) > 0.89:
          awayProfitMatrix[0][0] = awayProfitMatrix[0][0] + round(row[21],2)
          
        #less than .90 so .89 and greater than .79 so .80
        elif float(row[18]) < 0.90 and float(row[18]) > .79:
          awayProfitMatrix[1][0] = awayProfitMatrix[1][0] + round(row[21],2)
          
        elif float(row[18]) < 0.80 and float(row[18]) > .69:
          awayProfitMatrix[2][0] = awayProfitMatrix[2][0] + round(row[21],2)
          
        elif float(row[18]) < 0.70 and float(row[18]) > .59:
          awayProfitMatrix[3][0] = awayProfitMatrix[3][0] + round(row[21],2)
          
        elif float(row[18]) < 0.60 and float(row[18]) > .49:
          awayProfitMatrix[4][0] = awayProfitMatrix[4][0] + round(row[21],2)
          
        elif float(row[18]) < 0.50 and float(row[18]) > .39:
          awayProfitMatrix[5][0] = awayProfitMatrix[5][0] + round(row[21],2)
        
        elif float(row[18]) < 0.40 and float(row[18]) > .29:
          awayProfitMatrix[6][0] = awayProfitMatrix[6][0] + round(row[21],2)
            
      if float(row[7]) >= .6 and float(row[7]) <= .69:
        print ("away rows counted third level: " + str(counter))
        
        #less than 1 so .99 and greater than .89 so .90
        if float(row[18]) < 1 and float(row[18]) > 0.89:
          awayProfitMatrix[0][1] = awayProfitMatrix[0][1] + round(row[21],2)
          
        #less than .90 so .89 and greater than .79 so .80
        elif float(row[18]) < 0.90 and float(row[18]) > .79:
          awayProfitMatrix[1][1] = awayProfitMatrix[1][1] + round(row[21],2)
          
        elif float(row[18]) < 0.80 and float(row[18]) > .69:
          awayProfitMatrix[2][1] = awayProfitMatrix[2][1] + round(row[21],2)
          
        elif float(row[18]) < 0.70 and float(row[18]) > .59:
          awayProfitMatrix[3][1] = awayProfitMatrix[3][1] + round(row[21],2)
          
        elif float(row[18]) < 0.60 and float(row[18]) > .49:
          awayProfitMatrix[4][1] = awayProfitMatrix[4][1] + round(row[21],2)
          
        elif float(row[18]) < 0.50 and float(row[18]) > .39:
          awayProfitMatrix[5][1] = awayProfitMatrix[5][1] + round(row[21],2)
        
        elif float(row[18]) < 0.40 and float(row[18]) > .29:
          awayProfitMatrix[6][1] = awayProfitMatrix[6][1] + round(row[21],2)
      
      if float(row[7]) >= .7 and float(row[7]) <= .79:
        print ("away rows counted fourth level: " + str(counter))
        
        #less than 1 so .99 and greater than .89 so .90
        if float(row[18]) < 1 and float(row[18]) > 0.89:
          awayProfitMatrix[0][2] = awayProfitMatrix[0][2] + round(row[21],2)
          
        #less than .90 so .89 and greater than .79 so .80
        elif float(row[18]) < 0.90 and float(row[18]) > .79:
          awayProfitMatrix[1][2] = awayProfitMatrix[1][2] + round(row[21],2)
          
        elif float(row[18]) < 0.80 and float(row[18]) > .69:
          awayProfitMatrix[2][2] = awayProfitMatrix[2][2] + round(row[21],2)
          
        elif float(row[18]) < 0.70 and float(row[18]) > .59:
          awayProfitMatrix[3][2] = awayProfitMatrix[3][2] + round(row[21],2)
          
        elif float(row[18]) < 0.60 and float(row[18]) > .49:
          awayProfitMatrix[4][2] = awayProfitMatrix[4][2] + round(row[21],2)
          
        elif float(row[18]) < 0.50 and float(row[18]) > .39:
          awayProfitMatrix[5][2] = awayProfitMatrix[5][2] + round(row[21],2)
        
        elif float(row[18]) < 0.40 and float(row[18]) > .29:
          awayProfitMatrix[6][2] = awayProfitMatrix[6][2] + round(row[21],2)
          
      if float(row[7]) >= .8 and float(row[7]) <= .89:
        print ("away rows counted fifth level: " + str(counter))
        
        #less than 1 so .99 and greater than .89 so .90
        if float(row[18]) < 1 and float(row[18]) > 0.89:
          awayProfitMatrix[0][3] = awayProfitMatrix[0][3] + round(row[21],2)
          
        #less than .90 so .89 and greater than .79 so .80
        elif float(row[18]) < 0.90 and float(row[18]) > .79:
          awayProfitMatrix[1][3] = awayProfitMatrix[1][3] + round(row[21],2)
          
        elif float(row[18]) < 0.80 and float(row[18]) > .69:
          awayProfitMatrix[2][3] = awayProfitMatrix[2][3] + round(row[21],2)
          
        elif float(row[18]) < 0.70 and float(row[18]) > .59:
          awayProfitMatrix[3][3] = awayProfitMatrix[3][3] + round(row[21],2)
          
        elif float(row[18]) < 0.60 and float(row[18]) > .49:
          awayProfitMatrix[4][3] = awayProfitMatrix[4][3] + round(row[21],2)
          
        elif float(row[18]) < 0.50 and float(row[18]) > .39:
          awayProfitMatrix[5][3] = awayProfitMatrix[5][3] + round(row[21],2)
        
        elif float(row[18]) < 0.40 and float(row[18]) > .29:
          awayProfitMatrix[6][3] = awayProfitMatrix[6][3] + round(row[21],2)
          
      if float(row[7]) >= .9 and float(row[7]) <= 1:
        print ("away rows counted sixth level: " + str(counter))
        
        #less than 1 so .99 and greater than .89 so .90
        if float(row[18]) < 1 and float(row[18]) > 0.89:
          awayProfitMatrix[0][4] = awayProfitMatrix[0][4] + round(row[21],2)
          
        #less than .90 so .89 and greater than .79 so .80
        elif float(row[18]) < 0.90 and float(row[18]) > .79:
          awayProfitMatrix[1][4] = awayProfitMatrix[1][4] + round(row[21],2)
          
        elif float(row[18]) < 0.80 and float(row[18]) > .69:
          awayProfitMatrix[2][4] = awayProfitMatrix[2][4] + round(row[21],2)
          
        elif float(row[18]) < 0.70 and float(row[18]) > .59:
          awayProfitMatrix[3][4] = awayProfitMatrix[3][4] + round(row[21],2)
          
        elif float(row[18]) < 0.60 and float(row[18]) > .49:
          awayProfitMatrix[4][4] = awayProfitMatrix[4][4] + round(row[21],2)
          
        elif float(row[18]) < 0.50 and float(row[18]) > .39:
          awayProfitMatrix[5][4] = awayProfitMatrix[5][4] + round(row[21],2)
        
        elif float(row[18]) < 0.40 and float(row[18]) > .29:
          awayProfitMatrix[6][4] = awayProfitMatrix[6][4] + round(row[21],2)
       
  print(awayProfitMatrix)
  print(favoriteProfitMatrix)
      #away
      #if row[7] > .5:
        
homeFiveThirtyEightProb = {}
homeImpliedProb = {}
homeEdge = {}

def edgeDictionary():
  print ("hit")
  counter = 0
  for row in islice(reader, 1, None):
    uniqueKey = row[0]
    homeFiveProb = row[6]
    homeImpliedProbability = row[17]
    homeFiveThirtyEightProb[uniqueKey] = homeFiveProb
    homeImpliedProb[uniqueKey] = homeImpliedProbability


    
    
    
    
def edgeCalculator(dict1, dict2):
  
  print ("hit2")
  counter = 0
  for item in dict1:
    fiveThirtyProb = dict1[item]
    impliedProb = dict2[item]
    homeEdge[item] = round(float(fiveThirtyProb) - float(impliedProb),2)
  


edgeBins = {} 
def edgeBinner(dict1):
  
  for item in homeEdge:
    print ("hit3")
    initialFloor = -.29
    adjuster = 0
    if (homeEdge[item] >= initialFloor + adjuster) and homeEdge[item] < (initialFloor + .02 + adjuster):
      edgeBins[item] = 0
      adjuster = adjuster + .02
      
  for item in homeEdge:
    print ("hit4")
    initialFloor = -.29
    if (homeEdge[item] >= initialFloor) and homeEdge[item]< (initialFloor + .02):
      edgeBins[item] = edgeBins[item] + 1
      
def heatMapGenerators(favoriteMatrix,awayMatrix, favoriteProfitMatrix, awayProfitMatrix):
  traceHome = go.Heatmap(z=favoriteMatrix,
                     x=['.5-.59','.6-.69','.7-.79','.8-.89','.9-.99'],
                     y=['.3-.39','.4-.49','.5-.59','.6-.69','.7-.79','.8-.89','.9-.99']
                    )          
                      
  dataHome = [traceHome]


  traceAway = go.Heatmap(z=awayMatrix,
                   x=['.5-.59','.6-.69','.7-.79','.8-.89','.9-.99'],
                   y=['.3-.39','.4-.49','.5-.59','.6-.69','.7-.79','.8-.89','.9-.99']
                  )          
                    
  dataAway = [traceAway]

  traceHomeProf = go.Heatmap(z=favoriteProfitMatrix,
                     x=['.5-.59','.6-.69','.7-.79','.8-.89','.9-.99'],
                     y=['.3-.39','.4-.49','.5-.59','.6-.69','.7-.79','.8-.89','.9-.99']
                    )          
                      
  dataHomeProf = [traceHomeProf]

  traceAwayProf = go.Heatmap(z=awayProfitMatrix,
                     x=['.5-.59','.6-.69','.7-.79','.8-.89','.9-.99'],
                     y=['.3-.39','.4-.49','.5-.59','.6-.69','.7-.79','.8-.89','.9-.99']
                    )          
                      
  dataAwayProf = [traceAwayProf]

  py.iplot(dataHome, filename = 'HomeCountV2')  
  py.iplot(dataAway, filename = 'AwayCountV2')  
  py.iplot(dataHomeProf, filename = 'HomeProfitV1')
  py.iplot(dataAwayProf, filename = 'AwayProfitV1')  

def checker(favoriteMatrix):
  summer = 0
  for row in favoriteMatrix:
    for index in row:
      summer += int(index)
  print ("the number of games in favoriteMatrix is: " + str(summer))

def setup():
  favoriteMatrix = [[0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0],
                  [0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0]]

  awayMatrix = [[0,0,0,0,0], 
              [0,0,0,0,0], 
              [0,0,0,0,0], 
              [0,0,0,0,0], 
              [0,0,0,0,0], 
              [0,0,0,0,0], 
              [0,0,0,0,0]]

  favoriteProfitMatrix = [[0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0],
                  [0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0]]

  awayProfitMatrix = [[0,0,0,0,0], 
              [0,0,0,0,0], 
              [0,0,0,0,0], 
              [0,0,0,0,0], 
              [0,0,0,0,0], 
              [0,0,0,0,0], 
              [0,0,0,0,0]]

  createLocalCSV()
  binner(reader, favoriteMatrix, awayMatrix)
  checker(favoriteMatrix)
  profitCalculator(betSize)
  profitBinner(reader,favoriteProfitMatrix, awayProfitMatrix)
  #edgeDictionary()
  #edgeCalculator(homeFiveThirtyEightProb, homeImpliedProb)
  #edgeBinner(homeEdge)
  heatMapGenerators(favoriteMatrix, awayMatrix, favoriteProfitMatrix, awayProfitMatrix)
  #print (localCSV)

setup()
