import csv
from itertools import islice
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

#this line allows the code to send the heat map data to plotly to be generated.
plotly.tools.set_credentials_file(username = "dataVisualizationTeam", api_key = "LYoJNVINqw9j5m9amQea")

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
        homeBetResult = ((betSize * round(float(homeOdds),2))-100)
        awayBetResult = betSize * -1
        
        row.append(round((homeBetResult),2))
        row.append(round((awayBetResult),2))
      elif winner == awayTeam:
        homeBetResult = betSize * -1
        awayBetResult = ((betSize * round(float(awayOdds),2))-100)
        
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
def binnerHome(localCSV, favoriteMatrix):
  counter = 0
  for row in localCSV:
    fiveThirtyHome = float(row[6])
    impliedProbHome = float(row[17])
    if fiveThirtyHome >= 0.5:
#five thirty eight home prob between .90 and 1 (>.89999 and <1)
      if fiveThirtyHome >= 0.9 and fiveThirtyHome < 1:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteMatrix[6][4] = favoriteMatrix[6][4] + 1

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteMatrix[5][4] = favoriteMatrix[5][4] + 1

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteMatrix[4][4] = favoriteMatrix[4][4] + 1

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteMatrix[3][4] = favoriteMatrix[3][4] + 1

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteMatrix[2][4] = favoriteMatrix[2][4] + 1

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteMatrix[1][4] = favoriteMatrix[1][4] + 1

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteMatrix[0][4] = favoriteMatrix[0][4] + 1

# #five thirty eight home probability between 80 and 89 percent
      if fiveThirtyHome >= 0.8 and fiveThirtyHome < .89999:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteMatrix[6][3] = favoriteMatrix[6][3] + 1

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteMatrix[5][3] = favoriteMatrix[5][3] + 1

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteMatrix[4][3] = favoriteMatrix[4][3] + 1

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteMatrix[3][3] = favoriteMatrix[3][3] + 1

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteMatrix[2][3] = favoriteMatrix[2][3] + 1

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteMatrix[1][3] = favoriteMatrix[1][3] + 1

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteMatrix[0][3] = favoriteMatrix[0][3] + 1

# #five thirty eight home probability between 70 and 79 percent
      if fiveThirtyHome >= 0.7 and fiveThirtyHome < .79999:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteMatrix[6][2] = favoriteMatrix[6][2] + 1

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteMatrix[5][2] = favoriteMatrix[5][2] + 1

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteMatrix[4][2] = favoriteMatrix[4][2] + 1

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteMatrix[3][2] = favoriteMatrix[3][2] + 1

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteMatrix[2][2] = favoriteMatrix[2][2] + 1

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteMatrix[1][2] = favoriteMatrix[1][2] + 1

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteMatrix[0][2] = favoriteMatrix[0][2] + 1

#five thirty eight home probability between 60 and 69 percent
      if fiveThirtyHome >= 0.6 and fiveThirtyHome < .69999:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteMatrix[6][1] = favoriteMatrix[6][1] + 1

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteMatrix[5][1] = favoriteMatrix[5][1] + 1

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteMatrix[4][1] = favoriteMatrix[4][1] + 1

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteMatrix[3][1] = favoriteMatrix[3][1] + 1

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteMatrix[2][1] = favoriteMatrix[2][1] + 1

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteMatrix[1][1] = favoriteMatrix[1][1] + 1

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteMatrix[0][1] = favoriteMatrix[0][1] + 1

#five thirty eight home probability between 50 and 59 percent
      if fiveThirtyHome >= 0.5 and fiveThirtyHome < .59999:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteMatrix[6][0] = favoriteMatrix[6][0] + 1

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteMatrix[5][0] = favoriteMatrix[5][0] + 1

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteMatrix[4][0] = favoriteMatrix[4][0] + 1

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteMatrix[3][0] = favoriteMatrix[3][0] + 1

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteMatrix[2][0] = favoriteMatrix[2][0] + 1

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteMatrix[1][0] = favoriteMatrix[1][0] + 1

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteMatrix[0][0] = favoriteMatrix[0][0] + 1
  print (favoriteMatrix)

def binnerAway(localCSV,awayMatrix):
  counter = 0
  for row in localCSV:
    fiveThirtyAway = float(row[7])
    impliedProbAway = float(row[18])
    if fiveThirtyAway >= 0.5:
#five thirty eight home prob between .90 and 1 (>.89999 and <1)
      if fiveThirtyAway >= 0.9 and fiveThirtyAway < 1:
        if impliedProbAway >= 0.9 and impliedProbAway < 1:
          awayMatrix[6][4] = awayMatrix[6][4] + 1

        elif impliedProbAway >= 0.8 and impliedProbAway < 0.89999:
          awayMatrix[5][4] = awayMatrix[5][4] + 1

        elif impliedProbAway >= 0.7 and impliedProbAway < 0.79999:
          awayMatrix[4][4] = awayMatrix[4][4] + 1

        elif impliedProbAway >= 0.6 and impliedProbAway < 0.69999:
          awayMatrix[3][4] = awayMatrix[3][4] + 1

        elif impliedProbAway >= 0.5 and impliedProbAway < 0.59999:
          awayMatrix[2][4] = awayMatrix[2][4] + 1

        elif impliedProbAway >= 0.4 and impliedProbAway < 0.49999:
          awayMatrix[1][4] = awayMatrix[1][4] + 1

        elif impliedProbAway >= 0.3 and impliedProbAway < 0.39999:
          awayMatrix[0][4] = awayMatrix[0][4] + 1

# #five thirty eight home probability between 80 and 89 percent
      if fiveThirtyAway >= 0.8 and fiveThirtyAway < .89999:
        if impliedProbAway >= 0.9 and impliedProbAway < 1:
          awayMatrix[6][3] = awayMatrix[6][3] + 1

        elif impliedProbAway >= 0.8 and impliedProbAway < 0.89999:
          awayMatrix[5][3] = awayMatrix[5][3] + 1

        elif impliedProbAway >= 0.7 and impliedProbAway < 0.79999:
          awayMatrix[4][3] = awayMatrix[4][3] + 1

        elif impliedProbAway >= 0.6 and impliedProbAway < 0.69999:
          awayMatrix[3][3] = awayMatrix[3][3] + 1

        elif impliedProbAway >= 0.5 and impliedProbAway < 0.59999:
          awayMatrix[2][3] = awayMatrix[2][3] + 1

        elif impliedProbAway >= 0.4 and impliedProbAway < 0.49999:
          awayMatrix[1][3] = awayMatrix[1][3] + 1

        elif impliedProbAway >= 0.3 and impliedProbAway < 0.39999:
          awayMatrix[0][3] = awayMatrix[0][3] + 1

# # #five thirty eight home probability between 70 and 79 percent
      if fiveThirtyAway >= 0.7 and fiveThirtyAway < .79999:
        if impliedProbAway >= 0.9 and impliedProbAway < 1:
          awayMatrix[6][2] = awayMatrix[6][2] + 1

        elif impliedProbAway >= 0.8 and impliedProbAway < 0.89999:
          awayMatrix[5][2] = awayMatrix[5][2] + 1

        elif impliedProbAway >= 0.7 and impliedProbAway < 0.79999:
          awayMatrix[4][2] = awayMatrix[4][2] + 1

        elif impliedProbAway >= 0.6 and impliedProbAway < 0.69999:
          awayMatrix[3][2] = awayMatrix[3][2] + 1

        elif impliedProbAway >= 0.5 and impliedProbAway < 0.59999:
          awayMatrix[2][2] = awayMatrix[2][2] + 1

        elif impliedProbAway >= 0.4 and impliedProbAway < 0.49999:
          awayMatrix[1][2] = awayMatrix[1][2] + 1

        elif impliedProbAway >= 0.3 and impliedProbAway < 0.39999:
          awayMatrix[0][2] = awayMatrix[0][2] + 1

# #five thirty eight home probability between 60 and 69 percent
      if fiveThirtyAway >= 0.6 and fiveThirtyAway < .69999:
        if impliedProbAway >= 0.9 and impliedProbAway < 1:
          awayMatrix[6][1] = awayMatrix[6][1] + 1

        elif impliedProbAway >= 0.8 and impliedProbAway < 0.89999:
          awayMatrix[5][1] = awayMatrix[5][1] + 1

        elif impliedProbAway >= 0.7 and impliedProbAway < 0.79999:
          awayMatrix[4][1] = awayMatrix[4][1] + 1

        elif impliedProbAway >= 0.6 and impliedProbAway < 0.69999:
          awayMatrix[3][1] = awayMatrix[3][1] + 1

        elif impliedProbAway >= 0.5 and impliedProbAway < 0.59999:
          awayMatrix[2][1] = awayMatrix[2][1] + 1

        elif impliedProbAway >= 0.4 and impliedProbAway < 0.49999:
          awayMatrix[1][1] = awayMatrix[1][1] + 1

        elif impliedProbAway >= 0.3 and impliedProbAway < 0.39999:
          awayMatrix[0][1] = awayMatrix[0][1] + 1

# #five thirty eight home probability between 50 and 59 percent
      if fiveThirtyAway >= 0.5 and fiveThirtyAway < .59999:
        if impliedProbAway >= 0.9 and impliedProbAway < 1:
          awayMatrix[6][0] = awayMatrix[6][0] + 1

        elif impliedProbAway >= 0.8 and impliedProbAway < 0.89999:
          awayMatrix[5][0] = awayMatrix[5][0] + 1

        elif impliedProbAway >= 0.7 and impliedProbAway < 0.79999:
          awayMatrix[4][0] = awayMatrix[4][0] + 1

        elif impliedProbAway >= 0.6 and impliedProbAway < 0.69999:
          awayMatrix[3][0] = awayMatrix[3][0] + 1

        elif impliedProbAway >= 0.5 and impliedProbAway < 0.59999:
          awayMatrix[2][0] = awayMatrix[2][0] + 1

        elif impliedProbAway >= 0.4 and impliedProbAway < 0.49999:
          awayMatrix[1][0] = awayMatrix[1][0] + 1

        elif impliedProbAway >= 0.3 and impliedProbAway < 0.39999:
          awayMatrix[0][0] = awayMatrix[0][0] + 1
  print(awayMatrix)

#function takes three arguments, local csv, and the profit matrices defined in the setup funciton
#function returns populated profit matrices
#this function operates similarly to the binner function, however, instead of increasing the count in the correct positon in the matrix
#the function adds the profit or loss of taking that game.
def profitBinnerHome2(localCSV, favoriteProfitMatrix):
  for row in localCSV:
    fiveThirtyHome = float(row[6])
    impliedProbHome = float(row[17])
    homeProfit = float(row[20])
    if fiveThirtyHome >= 0.5:
#five thirty eight home prob between .90 and 1 (>=.90 and <1)
      if fiveThirtyHome >= 0.9 and fiveThirtyHome < 1:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteProfitMatrix[6][4] = favoriteProfitMatrix[6][4] + homeProfit

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteProfitMatrix[5][4] = favoriteProfitMatrix[5][4] + homeProfit

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteProfitMatrix[4][4] = favoriteProfitMatrix[4][4] + homeProfit

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteProfitMatrix[3][4] = favoriteProfitMatrix[3][4] + homeProfit

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteProfitMatrix[2][4] = favoriteProfitMatrix[2][4] + homeProfit

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteProfitMatrix[1][4] = favoriteProfitMatrix[1][4] + homeProfit

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteProfitMatrix[0][4] = favoriteProfitMatrix[0][4] + homeProfit
# #five thirty eight home probability between 80 and 8999 percent
      if fiveThirtyHome >= 0.8 and fiveThirtyHome < .89999:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteProfitMatrix[6][3] = favoriteProfitMatrix[6][3] + homeProfit

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteProfitMatrix[5][3] = favoriteProfitMatrix[5][3] + homeProfit

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteProfitMatrix[4][3] = favoriteProfitMatrix[4][3] + homeProfit

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteProfitMatrix[3][3] = favoriteProfitMatrix[3][3] + homeProfit

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteProfitMatrix[2][3] = favoriteProfitMatrix[2][3] + homeProfit

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteProfitMatrix[1][3] = favoriteProfitMatrix[1][3] + homeProfit

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteProfitMatrix[0][3] = favoriteProfitMatrix[0][3] + homeProfit
# #five thirty eight home probability between 70 and 7999 percent
      if fiveThirtyHome >= 0.7 and fiveThirtyHome < .79999:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteProfitMatrix[6][2] = favoriteProfitMatrix[6][2] + homeProfit

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteProfitMatrix[5][2] = favoriteProfitMatrix[5][2] + homeProfit

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteProfitMatrix[4][2] = favoriteProfitMatrix[4][2] + homeProfit

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteProfitMatrix[3][2] = favoriteProfitMatrix[3][2] + homeProfit

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteProfitMatrix[2][2] = favoriteProfitMatrix[2][2] + homeProfit

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteProfitMatrix[1][2] = favoriteProfitMatrix[1][2] + homeProfit

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteProfitMatrix[0][2] = favoriteProfitMatrix[0][2] + homeProfit
# #five thirty eight home probability between 60 and 6999 percent
      if fiveThirtyHome >= 0.6 and fiveThirtyHome < .69999:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteProfitMatrix[6][1] = favoriteProfitMatrix[6][1] + homeProfit

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteProfitMatrix[5][1] = favoriteProfitMatrix[5][1] + homeProfit

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteProfitMatrix[4][1] = favoriteProfitMatrix[4][1] + homeProfit

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteProfitMatrix[3][1] = favoriteProfitMatrix[3][1] + homeProfit

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteProfitMatrix[2][1] = favoriteProfitMatrix[2][1] + homeProfit

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteProfitMatrix[1][1] = favoriteProfitMatrix[1][1] + homeProfit

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteProfitMatrix[0][1] = favoriteProfitMatrix[0][1] + homeProfit
# #five thirty eight home probability between 50 and 5999 percent
      if fiveThirtyHome >= 0.5 and fiveThirtyHome < .59999:
        if impliedProbHome >= 0.9 and impliedProbHome < 1:
          favoriteProfitMatrix[6][0] = favoriteProfitMatrix[6][0] + homeProfit

        elif impliedProbHome >= 0.8 and impliedProbHome < 0.89999:
          favoriteProfitMatrix[5][0] = favoriteProfitMatrix[5][0] + homeProfit

        elif impliedProbHome >= 0.7 and impliedProbHome < 0.79999:
          favoriteProfitMatrix[4][0] = favoriteProfitMatrix[4][0] + homeProfit

        elif impliedProbHome >= 0.6 and impliedProbHome < 0.69999:
          favoriteProfitMatrix[3][0] = favoriteProfitMatrix[3][0] + homeProfit

        elif impliedProbHome >= 0.5 and impliedProbHome < 0.59999:
          favoriteProfitMatrix[2][0] = favoriteProfitMatrix[2][0] + homeProfit

        elif impliedProbHome >= 0.4 and impliedProbHome < 0.49999:
          favoriteProfitMatrix[1][0] = favoriteProfitMatrix[1][0] + homeProfit

        elif impliedProbHome >= 0.3 and impliedProbHome < 0.39999:
          favoriteProfitMatrix[0][0] = favoriteProfitMatrix[0][0] + homeProfit

  print(favoriteProfitMatrix)
def profitBinnerAway2(localCSV, awayProfitMatrix):
  for row in localCSV:
    fiveThirtyAway = float(row[7])
    impliedProbAway = float(row[18])
    awayProfit = float(row[20])
    if fiveThirtyAway >= 0.5:
#five thirty eight home prob between .90 and 1 (>=.90 and <1)
      if fiveThirtyAway >= 0.9 and fiveThirtyAway < 1:
        if impliedProbAway >= 0.9 and impliedProbAway < 1:
          awayProfitMatrix[6][4] = awayProfitMatrix[6][4] + awayProfit

        elif impliedProbAway >= 0.8 and impliedProbAway < 0.89999:
          awayProfitMatrix[5][4] = awayProfitMatrix[5][4] + awayProfit

        elif impliedProbAway >= 0.7 and impliedProbAway < 0.79999:
          awayProfitMatrix[4][4] = awayProfitMatrix[4][4] + awayProfit

        elif impliedProbAway >= 0.6 and impliedProbAway < 0.69999:
          awayProfitMatrix[3][4] = awayProfitMatrix[3][4] + awayProfit

        elif impliedProbAway >= 0.5 and impliedProbAway < 0.59999:
          awayProfitMatrix[2][4] = awayProfitMatrix[2][4] + awayProfit

        elif impliedProbAway >= 0.4 and impliedProbAway < 0.49999:
          awayProfitMatrix[1][4] = awayProfitMatrix[1][4] + awayProfit

        elif impliedProbAway >= 0.3 and impliedProbAway < 0.39999:
          awayProfitMatrix[0][4] = awayProfitMatrix[0][4] + awayProfit
# #five thirty eight home probability between 80 and 8999 percent
      if fiveThirtyAway >= 0.8 and fiveThirtyAway < .89999:
        if impliedProbAway >= 0.9 and impliedProbAway < 1:
          awayProfitMatrix[6][3] = awayProfitMatrix[6][3] + awayProfit

        elif impliedProbAway >= 0.8 and impliedProbAway < 0.89999:
          awayProfitMatrix[5][3] = awayProfitMatrix[5][3] + awayProfit

        elif impliedProbAway >= 0.7 and impliedProbAway < 0.79999:
          awayProfitMatrix[4][3] = awayProfitMatrix[4][3] + awayProfit

        elif impliedProbAway >= 0.6 and impliedProbAway < 0.69999:
          awayProfitMatrix[3][3] = awayProfitMatrix[3][3] + awayProfit

        elif impliedProbAway >= 0.5 and impliedProbAway < 0.59999:
          awayProfitMatrix[2][3] = awayProfitMatrix[2][3] + awayProfit

        elif impliedProbAway >= 0.4 and impliedProbAway < 0.49999:
          awayProfitMatrix[1][3] = awayProfitMatrix[1][3] + awayProfit

        elif impliedProbAway >= 0.3 and impliedProbAway < 0.39999:
          awayProfitMatrix[0][3] = awayProfitMatrix[0][3] + awayProfit
# #five thirty eight home probability between 70 and 7999 percent
      if fiveThirtyAway >= 0.7 and fiveThirtyAway < .79999:
        if impliedProbAway >= 0.9 and impliedProbAway < 1:
          awayProfitMatrix[6][2] = awayProfitMatrix[6][2] + awayProfit

        elif impliedProbAway >= 0.8 and impliedProbAway < 0.89999:
          awayProfitMatrix[5][2] = awayProfitMatrix[5][2] + awayProfit

        elif impliedProbAway >= 0.7 and impliedProbAway < 0.79999:
          awayProfitMatrix[4][2] = awayProfitMatrix[4][2] + awayProfit

        elif impliedProbAway >= 0.6 and impliedProbAway < 0.69999:
          awayProfitMatrix[3][2] = awayProfitMatrix[3][2] + awayProfit

        elif impliedProbAway >= 0.5 and impliedProbAway < 0.59999:
          awayProfitMatrix[2][2] = awayProfitMatrix[2][2] + awayProfit

        elif impliedProbAway >= 0.4 and impliedProbAway < 0.49999:
          awayProfitMatrix[1][2] = awayProfitMatrix[1][2] + awayProfit

        elif impliedProbAway >= 0.3 and impliedProbAway < 0.39999:
          awayProfitMatrix[0][2] = awayProfitMatrix[0][2] + awayProfit
# #five thirty eight home probability between 60 and 6999 percent
      if fiveThirtyAway >= 0.6 and fiveThirtyAway < .69999:
        if impliedProbAway >= 0.9 and impliedProbAway < 1:
          awayProfitMatrix[6][1] = awayProfitMatrix[6][1] + awayProfit

        elif impliedProbAway >= 0.8 and impliedProbAway < 0.89999:
          awayProfitMatrix[5][1] = awayProfitMatrix[5][1] + awayProfit

        elif impliedProbAway >= 0.7 and impliedProbAway < 0.79999:
          awayProfitMatrix[4][1] = awayProfitMatrix[4][1] + awayProfit

        elif impliedProbAway >= 0.6 and impliedProbAway < 0.69999:
          awayProfitMatrix[3][1] = awayProfitMatrix[3][1] + awayProfit

        elif impliedProbAway >= 0.5 and impliedProbAway < 0.59999:
          awayProfitMatrix[2][1] = awayProfitMatrix[2][1] + awayProfit

        elif impliedProbAway >= 0.4 and impliedProbAway < 0.49999:
          awayProfitMatrix[1][1] = awayProfitMatrix[1][1] + awayProfit

        elif impliedProbAway >= 0.3 and impliedProbAway < 0.39999:
          awayProfitMatrix[0][1] = awayProfitMatrix[0][1] + awayProfit
# #five thirty eight home probability between 50 and 5999 percent
      if fiveThirtyAway >= 0.5 and fiveThirtyAway < .59999:
        if impliedProbAway >= 0.9 and impliedProbAway < 1:
          awayProfitMatrix[6][0] = awayProfitMatrix[6][0] + awayProfit

        elif impliedProbAway >= 0.8 and impliedProbAway < 0.89999:
          awayProfitMatrix[5][0] = awayProfitMatrix[5][0] + awayProfit

        elif impliedProbAway >= 0.7 and impliedProbAway < 0.79999:
          awayProfitMatrix[4][0] = awayProfitMatrix[4][0] + awayProfit

        elif impliedProbAway >= 0.6 and impliedProbAway < 0.69999:
          awayProfitMatrix[3][0] = awayProfitMatrix[3][0] + awayProfit

        elif impliedProbAway >= 0.5 and impliedProbAway < 0.59999:
          awayProfitMatrix[2][0] = awayProfitMatrix[2][0] + awayProfit

        elif impliedProbAway >= 0.4 and impliedProbAway < 0.49999:
          awayProfitMatrix[1][0] = awayProfitMatrix[1][0] + awayProfit

        elif impliedProbAway >= 0.3 and impliedProbAway < 0.39999:
          awayProfitMatrix[0][0] = awayProfitMatrix[0][0] + awayProfit

  print(awayProfitMatrix)

#once the matrices have been populated this function can be called correctly
#this function generates heatmaps using the plotly library
#function takes four arguments, the four matrices defined in the setup function
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

  py.iplot(dataHome, filename = 'HomeCountV3fix')  
  py.iplot(dataAway, filename = 'AwayCountV3fix')  
  py.iplot(dataHomeProf, filename = 'HomeProfitFinal')
  py.iplot(dataAwayProf, filename = 'AwayProfitFinal')  

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
  binnerHome(localCSV, favoriteMatrix)
  binnerAway(localCSV,awayMatrix)
  #checker(awayMatrix)
  profitCalculator(betSize)
  profitBinnerHome2(localCSV,favoriteProfitMatrix)
  profitBinnerAway2(localCSV,awayProfitMatrix)
  #heatMapGenerators(favoriteMatrix, awayMatrix, favoriteProfitMatrix, awayProfitMatrix)
  #print (localCSV)

setup()
