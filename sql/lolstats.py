#!/usr/bin/python

import pymysql
import glob
import os

db = pymysql.connect(host="localhost", user="root", passwd="'a;s]q[w", db="lolstats")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("db version: %s" % data)

playerNamesList = []

def fillNames():
	fn = "players.txt"
	path = "./"
	if not os.path.exists(path):
		os.makedirs(path)
	if (os.path.isfile(os.path.join(path, fn))):
		with open((os.path.join(path, fn))) as res:
			lines = res.readlines()
		for data in lines:
			playerNamesList.append(data.strip())

fillNames()

cursor.execute('CREATE TABLE \
IF NOT EXISTS players \
(name TEXT, pos TEXT, team TEXT, games INTEGER, \
min FLOAT, gold INTEGER, wards INTEGER, exp INTEGER, \
cs INTEGER, monst INTEGER, champDMG FLOAT, towerDMG FLOAT, \
takenDMG FLOAT, healing FLOAT, kills INTEGER, \
deaths INTEGER, assists INTEGER)')

for playerName in playerNamesList:
	cursor.execute('INSERT INTO players (name) \
	SELECT (%s) \
	WHERE NOT EXISTS\
	(SELECT * FROM players WHERE name=(%s))', \
	(playerName, playerName))

db.commit()

print('players: ')

cursor.execute('SELECT name FROM players')

for row in cursor:
	print(row)

db.close()