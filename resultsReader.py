#! python

import player
import team
import glob

teamResults = []

def readData():
	
	for filename in glob.glob('c9Results.txt'):
		with open(filename) as teamResultsFile:
			teamResults = teamResultsFile.readlines()

winner = ''
loser = ''
def findTeams():
	for teamName in team.teamList:
		if teamName is teamResults[0]:
			winner = teamName;

def fillData(teamName):
	for result in teamResults:
		team.teamName.teamStats = result

def printData(teamName):
	f = open('c9StatsPM.txt', 'w')
	for data in team.teamName.statsPM:
		f.write(statsPM + "\n")
	f.close()

def doResults():
	readData()
	findTeams()
	fillData(winner)
	fillData(loser)
