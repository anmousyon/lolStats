import glob
import os
import pandas as pd
from collections import defaultdict

class player:
	
	def __init__(self, name):
		self.results = []
		self.pmres = []
		self.totalres = []
		self.total = {}
		self.pm = {}
		self.stats = {}
		self.name = name
		self.statsFormat = []
		self.totalFormat = []
		self.pmFormat = []

	def fillFormat(self, f1, f2):
		path = "./metadata/"
		if not os.path.exists(path):
			os.makedirs(path)
		with open((os.path.join(path, f1 + ".txt"))) as pf:
			self.statsFormat = pf.readlines()
		self.statsFormat = [item.strip() for item in self.statsFormat]

		path = "./metadata/"
		if not os.path.exists(path):
			os.makedirs(path)
		with open((os.path.join(path, f2 + ".txt"))) as pf:
			self.pmFormat = pf.readlines()
		self.pmFormat= [item.strip() for item in self.pmFormat]


	def fillStats(self, name, week, day):
		fn = str(name).strip() + "-" + str(week).strip() + "-" + str(day).strip() + ".txt"
		path = "./playerResults/"
		if not os.path.exists(path):
			os.makedirs(path)
		if (os.path.isfile(os.path.join(path, fn))):
			with open((os.path.join(path, fn))) as res:
				lines = res.readlines()
			for data in lines:
				self.results.append(data.strip())

		fn = str(name).strip() + "t.txt"
		path = "./playerStats/"
		if not os.path.exists(path):
			os.makedirs(path)
		if (os.path.isfile(os.path.join(path, fn))):
			with open((os.path.join(path, fn))) as res:
				lines = res.readlines()
			for data in lines:
				self.totalres.append(data.strip())

	def zipper(self):
		self.stats = dict(zip(self.statsFormat, self.results))
		self.total = dict(zip(self.statsFormat, self.totalres))
		self.pm = dict(zip(self.pmFormat, self.pmres))

	def process(self):
		for i in range(5, len(self.results)):
			self.pmres.append(float(self.results[i])/float(self.results[4]))
			self.totalres[i] = float(self.totalres[i]) + float(self.results[i])

	def createSeries(self):
		self.ss = pd.Series(self.results, index = self.statsFormat)
		print(self.ss)
		self.spms = pd.Series(self.pmres, index = self.pmFormat)
		print(self.spms)
		self.sts = pd.Series(self.totalres, index = self.statsFormat)
		print(self.sts)

class team:
	
	def __init__(self, name):
		self.results = []
		self.pmres= []
		self.totalres = []
		self.total = {}
		self.pm = {}
		self.stats = {}
		self.name = name
		self.statsFormat = []
		self.totalFormat = []
		self.pmFormat = []

	def fillFormat(self, formats):
		path = "./metadata/"
		if not os.path.exists(path):
			os.makedirs(path)
		with open((os.path.join(path, formats + '.txt'))) as tf:
			self.statsFormat = tf.readlines()
		self.statsFormat = [item.strip() for item in self.statsFormat]

	def fillStats(self, name, week, day):
		fn = str(name).strip() + "-" + str(week).strip() + "-" + str(day).strip() + ".txt"
		path = "./teamResults/"
		if not os.path.exists(path):
			os.makedirs(path)
		if (os.path.isfile(os.path.join(path, fn))):
			with open((os.path.join(path, fn))) as res:
				lines = res.readlines()
			for data in lines:
				self.results.append(float(data.strip()))

	def zipper(self):
		self.stats = dict(zip(self.statsFormat, self.results))

	def process(self):
		self.ts = pd.Series(self.results, index = self.statsFormat)
		#print(self.ts)

teamNameList = []
teamList = []

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
		p.fillFormat("ps", "ppms")
		p.fillStats(5, 3, 1)
		p.zipper()
		p.process()
		p.createSeries()

	for t in teamList:
		t.fillFormat("ts")
		t.fillStats(1, 3, 1)
		t.zipper()
		t.process()

def main():
	fillTeams()
	fillPlayers()
	fillData()

main()




