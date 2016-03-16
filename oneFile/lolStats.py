#! python
import glob
import os
from numpy import ndarray

class player:
	pRawFormat = []
	pPMFormat = []

	def __init__(self, name):
		self.pRawStats = []
		self.pPMStats = []
		self.pProcStats = []
		self.pMetadata = []
		self.pTotalStats = []
		self.name = name

	def pFill(self):
		fileName = str(self.name).strip() + "PResults.txt"
		path = "./playerResults/"
		if not os.path.exists(path):
			os.makedirs(path)
		
		if (os.path.isfile(os.path.join(path, fileName))):
			print("opened results")
			with open((os.path.join(path, fileName))) as pResultsFile:
				lines = pResultsFile.readlines()
			for data in lines:
				#print(data)
				self.pRawStats.append(float(data.strip()))
			print(self.pRawStats)

		fileName = str(self.name).strip() + "PTotalStats.txt"
		path = "./playerStats/"

		if not os.path.exists(path):
			os.makedirs(path)

		if (os.path.isfile(os.path.join(path, fileName))):
			print("opened totals")
			print (fileName)
			with open((os.path.join(path, fileName))) as pTotalFile:
				lines = pTotalFile.readlines()
			for data in lines:
				#print(data)
				self.pTotalStats.append(float(data.strip()))
			print(self.pTotalStats)

	def pProcData(self):
		if(self.pRawStats):
			for i in range(5, 13):
				self.pPMStats.append(float(self.pRawStats[i])/float(self.pRawStats[4]))
			self.pMetadata.append(self.pRawStats[0])
			self.pMetadata.append(self.pRawStats[1])
			self.pMetadata.append(self.pRawStats[2])
		
			for data in self.pRawStats:
				self.pProcStats.append(data)
	
			for data in self.pPMStats:
				self.pProcStats.append(data)
			for i in range(0, 3):
				self.pTotalStats[i] = self.pRawStats[i]
			for i in range(3, len(self.pRawStats)):
				self.pTotalStats[i] += self.pRawStats[i]

	def kPart(self, k, team):
		return k/int(team.tRawStats[3])
	
	def kda(self, k, d, a):
		return (k+a)/(d)

class team:
	tRawFormat = []

	def __init__(self, name):
		self.tRawStats = []
		self.tProcStats = []
		self.tRawStats.append(name)

	def pPMCalc(self):
		for data in tRawStats:
			self.tProcStats = self.tRawStats/self.tRawStats[13]
	
	def tFill(self):
		fileName = self.tRawStats[0].strip() + "TResults.txt"
		path = "./teamResults/"

		if not os.path.exists(path):
			os.makedirs(path)
		
		if (os.path.isfile(os.path.join(path, fileName))):
			with open((os.path.join(path, fileName))) as tResultsFile:
				self.tRawStats = tResultsFile.readlines()

teamNameList = []
teamList = []

def fillFormats():
	path = "./metadata/"

	if not os.path.exists(path):
		os.makedirs(path)

	with open((os.path.join(path, 'pRawStats.txt'))) as pFormat:
		player.pRawFormat = pFormat.readlines()
	
	path = "./metadata/"
	
	with open((os.path.join(path,'tRawStats.txt'))) as tFormat:
		player.tRawFormat = tFormat.readlines()
	
	path = "./metadata/"

	with open((os.path.join(path, 'pPMStats.txt'))) as pFormat:
		player.pPMFormat = pFormat.readlines()

def fillTeams():
	path = "./metadata/"

	if not os.path.exists(path):
		os.makedirs(path)

	with open((os.path.join(path, 'teams.txt'))) as teamNames:
		teamNameList = teamNames.readlines()
	for teamName in teamNameList:
		newTeam = team(teamName)
		teamList.append(newTeam)

playerNameList = []
playerList = []

def fillPlayers():
	path = "./metadata/"
	
	if not os.path.exists(path):
		os.makdirs(path)

	with open((os.path.join(path, 'players.txt'))) as playerNames:
		playerNameList = playerNames.readlines()
	for playerName in playerNameList:
		newPlayer = player(playerName)
		playerList.append(newPlayer)

def fillData():
	for p in playerList:
		p.pFill()

	for t in teamList:
		t.tFill()
	
	for p in playerList:
		p.pProcData()

def writeData():
	path = "./playerStats/"
	
	if not os.path.exists(path):
	    os.makedirs(path)

	for p in playerList:
		if(p.pRawStats):
			fileName = (str(int(p.pRawStats[0]))) + "PRawStats.txt"
			f = open((os.path.join(path, fileName)), 'w')
			for data in p.pRawStats:
				f.write(str(data)+"\n")
			f.close()
		if(p.pPMStats):
			fileName = (str(int(p.pRawStats[0]))) + "PPMStats.txt"
			f = open((os.path.join(path, fileName)), 'w')
			for data in p.pPMStats:
				f.write(str(data)+"\n")
			f.close()
		if(p.pTotalStats):
			fileName = (str(int(p.pRawStats[0]))) + "PTotalStats.txt"
			f = open((os.path.join(path, fileName)), 'w')
			for data in p.pTotalStats:
				f.write(str(data)+"\n")
			f.close()
		
	path = "./teamStats/"

	if not os.path.exists(path):
		os.makedirs(path)

	for t in teamList:
		if(t.tRawStats):
			fileName = (t.tRawStats[0]).strip() + "TStats.txt"
			f = open((os.path.join(path, fileName)), 'w')
			for data in t.tRawStats:
				f.write(data + "\n")
			f.close()

def printData():
	if(playerList):
		for p in playerList:
			if(p.pRawStats):
				print((p.pRawStats[0]))
				for i in range(len(p.pRawStats)):
					print(player.pRawFormat[i].strip() + " " + str(p.pRawStats[i]))
			if(p.pPMStats):
				for i in range(len(p.pPMStats)):
					print(player.pPMFormat[i].strip() + " " + str(p.pPMStats[i]))
	if(teamList):
		for t in teamList:
			for i in range(len(t.tRawStats)):
				print(player.tRawFormat[i].strip() + " " + str(t.tRawStats[i]))

def main():
	fillFormats()
	fillPlayers()
	fillTeams()
	fillData()
	writeData()
	printData()


main()
