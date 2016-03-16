#! python


class player():

	statsRaw = []
	statsPM = []

	def __init__(self, tag):
		self.name = tag
		#stats
	
	def perMinCalc(raw):
		for data in statsPM:
			statsPM = statsRaw/statsRaw[13]

'''	#metadata
	minPlayed = statsRaw[13]
	gamesPlayed = statsRaw[14]
	pos = statsRaw[15]
	team = statsRaw[16]
	
	#gold and gold usage
	gold = statsRaw[0]
	goldPM = statsPM[0]
	wards = statsRaw[1]
	wardsPM = statsPM[1]
	exp = statsRaw[2]
	expPM = statsPM[2]
	cs = statsRaw[3]
	csPM = statsPM[3]
	monst = statsRaw[4]
	monstPM = statsPM[4]

	#combat
	champDmg = statsRaw[5]
	ChampDmgPM = statsPM[5]
	towerDmg = statsRaw[6]
	towerDmgPM = statsPM[6]
	takenDmg = statsRaw[7]
	takenDmgPM = statsPM[7]
	healing = statsRaw[8]
	healingPM = statsPM[8]

	#kills/deaths
	killPart = statsRaw[9]
	killPartPM = statsPM[9]
	kills = statsRaw[10]
	killsPM = statsPM[10]
	deaths = statsRaw[11]
	deathsPM = statsPM[11]
	assists = statsRaw[12]
	assistsPM = statsRaw[12]
	kda = kdaCalc(kills, deaths, assists)
'''
playerList = []
playerNames = []
def fill():
	with open('playerNames.txt') as playerFile:
		playerNames = playerFile.read().splitlines()


	for playerName in playerNames:
		playerList = player(playerName)
