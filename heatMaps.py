import csv
from itertools import islice
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

#this line allows the code to send the heat map data to plotly to be generated.
plotly.tools.set_credentials_file(username = "dataVIZ2", api_key = "4TeEmzMDVNmPdZ9SzzwR")

#these initial files are important for the code in general
file = ("1finaldata.csv")
openFile = open(file, 'r')
reader = csv.reader(openFile)

#creating global variables to be used throughout the code.
#LocalCSV will become a localized copy of the csv data.
#betsize is used as the basis for the profit calculations later
localCSV = []
betSize = 100

#function takes no arguments
#function iterates through the csv data and returns a local copy of the csv data.
def createLocalCSV():
  for row in islice(reader,1,None):
    localCSV.append(row)

#function takes no arguments.
#function appends profit calculations to the local copy of the csv.
#function iterates through the data, calculating the profit based on the odds and outcome of taking either the home or away team

def profitCalculator(betSize):
  for row in localCSV:
      homeTeam = row[2]
      awayTeam = row[3]
      homeOdds = round(float(row[14]),2)
      awayOdds = round(float(row[15]),2)
      winner = row[13]


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

#function is populates the favorite and away matrices defined in the setup function
#function takes localCSV, and the two matrices defined in the setup function as arguments
#function returns a populated favorite matrix and away matrix.
#based on the 538 home probability prediction, the function bins that game with respect to its corresponding implied probability
def binner2(localCSV, favoriteMatrix, awayMatrix):
  counter = 0
  for row in localCSV:
    fiveThirtyHome = float(row[6])
    impliedProbHome = float(row[17])
    if fiveThirtyHome >= 0.5:
#five thirty eight home prob between .90 and 1 (>.89999 and <1)
      if fiveThirtyHome >= 0.9 and fiveThirtyHome < 1:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteMatrix[0][4] = favoriteMatrix[0][4] + 1

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteMatrix[1][4] = favoriteMatrix[1][4] + 1

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteMatrix[2][4] = favoriteMatrix[2][4] + 1

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteMatrix[3][4] = favoriteMatrix[3][4] + 1

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteMatrix[4][4] = favoriteMatrix[4][4] + 1

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteMatrix[5][4] = favoriteMatrix[5][4] + 1

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteMatrix[6][4] = favoriteMatrix[6][4] + 1

# #five thirty eight home probability between 80 and 89 percent
      if fiveThirtyHome >= 0.8 and fiveThirtyHome < .89999:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteMatrix[0][3] = favoriteMatrix[0][3] + 1

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteMatrix[1][3] = favoriteMatrix[1][3] + 1

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteMatrix[2][3] = favoriteMatrix[2][3] + 1

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteMatrix[3][3] = favoriteMatrix[3][3] + 1

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteMatrix[4][3] = favoriteMatrix[4][3] + 1

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteMatrix[5][3] = favoriteMatrix[5][3] + 1

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteMatrix[6][3] = favoriteMatrix[6][3] + 1

# #five thirty eight home probability between 70 and 79 percent
      if fiveThirtyHome >= 0.7 and fiveThirtyHome < .79999:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteMatrix[0][2] = favoriteMatrix[0][2] + 1

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteMatrix[1][2] = favoriteMatrix[1][2] + 1

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteMatrix[2][2] = favoriteMatrix[2][2] + 1

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteMatrix[3][2] = favoriteMatrix[3][2] + 1

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteMatrix[4][2] = favoriteMatrix[4][2] + 1

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteMatrix[5][2] = favoriteMatrix[5][2] + 1

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteMatrix[6][2] = favoriteMatrix[6][2] + 1

#five thirty eight home probability between 60 and 69 percent
      if fiveThirtyHome >= 0.6 and fiveThirtyHome < .69999:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteMatrix[0][1] = favoriteMatrix[0][1] + 1

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteMatrix[1][1] = favoriteMatrix[1][1] + 1

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteMatrix[2][1] = favoriteMatrix[2][1] + 1

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteMatrix[3][1] = favoriteMatrix[3][1] + 1

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteMatrix[4][1] = favoriteMatrix[4][1] + 1

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteMatrix[5][1] = favoriteMatrix[5][1] + 1

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteMatrix[6][1] = favoriteMatrix[6][1] + 1

#five thirty eight home probability between 50 and 59 percent
      if fiveThirtyHome >= 0.5 and fiveThirtyHome < .59999:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteMatrix[0][0] = favoriteMatrix[0][0] + 1

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteMatrix[1][0] = favoriteMatrix[1][0] + 1

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteMatrix[2][0] = favoriteMatrix[2][0] + 1

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteMatrix[3][0] = favoriteMatrix[3][0] + 1

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteMatrix[4][0] = favoriteMatrix[4][0] + 1

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteMatrix[5][0] = favoriteMatrix[5][0] + 1

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteMatrix[6][0] = favoriteMatrix[6][0] + 1
  print(favoriteMatrix)

#function takes three arguments, local csv, and the profit matrices defined in the setup funciton
#function returns populated profit matrices
#this function operates similarly to the binner function, however, instead of increasing the count in the correct positon in the matrix
#the function adds the profit or loss of taking that game.
def profitBinnerHome2(localCSV, favoriteProfitMatrix, awayProfitMatrix):
  for row in localCSV:
    fiveThirtyHome = float(row[6])
    impliedProbHome = float(row[17])
    homeProfit = float(row[20])
    if fiveThirtyHome >= 0.5:
#five thirty eight home prob between .90 and 1 (>=.90 and <1)
      if fiveThirtyHome >= 0.9 and fiveThirtyHome < 1:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteProfitMatrix[0][4] = favoriteProfitMatrix[0][4] + homeProfit

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteProfitMatrix[1][4] = favoriteProfitMatrix[1][4] + homeProfit

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteProfitMatrix[2][4] = favoriteProfitMatrix[2][4] + homeProfit

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteProfitMatrix[3][4] = favoriteProfitMatrix[3][4] + homeProfit

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteProfitMatrix[4][4] = favoriteProfitMatrix[4][4] + homeProfit

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteProfitMatrix[5][4] = favoriteProfitMatrix[5][4] + homeProfit

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteProfitMatrix[6][4] = favoriteProfitMatrix[6][4] + homeProfit
# #five thirty eight home probability between 80 and 8999 percent
      if fiveThirtyHome >= 0.8 and fiveThirtyHome < .89999:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteProfitMatrix[0][3] = favoriteProfitMatrix[0][3] + homeProfit

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteProfitMatrix[1][3] = favoriteProfitMatrix[1][3] + homeProfit

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteProfitMatrix[2][3] = favoriteProfitMatrix[2][3] + homeProfit

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteProfitMatrix[3][3] = favoriteProfitMatrix[3][3] + homeProfit

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteProfitMatrix[4][3] = favoriteProfitMatrix[4][3] + homeProfit

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteProfitMatrix[5][3] = favoriteProfitMatrix[5][3] + homeProfit

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteProfitMatrix[6][3] = favoriteProfitMatrix[6][3] + homeProfit
# #five thirty eight home probability between 70 and 7999 percent
      if fiveThirtyHome >= 0.7 and fiveThirtyHome < .79999:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteProfitMatrix[0][2] = favoriteProfitMatrix[0][2] + homeProfit

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteProfitMatrix[1][2] = favoriteProfitMatrix[1][2] + homeProfit

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteProfitMatrix[2][2] = favoriteProfitMatrix[2][2] + homeProfit

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteProfitMatrix[3][2] = favoriteProfitMatrix[3][2] + homeProfit

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteProfitMatrix[4][2] = favoriteProfitMatrix[4][2] + homeProfit

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteProfitMatrix[5][2] = favoriteProfitMatrix[5][2] + homeProfit

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteProfitMatrix[6][2] = favoriteProfitMatrix[6][2] + homeProfit
# #five thirty eight home probability between 60 and 6999 percent
      if fiveThirtyHome >= 0.6 and fiveThirtyHome < .69999:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteProfitMatrix[0][1] = favoriteProfitMatrix[0][1] + homeProfit

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteProfitMatrix[1][1] = favoriteProfitMatrix[1][1] + homeProfit

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteProfitMatrix[2][1] = favoriteProfitMatrix[2][1] + homeProfit

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteProfitMatrix[3][1] = favoriteProfitMatrix[3][1] + homeProfit

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteProfitMatrix[4][1] = favoriteProfitMatrix[4][1] + homeProfit

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteProfitMatrix[5][1] = favoriteProfitMatrix[5][1] + homeProfit

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteProfitMatrix[6][1] = favoriteProfitMatrix[6][1] + homeProfit
# #five thirty eight home probability between 50 and 5999 percent
      if fiveThirtyHome >= 0.5 and fiveThirtyHome < .59999:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteProfitMatrix[0][0] = favoriteProfitMatrix[0][0] + homeProfit

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteProfitMatrix[1][0] = favoriteProfitMatrix[1][0] + homeProfit

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteProfitMatrix[2][0] = favoriteProfitMatrix[2][0] + homeProfit

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteProfitMatrix[3][0] = favoriteProfitMatrix[3][0] + homeProfit

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteProfitMatrix[4][0] = favoriteProfitMatrix[4][0] + homeProfit

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteProfitMatrix[5][0] = favoriteProfitMatrix[5][0] + homeProfit

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteProfitMatrix[6][0] = favoriteProfitMatrix[6][0] + homeProfit

  print(favoriteProfitMatrix)

#once the matrices have been populated this function can be called correctly
#this function generates heatmaps using the plotly library
#function takes four arguments, the four matrices defined in the setup function
def heatMapGenerators(favoriteMatrix,awayMatrix, favoriteProfitMatrix, awayProfitMatrix):
  traceHome = go.Heatmap(z=favoriteMatrix,
                     x=['.5-.59','.6-.69','.7-.79','.8-.89','.9-.99'],
                     
                     y=['.9-.99','.8-.89','.7-.79','.6-.69','.5-.59','.4-.49','.3-.39']
                    )          
                      
  dataHome = [traceHome]


  # traceAway = go.Heatmap(z=awayMatrix,
  #                  x=['.5-.59','.6-.69','.7-.79','.8-.89','.9-.99'],
  #                  y=['.3-.39','.4-.49','.5-.59','.6-.69','.7-.79','.8-.89','.9-.99']
  #                 )          
                    
  # dataAway = [traceAway]

  traceHomeProf = go.Heatmap(z=favoriteProfitMatrix,
                     x=['.5-.59','.6-.69','.7-.79','.8-.89','.9-.99'],
                     y=['.9-.99','.8-.89','.7-.79','.6-.69','.5-.59','.4-.49','.3-.39']
                    )          
                      
  dataHomeProf = [traceHomeProf]

  # traceAwayProf = go.Heatmap(z=awayProfitMatrix,
  #                    x=['.5-.59','.6-.69','.7-.79','.8-.89','.9-.99'],
  #                    y=['.3-.39','.4-.49','.5-.59','.6-.69','.7-.79','.8-.89','.9-.99']
  #                   )          
                      
  # dataAwayProf = [traceAwayProf]

  py.iplot(dataHome, filename = 'HomeCountV3')  
  #py.iplot(dataAway, filename = 'AwayCountV2')  
  py.iplot(dataHomeProf, filename = 'HomeProfitV2')
  #py.iplot(dataAwayProf, filename = 'AwayProfitV1')  

#this function is a proofing function to keep track of the number of games being added to the matrices
def checker(favoriteMatrix):
  summer = 0
  for row in favoriteMatrix:
    for index in row:
      summer += int(index)
  print ("the number of games in " + str(favoriteMatrix) + " is: " + str(summer))

#setup function takes no arguments
#function is the function that subsequently sets the chain of events in motion for the program.
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
  binner2(localCSV, favoriteMatrix, awayMatrix)
  #checker(favoriteMatrix)
  profitCalculator(betSize)
  profitBinnerHome2(localCSV,favoriteProfitMatrix, awayProfitMatrix)

  heatMapGenerators(favoriteMatrix, awayMatrix, favoriteProfitMatrix, awayProfitMatrix)
  #print (localCSV)

setup()
