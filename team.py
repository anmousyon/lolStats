#! python

class team():
	
	teamStats = []

	def __init__(self, abv):
		self.name = abv
		#main array
		self.teamStats = []

	#players
	players = []
'''
	#game results
	win = teamStats[0]
	loss = teamStats[1]
	wlRatio = teamStats[2]
	gameLength = teamStats[3]
	
	#Kills
	firstKillTime = teamStats[4]
	firstKill = teamStats[5]
	kills = teamStats[6]

	#Deaths
	firstDeathTime = teamStats[7]
	firstDeath = teamStats[8]
	deaths = teamStats[9]
	
	#Assists
	firstAssistTime = teamStats[9]
	firstAssist = teamStats[10]
	assists = teamStats[11]

	#Tower
	firstTowerTime = teamStats[12]
	firstTower = teamStats[13]
	towers = teamStats[14]
	
	#Inhibitor
	firstInhibTime = teamStats[15]
	firstInhib = teamStats[16]
	inhibs = teamStats[17]

	#Dragon
	firstDragonTime = teamStats[18]
	firstDragon = teamStats[19]
	dragons = teamStats[20]

	#Baron
	firstBaronTime = teamStats[21]
	firstBaron = teamStats[22]
	barons = teamStats[23]

	#Scuttle
	firstScuttleTime = teamStats[24]
	firstScuttle = teamStats[25]
	scuttles = teamStats[26]
'''
teamList = []

def fill():
	
	with open('teamNames.txt') as teamFile:
		teamList = teamFile.read().splitlines()
	
	for x in range(10):
		newTeam = team(x)
		print(x)
		teamList.append(newTeam)
