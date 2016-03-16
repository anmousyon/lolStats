import player
import team
import glob

playerStats = []

def readData():
	for fileName in glob.glob('*Stats.txt'):
		with open(fileName) as playerStatsFile:
			playerStats = playerStatsFile.readlines()

pname = ''

def findPlayers():
	for PLAYER in player.playerList:
		if player.playerList.name is player.name:
			pname = PLAYER

def fillData(tag):
	for stat in playerStats:
		player.tag.statsRaw = stat

def doStats():
	readData()
	findPlayers()
	fillData(pname)
