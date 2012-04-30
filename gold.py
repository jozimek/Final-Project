#!/usr/bin/env python

import getpass, fileinput, os
from sys import stdin, stdout, stderr, exit

global gold

gold = 0

def room1():
	global gold
	print 'You are in room number 1, where you started the game. You currently have',gold,'gold. There is a table in this room with a vase sitting on top. There are two doors one to the north and one to the west. To go to the room to the north type n, to go to the west type w, to examine the table type l.'
	prompt_room1()


def prompt_room1():
	global gold
	prompt = raw_input("Type a command: ")
	try:
		if prompt == "w":
			room4()
		elif prompt == "n":
			room2()
		elif prompt == "l":
			print "You see 20 coins on the table. You picked them up and now have them."
			gold = gold + 20
			prompt_room1()
		else:
			print "That command was not valid"
			prompt_room1()			
	except ValueError:
		print "That command was not valid"
		print
		prompt_room1()


def room2():
	global gold
	print 'You are in room number 2'
	print 'You currently have',gold,'gold. There is a table in this room with a vase sitting on top. There are two doors one to the south and one to the west. To go to the room to the south type s, to go to the west type w, to examine the table type l.'
	prompt_room2()


def prompt_room2():
	global gold
	prompt = raw_input("Type a command: ")
	try:
		if prompt == "w":
			room3()
		elif prompt == "s":
			room1()
		elif prompt == "l":
			print "You see 20 coins on the table. You picked them up and now have them."
			gold = gold + 20
			prompt_room2()
		else:
			print "That command was not valid"
			prompt_room2()
	except ValueError:
		print "That command was not valid"
		print
		prompt_room2()


def room3():
	global gold
	print "You are in room number 3"
	print 'You currently have',gold,'gold.There is a table in this room with a vase sitting on top. There are two doors one to the south and one to the east. To go to the room to the south type s, to go to the east type e, to examine the table type l.'
	prompt_room3()

def prompt_room3():
	global gold
	prompt = raw_input("Type a command: ")
	try:
		if prompt == "e":
			room2()
		elif prompt == "s":
			room4()
		elif prompt == "l":
			print "You see 20 coins on the table. You picked them up and now have them."
			gold = gold + 20
			prompt_room3()
		else:
			print "That command was not valid"
			prompt_room3()
	except ValueError:
		print "That command was not valid"
		print
		prompt_room3()

def room4():
	global gold
	print "You are in room number 4"
	print 'You currently have',gold,'gold.There is a table in this room with a vase sitting on top. There are two doors one to the north and one to the east. To go to the room to the north type n, to go to the east type e, to examine the table type l.'
	prompt_room4()

def prompt_room4():
	global gold
	prompt = raw_input("Type a command: ")
	try:
		if prompt == "e":
			room1()
		elif prompt == "n":
			room3()
		elif prompt == "l":
			print "You see 20 coins on the table. You picked them up and now have them."
			gold = gold + 20
			prompt_room4()
		else:
			print "That command was not valid"
			prompt_room4()
	except ValueError:
		print "That command was not valid"
		print
		prompt_room4()

room1()
