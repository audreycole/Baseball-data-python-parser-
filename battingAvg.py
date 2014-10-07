import re
import math
import sys, os
from collections import OrderedDict

# If the input is < 2 (you haven't input a file) then print the "Usage message" 
if len(sys.argv) < 2:
	sys.exit("Usage: %s filename" % sys.argv[0])

# Filename is the second thing that you input into python--> it's in the format "python battingAvg.py filename.txt"
filename = sys.argv[1]

# If you haven't specified a file-path to reach filename (or it isn't stored locally with battingAvg.py) print "Error message" 
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % sys.argv[1])

# Open the file for reading
f = open(filename)

# Players class we'll use to help keep track of a player's batting average 
class Player:
	def __init__(self, name):
		self.name = name
		self.bats = 0
		self.hits = 0

	def addBats(self, bats):
		self.bats += bats

	def getBats(self):
		return self.bats

	def addHits(self, hits):
		self.hits += hits

	def getHits(self):
		return self.hits

	def getBattingAvg(self):
		if int(self.hits != 0):
			return round(float(self.hits) /float(self.bats), 3)
		else:
			return 0

# Create a "players" dictionary to store players and averages and a "result" one we'll use for sorting/printing
players = {}
result = {}

line_count = 0
# Loop through each line in the file 
for line in f:

	line_count += 1
	
	# Use regex to find names in the format "Firstname Lastname " within a given line 
	name = ""
	name_regex = re.compile(r"(?P<name>(\b[A-Z]([\w])* \b){2})")
	m = name_regex.match(line)
	if m != None:
		name = m.group('name')

	# Make a list containing the numbers that we seek 
	numbers_list = re.findall(r'[\d]+', line) 

	# Check to see if the name is already in the dictionary "players"
	if name in players:
		p = players[name]
		num_count = 0
		# Add players bats and hits 
		if line[0]!= "=":
			for n in numbers_list:
				num_count += 1
				if num_count == 1:
					#print "bats are " + n
					p.addBats(int(float(n)))
				if num_count == 2:
					#print "hits are " + n
					p.addHits(int(float(n)))
		# Add in an entry to the results dictionary that we'll actually sort and print 			
		result[name] = p.getBattingAvg()
	else :
	# Create a new Player since it's not already in the dictionary "players"
		# Make sure name isn't set to "" as its default 
		if name != "":
			p = Player(name)

			num_count = 0
			# Add players bats and hits 
			if line[0]!= "=":
				for n in numbers_list:
					num_count += 1
					if num_count == 1:
						#print "bats are " + n
						p.addBats(int(float(n)))
					if num_count == 2:
						#print "hits are " + n
						p.addHits(int(float(n)))
			# Add to players the "name" as the key and the "Player object" as the value 
			players[name] = p
# Create a new sorted dictionary that uses the result dictionary and sorts it by the keys in reverse 
d_sorted_by_value = OrderedDict(sorted(result.items(), key=lambda x: x[1], reverse = True))
# Loop through the dictionary and print the player's names and batting averages 
for k, v in d_sorted_by_value.items():
    print "%s: %s" % (k, v)

f.close()