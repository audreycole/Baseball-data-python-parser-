import re

s = raw_input("Please enter a sentence")

#find hello world in a sentence
r1 = re.search("hello world", s)
#if r1 != None:
	#print r1.group()


#Find all words in an input string that contain a triple vowel
r2 = re.findall(r"([\w]*[aeiou]{3}[\w]*)", s)
#if r2 != None:
	#print r2

#Match an input string that is entirely a flight code, of the format AA####, where AA is a two-letter uppercase airline code, and #### is a three- or four-digit flight number
r3 = re.search(r"([A-Z]{2}[\d]{3,4})", s)
if r3 != None:
	print r3.group()