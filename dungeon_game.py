from sys import exit
from os.path import exists
from random import *

hina_alive = True # gold hungry bounty hunter
snow_alive = True # white haired bounty hunter
scarecrow_alive = True # male bounty hunter
skeletons_alive = True # passive skeletons in room 5
stone_golem_alive = True # room 1, falls on your head almost
fire_golem_alive = True # room 3, just chilling there
eventA_occured = False # meet Hina for the first time. At an intersection
monkey_present = True # monkey's in room 4
secret_discovered = False # secret being the room off of room 9
gold_of_secret_room_taken = False # secret room off of room 9 that has gold
room7_gold_taken = False # gold from the room with one lever
room8_gold_taken = False # gold from the room with the treasure chest
ninjas_alive = True # from room 12
dwarf_alive = True # from room 6
miyu_alive = True # also from room 10
miyu_with_you = False
eventB_occured = False # meet Snow and Scarecrow in a hallway
rouge_alive = True
room17_gold_taken = False
room17_healing_used = False
room16_button_discovered = False
boss_alive = True

door1_closed = True
door2_closed = True
door3_closed = True
door4_closed = True

player_health = 50

def dead():
	global player_health
	if player_health <= 0:
		print "You're health has been reduced to zero!" 
		print "Game over."
		exit(0)

def gold(situation, amount):
	global hina_alive
	print situation
	if hina_alive:
		hina_encounter()
	else:
		print "Do you want to take the gold?"
		next = raw_input("> ")
		if "yes" in next:
			print "You gain %d gold." % amount
		else:
			print "Don't worry its safe. You take it anyway and gain %d gold." % amount

def hina_encounter():
	global hina_alive
	global player_health
	global door1_closed
	global door2_closed
	global door4_closed
	global room17_healing_used
	
	print "Suddenly you hear footsteps approaching rapidly."
	print "That bounty hunter, Hina, appears and starts raking the gold into her pockets."
	print "What do you do?"
		
	next = raw_input("> ")
		
	if "take" in next and "gold" in next:
		print "You try to grab the gold, but Hina is too quick and takes all of it."
		print "She runs before you can say anything to her."
	elif "stop" in next and ("Hina" in next or "her" in next):
		print "You are unable to stop Hina and she takes all the gold and leaves before \nyou can talk."
	elif "kill" in next and ("Hina" in next or "her" in next):
		print "You attempt to assassinate Hina with your sword but she deftly deflects \nthe blow."
		print "Taking the rest of the gold, she quickly runs out of the room."
	elif "attack" in next and ("Hina" in next or "her" in next):
		print "She dodges your attack and continues to collect gold."
		print "After taking all of it, she runs away before you can talk to her."
	elif "pull" in next and "top left" in next:
		print "You pull the lever and spears shoot out of the ground in the top half \nof the room."
		print "As you were standing by that lever, the spears deal 10 damage to you."
		player_health -= 10
		print "Meanwhile, Hina takes the rest of the gold and leaves without talking to you."
	elif "pull" in next and "top right" in next and not room17_healing_used:
		print "You pull the lever and water pours out of the ceiling, briefly covering the \nfloor before vanishing."
		print "The water heals you completely."
		room17_healing_used = True
		print "Meanwhile, Hina takes the rest of the gold and leaves without talking to you."
	elif "pull" in next and "top right" in next and room17_healing_used:
		print "You pull the lever, but nothing happens."
		print "Meanwhile, Hina takes the rest of the gold and leaves without talking to you."
	elif "pull" in next and "right top" in next:
		print "A giant spear shoots out of the wall and impales Hina."
		hina_alive = False
		print "She dies instantly."
		gold("Now that Hina is gone, the gold is yours.", 2000)
	elif "pull" in next and "right bottom" in next and door1_closed:
		print "You pull the lever and hear what sounds like a mechanism turning."
		print "Nothing in the room changes though."
		door1_closed = False
		door2_closed = False
		door4_closed = False
		print "Meanwhile, Hina takes the rest of the gold and leaves without talking to you."
	elif "pull" in next and "right bottom" in next and door1_closed:
		print "You pull the lever, but nothing happens."
		print "Meanwhile, Hina takes the rest of the gold and leaves without talking to you."
	elif "pull" in next and "bottom left" in next:
		print "You pull the lever, but nothing happens."
		print "Meanwhile, Hina takes the rest of the gold and leaves without talking to you."
	elif "pull" in next and "bottom right" in next:
		print "You pull the lever and an explosion goes off in the north-west corner of \nthe room."
		print "There was no apparent cause and it left no damage."
		print "Meanwhile, Hina takes the rest of the gold and leaves without talking to you."
	elif "west" in next or "go back" in next or "leave" in next:
		print "Meanwhile, Hina takes the rest of the gold and leaves without talking to you."
		print "You follow her out of the room, travelling 10 feet the east and arrive in \nanother room."
		room15()
	else:
		print "Hina takes all of the gold and leaves without saying a word to you."

def room1():
	global stone_golem_alive
	global player_health
	if stone_golem_alive:
		print "As you enter the room, a giant stone golem falls from the ceiling, \nnearly missing you."
		print "What do you do?"
		golem_health = 20
		golem_attacking = False
		while stone_golem_alive:
			next = raw_input("> ")
			if "flee" in next or "run" in next or "escape" in next or "go past" in next:
				print "You may not run away from a fight or you will die."
			elif ("attack" in next or "slice" in next or ("swing" in next and "sword" in next)) and not golem_attacking:
				print "The golem takes 10 damage from your attack."
				golem_health -= 10
				if golem_health == 0:
					stone_golem_alive = False
					print "The attack kills the golem."
				else:
					print "He staggers back before moving to attack you."
					golem_attacking = True
			elif ("attack" in next or "slice" in next or ("swing" in next and "sword" in next)) and golem_attacking:
				print "The golem takes 10 damage from your attack, but you also take 5 damage from \nits attack."
				golem_health -= 10
				player_health -= 5
				dead()
				if golem_health == 0:
					stone_golem_alive = False
					print "The attack still killed the golem though."
				else:
					print "Both you and the golem move back from each other."
					golem_attacking = False
			elif ("dodge" in next or "jump back" in next) and golem_attacking:
				print "The golem's swipe at you misses."
				golem_attacking = False
			elif ("dodge" in next or "jump back" in next) and not golem_attacking:
				print "You move back a little. The golem starts running at you."
				golem_attacking = True
			else:
				print "The golem takes the opportunity to attack you and deals 5 damage."
				player_health -= 5
				dead()
				golem_attacking = False

		print "The golem is now a pile of rocks and dust."
		
	else:
		print "You arrive in a room that has a pile of rocks and dust."
		
	print "This room has exits to the east, west, and south."
	print "Where do you want to go?"
	
	while True:
		next = raw_input("> ")
		if next == "east":
			print "You travel 5 feet east, turn north, and travel 10 more feet before \nreaching another room."
			room3()
		elif next == "west":
			print "You travel 5 feet west, turn north, and travel 10 more feet before \nreaching another room."
			room2()
		elif next == "south":
			print "Really, you want to leave? Request denied."
		else:
			print "I don't know what you want to do... input something else please."

def room2():
	print "This room is empty."
	print "There are exits to the east and south."
	print "What do you want to do?"
	while True:
		next = raw_input("> ")
		if "east" in next:
			print "You travel 5 feet east before reaching an intersection."
			eventA()
		elif "south" in next:
			print "You travel 10 feet south, turn east, and travel 5 more feet before \nreaching a room."
			room1()
		elif "search" in next or "look around" in next:
			print "You search reveals nothing more about the room."
		else:
			print "I don't know what you want to do... input something else please."

def room3():
	global fire_golem_alive
	global player_health
	if fire_golem_alive:
		print "In this room, you find a fire golem."
		print "What do you do?"
		golem_health = 20
		golem_attacking = False
		while fire_golem_alive:
			next = raw_input("> ")
			if "flee" in next or "run" in next or "escape" in next or "go past" in next:
				print "You may not run away from a fight or you will die."
			elif ("attack" in next or "slice" in next or ("swing" in next and "sword" in next)) and not golem_attacking:
				print "The golem takes 10 damage from your attack."
				golem_health -= 10
				if golem_health == 0:
					fire_golem_alive = False
					print "The attack kills the golem."
				else:
					print "He staggers back before moving to attack you."
					golem_attacking = True
			elif ("attack" in next or "slice" in next or ("swing" in next and "sword" in next)) and golem_attacking:
				print "The golem takes 10 damage from your attack, but you also take 5 damage \nfrom its attack."
				golem_health -= 10
				player_health -= 5
				dead()
				if golem_health == 0:
					fire_golem_alive = False
					print "The attack still killed the golem though."
				else:
					print "Both you and the golem move back from each other."
					golem_attacking = False
			elif ("dodge" in next or "jump back" in next) and golem_attacking:
				print "The golem's swipe at you misses."
				golem_attacking = False
			elif ("dodge" in next or "jump back" in next) and not golem_attacking:
				print "You move back a little. The golem starts running at you."
				golem_attacking = True
			else:
				print "The golem takes the opportunity to throw a fireball at you. You take 5 \nfire damage."
				player_health -= 5
				dead()
				golem_attacking = False

		print "The golem is now a large pile of ash."
		
	else:
		print "You arrive in a room that has a large pile of ash."
		
	print "This room has exits to the west and south."
	print "Where do you want to go?"
	
	while True:
		next = raw_input("> ")
		if "west" in next:
			print "You travel 5 feet east before reaching an intersection."
			eventA()
		elif "south" in next:
			print "You travel 10 feet south, turn west, and travel 5 more feet before \nreaching a room."
			room1()
		elif "search" in next or "look around" in next:
			print "You search reveals nothing more about the room."
		else:
			print "I don't know what you want to do... input something else please."

def eventA():
	global eventA_occured
	if not eventA_occured:
		print "At this intersection, you find a woman."
		print "She is dressed in all black and has brown hair."
		print "She is ignoring you. Do you want to talk to her or avoid her?"
		next = raw_input("> ")
		if "talk" in next:
			print "She looks at you irritatedly."
			print '''Hina: "I'm Hina. I'm a bounty hunter looking for Black Wing. \n\tYou are clearly not Black Wing so stay out of my way."'''
			print "She runs up the north passage and disappears."
		elif "attack" in next or "kill" in next:
			print "She immediately reacts to your attack, parrying it easily."
			print '''Woman: "How rude."'''
			print "She runs up the north passage and disappears without saying another word."
		else:
			print "The woman runs up the north passage and disappears without saying another word."
		eventA_occured = True
		
	print "From this intersection, you can go north, east, or west."
	print "Where do you want to go?"
	
	while True:
			next = raw_input("> ")
			if "north" in next:
				print "You travel 10 feet north before reaching a room."
				room4()
			elif "east" in next:
				print "You travel 5 feet east before reaching a room."
				room3()
			elif "west" in next:
				print "You travel 5 feet west before reaching a room."
				room2()
			else:
				print "I don't know what you want to do... input something else please."

def room4():
	global monkey_present
	global player_health
	global eventB_occured
	if monkey_present: # monkey is still here
		print "In this room, you see a small monkey in a corner."
		print "What do you want to do?"	
		monkey_evaded = False
		
		while monkey_present:
			next = raw_input("> ")
			if ("catch" in next or "capture" in next or "approach" in next or "pick up" in next or "move toward" in next) and monkey_evaded:
				print "Again, the monkey avoids you. This time, however, it then runs down the \npassage leading to the west."
				monkey_present = False
			elif ("catch" in next or "capture" in next or "approach" in next or "pick up" in next or "move toward" in next) and not monkey_evaded:
				print "The monkey skirts away from you."
				monkey_evaded = True
			elif "attack" in next or "kill" in next or "slice" in next:
				print "The monkey narrowly avoids you attack and screeches at you."
				print "It then runs down the a passage leading to the west."
				monkey_present = False
			elif "ignore" in next or "west" in next or "north" in next or "south" in next or "east" in next:
				print "The monkey sneaks up and bites your hand before running back to its corner. \nYou take 1 damage."
				player_health -= 1
				dead()
			else:
				print "Nothing happens."

		print "The room is now empty. There are exits in all four directions."
		print "Where do you want to go?"

	else: # monkey is gone
		print "You arrive in an empty room."
		print "There are exits in all four directions."
		print "Where do you want to go?"
	
	while True:
		next = raw_input("> ")
		if "east" in next:
			print "You travel 20 feet east before reaching a room."
			room6()
		elif "south" in next:
			print "You travel 10 feet south before reaching an intersection."
			eventA()
		elif "west" in next:
			print "You travel 20 feet west and reach another room."
			room5()
		elif "chase" in next:
			print "Following the monkey, you travel 20 feet west before reaching another room."
			print "The monkey is nowhere to be found."
			room5()
		elif "north" in next:
			if eventB_occured:
				print "You travel 50 feet north, passing two bodies in the hallway before \nreaching another room."
				room13()
			else:
				eventB()
		elif "search" in next or "look around" in next:
			print "You search reveals nothing more about the room."
		else:
			print "I don't know what you want to do... input something else please."

def room5():
	global snow_alive
	global skeletons_alive
	global player_health
	global snow_alive
	if skeletons_alive and snow_alive:
		print "You find another woman fighting three skeleton soldiers in this room."
		print "This woman is clothed in red and has white hair."
		print "What do you want to do?"
		next = raw_input("> ")
		if ("assist" in next or "help" in next) and ("her" in next or "girl" in next or "woman" in next):
			print "Together, you and the woman fight the skeletons and easily reduce them to \npiles of bones."
			skeletons_alive = False
			print "Right after the fight, though, the woman turns on you and holds you at \nsword point."
			print "She looks at you for a bit and then speaks."
			print '''Woman: "For helping me this time, I will not kill you. But if we meet again, \n\texpect no such generosity."'''
			print '''Woman: "You would be wise not to cross paths with me again."'''
			print "She then walks out through the east exit."
			print "All that's left in this room are three piles of bones."
		elif ("kill" in next or "attack" in next) and ("her" in next or "girl" in next or "woman" in next):
			print "You stab the woman in the back, killing her."
			snow_alive = False
			print "The skeletons pause and look at you."
			print "They move back to the center of the room and appear to be on guard."
			print "They do not seem to be willing to attack you."
			print "What do you want to do?"
			skeleton_fight()
		else:
			print "You do nothing."
			print "The woman fights off the three skeletons with a little difficulty, but \nmanages to win unscathed."
			skeletons_alive = False
			print "She then turns to you, looking ready to fight."
			print "What do you do?"
			snow_fight()
			
	elif skeletons_alive and not snow_alive:
		print "You find 3 skeleton soldiers in this room."
		print "They do not seem to have any interest in attacking you. In fact, they are \nsimply staring straight ahead."
		print "What do you want to do?"
		skeleton_fight()

	else:
		print "In this room, you find three piles of bones."
	
	print "There are exits in all four directions."
	print "Where do you want to go?"
	while True:
		next = raw_input("> ")
		if "east" in next:
			print "You travel 20 feet east before reaching a room."
			room4()
		elif "south" in next:
			print "You travel 5 feet south before reaching a room."
			room11()
		elif "west" in next:
			print "You travel 5 feet west and reach another room."
			room9()
		elif "north" in next:
			print "You travel 5 feet and reach a room."
			room7()
		elif "search" in next or "look around" in next:
			print "You search reveals nothing more about the room."
		else:
			print "I don't know what you want to do... input something else please."

def snow_fight():
	global player_health
	global snow_alive
	snow_attacking = False
	snow_attacked_once = False
	snow_health = 40
	first_turn = True
	while snow_alive:
		next = raw_input("> ")
		if "talk" in next and first_turn:
			print "You ask her who she is."
			print '''Snow: "I am Snow, a bounty hunter looking for Black Wing. \n\tAnd you're getting in my way."'''
			print "She moves to slash at you with her sword."
			snow_attacking = True
			first_turn = False
		elif "talk" in next and snow_attacking:
			print "As you try to speak, she hits you with her sword, dealing 5 damage."
			player_health -= 5
			dead()
		elif "talk" in next and not first_turn:
			print '''Snow: "I'm not talking to you about anything!"'''
			print "She starts to swing at you."
			snow_attacking = True
		elif ("dodge" in next or "jump back" in next) and snow_attacking and snow_attacked_once:
			print "You dodge the attack."
			snow_attacking = False
			snow_attacked_once = False
		elif ("dodge" in next or "jump back" in next) and snow_attacking and not snow_attacked_once:
			print "You jump away, but Snow comes after you."
			snow_attacking = True
			snow_attacked_once = True
		elif ("dodge" in next or "jump back" in next) and not snow_attacking and snow_attacked_once:
			first_turn = False
			print "You back away a bit. Snow starts moving in towards you."
			snow_attacking = True
			snow_attacked_once = False
		elif ("dodge" in next or "jump back" in next) and not snow_attacking and not snow_attacked_once:
			first_turn = False
			print "You jump back. Snow starts moving in towards you."
			snow_attacking = True
			snow_attacked_once = True
		elif ("attack" in next or "swing" in next or "slice" in next or "kill" in next) and not snow_attacking:
			print "You attack Snow, dealing 10 damage."
			snow_health -= 10
			first_turn = False
			if snow_health == 0:
				print "Your last attack killed Snow. But with her dying breath, she speaks."
				print '''Snow: "You'll never make it out of here alive."'''
				print "Then she dies.\n"
				snow_alive = False
			else:
				print "She then starts to swing at you again."
				snow_attacking = True
				snow_attacked_once = False
		elif ("attack" in next or "swing" in next or "slice" in next or "kill" in next) and snow_attacking:
			print "Both of your attacks, hit, your attack dealing 10 damage, hers dealing 5."
			snow_health -= 10
			player_health -= 5
			dead()
			first_turn = False
			if snow_health == 0:
				print "Your last attack still killed Snow. But with her dying breath, she speaks."
				print '''Snow: "You'll never make it out of here alive."'''
				print "Then she dies.\n"
				snow_alive = False
			else:
				print "She then starts to swing at you again."
				snow_attacking = True
				snow_attacked_once = False
		else:
			print "Snow takes the opportunity to attack you, dealing 5 damage."
			player_health -= 5
			dead()
			snow_attacking = False
			snow_attacked_once = False

def skeleton_fight():
	global player_health
	global skeletons_alive
	next = raw_input("> ")
	if "behind" in next and ("attack" in next or "kill" in next):
		print "You get behind the skeleton soldiers and swiftly cut them to pieces."
		print "The skeletons fall apart into three piles of bones."
		skeletons_alive = False
	elif "attack" in next or "kill" in next:
		print "You move to attack the skeletons. Working together though, they deflect \nyour attack and each take a swing at you."
		print "Each of there attacks deal 5 damage, but you are not deterred."
		player_health -= 15
		dead()
		print "Angered by their attack, you rip into the skeletons, tearing them apart with \nyour sword and fist."
		print "You reduce the skeletons to three piles of bones."
		skeletons_alive = False
	elif "ignore" in next or "avoid" in next or ("leave" in next and "alone" in next):
		print "The skeletons will also leave you alone."
	elif "talk" in next:
		print "You try to talk to the skeletons but they do not respond."
	else:
		print "You and the skeletons reach a mutual understanding to do nothing."

def room7():
	global room7_gold_taken
	print "You arrive in an empty room. The only thing of interest is a lever on the \nnorth wall."
	print "The only exit is the one you came from, to the south."
	print "What do you do?"
	while True:
		next = raw_input("> ")
		if not room7_gold_taken and "pull" in next and "lever" in next:
			gold("Parts of the east and west walls open up and gold starts spilling out of them.", 500)
			room7_gold_taken = True
			print "Now the gold is gone. What do you want to do?"
		elif room7_gold_taken and "pull" in next and "lever" in next:
			print "You pull the lever but nothing happens."
		elif "south" in next or "leave" in next or "go back" in next:
			print "You leave the room and travel 5 feet south before reaching a room."
			room5()
		elif "search" in next or "look around" in next:
			print "You find nothing of interest in this room other than the lever."
		else:
			print "I don't know what you want to do... input something else."

def room9():
	global secret_discovered
	print "This room is empty."
	if secret_discovered:
		print "There are exits to the west and east."
	else:
		print "There is an exit to the east."
	
	print "What do you want to do?"
	
	while True:
		next = raw_input("> ")
		if "east" in next or "leave" in next or "go back" in next:
			print "You travel 5 feet east before reaching a room."
			room5()
		elif ("search" in next or "look around" in next) and not secret_discovered:
			print "You discover a secret doorway in the west wall."
			secret_discovered = True
		elif ("search" in next or "look around" in next) and secret_discovered:
			print "You find nothing else of interest in this room."
		elif ("west" in next or "through" in next) and secret_discovered:
			print "You go through the secret door and travel 5 feet west, arriving in a new room."
			secret_room()
		else:
			print "I don't know what you want to do... input something else please."

def room11():
	global scarecrow_alive
	if scarecrow_alive:
		print "In this room, you find a man. He turns to you and asks who you are."
		print "You tell him your name and say you are simply exploring the dungeon."
		print "You ask him who he is."
		print '''Scarecrow: "They call me The Scarecrow. I'm here looking for Black Wing."'''
		print '''Scarecrow: "Now, out of my way. You're wasting my time."'''
		print "You brandish your sword, preparing to fight him."
		print "He simply sneers at you and easily shoves you aside."
		print "With that, he leaves the room."
	else:
		print "You arrive in an empty room."
		
	print "The only exit is the one you came from, to the north."
	print "What do you do?"
	while True:
		next = raw_input("> ")
		if "north" in next or "leave" in next or "go back" in next:
			print "You travel 5 feet north before reaching a room."
			room5()
		elif "search" in next or "look around" in next:
			print "You find nothing of interest in this room."
		else:
			print "I don't know what you want to do... input something else please."

def secret_room():
	global gold_of_secret_room_taken
	if gold_of_secret_room_taken:
		print "This room is empty and the only exit is to the east."
		print "What do you want to do?"
	else:
		gold("As you enter this room, gold suddenly pours from the ceiling.", 1000)
		gold_of_secret_room_taken = True
		print "The room you are in has no exits except the one you came from, to the east."
		print "Now what do you want to do?"
	
	while True:
		next = raw_input("> ")
		if "east" in next or "leave" in next or "go back" in next:
			print "You travel 5 feet east, going back through the secret doorway into a room."
			room9()
		elif "search" in next or "look around" in next:
			print "You find nothing of interest in this room."
		else:
			print "I don't know what you want to do... input something else please."

def room6():
	global player_health
	global dwarf_alive
	dwarf_attacking = True
	dwarf_dodging = False
	dwarf_health = 30
	if dwarf_alive:
		print "In this room, you meet a dwarf."
		print "He immediately starts to swipe at you with a sword."
		while dwarf_alive:
			next = raw_input("> ")
			if dwarf_attacking and ("dodge" in next or "jump back" in next):
				print "You dodge his attack."
				dwarf_attacking = False
				dwarf_dodging = True
			elif not dwarf_attacking and ("dodge" in next or "jump back" in next):
				print "You jump back and the dwarf starts to come towards you."
				dwarf_attacking = True
			elif dwarf_dodging and not dwarf_attacking and ("attack" in next or "swing" in next or "swipe" in next or "kill" in next):
				print "The dwarf dodges your attack, but is now off balance."
				dwarf_dodging = False
			elif not dwarf_dodging and not dwarf_attacking and("attack" in next or "swing" in next or "swipe" in next or "kill" in next):
				print "Your attack hits and deals 10 damage."
				dwarf_health -= 10
				if dwarf_health == 0:
					print "That attack killed the dwarf."
					dwarf_alive = False
				else:
					print "The dwarf staggers back and then comes at you."
					dwarf_attacking = True
					dwarf_dodging = True
			elif dwarf_attacking and ("attack" in next or "swing" in next or "swipe" in next or "kill" in next):
				print "Both of your attacks hit each other. You deal 10 damage and he deals 5."
				player_health -= 5
				dead()
				dwarf_health -= 10
				if dwarf_health == 0:
					print "That attack still managed to kill the dwarf."
					dwarf_alive = False
				else:
					print "You both stagger backwards."
					dwarf_dodging = True
					dwarf_attacking = False
			else:
				print "The dwarf takes the opportunity to quickly attack and deals 3 damage."
				player_health -= 3
				dead()
				dwarf_dodging = True
				dwarf_attacking = False
		
	else:
		print "You arrive in a room that contains the corpse of a dwarf."
	
	print "There are exits in all four directions."
	print "Where do you want to go?"	
	while True:
		next = raw_input("> ")
		if "west" in next:
			print "You travel 20 feet before reaching a room."
			room4()
		elif "east" in next:
			print "You travel 5 feet east before reaching another room."
			room10()
		elif "north" in next:
			print "You travel 5 feet north and arrive in a different room."
			room8()
		elif "south" in next:
			print "You travel 5 feet south and enter a room."
			room12()
		elif "search" in next or "look around" in next:
			print "You find nothing of interest in this room."
		else:
			print "I don't know what you want to do... input something else please."

def room8():
	global room8_gold_taken
	global player_health
	print "You arrive in a room that only contains a treasure chest near the north wall."
	print "The only exit is the one you came from, to the south."
	print "What do you do?"
	while True:
		next = raw_input("> ")
		if not room8_gold_taken and "open" in next and ("dodge" in next or "jump back" in next or "avoid" in next or "back away" in next or "move away" in next):
			print "You open the chest and quickly jump away from it."
			print "The treasure chest suddenly gets launched into the air and slams down \nwhere you had been standing."
			gold("Gold spews everywhere.", 1200)
		elif not room8_gold_taken and "open" in next:
			print "As you open the chest, it suddenly gets launched into the air and slams \ndown on top of you."
			player_health -= 10
			dead()
			gold("You take 10 damage from the chest and gold spews everywhere.", 1200)
			room8_gold_taken = True
			print "Now the gold is gone. The only thing in the room is the now \nclosed treasure chest."
			print "What do you want to do?"
		elif room8_gold_taken and "open" in next:
			print "You open the chest. It is empty and nothing happens."
		elif "south" in next or "leave" in next or "go back" in next:
			print "You leave the room and travel 5 feet south before reaching a room."
			room6()
		elif "search" in next or "look around" in next:
			print "You find nothing of interest in this room other than the treasure chest."
		else:
			print "I don't know what you want to do... input something else."

def room10():
	global miyu_alive
	global miyu_with_you
	if miyu_alive:
		print "In this room, you find a little girl crying." 
		print "She is standing near the body of a dead, fat man."
		print "What do you do?"
		while miyu_alive and not miyu_with_you:
			next = raw_input("> ")
			if "kill" in next or "attack" in next or "swing" in next:
				print "You kill the girl."
				miyu_alive = False
			elif "search" in next or "look around" in next:
				print "You search around the room, finding nothing of particular interest."
				print "You also inspect the body. It appears that the man was killed with a sword."
			elif "ask" in next and ("man" in next or "guy" in next or "body" in next):
				print '''Miyu: "He was taking me through these caves, but a woman in all \nblack killed him."'''
			elif ("ask" in next and ("father" in next or "dad" in next or "related" in next)) or ("do you know him" in next):
				print '''Miyu: "No, I don't really know him."'''
			elif "ask" in next and "name" in next:
				print "She says her name is Miyu."
			elif "talk to" in next:
				print "She says her name is Miyu."
				print '''Miyu: "This man was taking me through the caves, but some woman \nin black killed him when he was trying to pick up gold."'''
				print '''Miyu: "I don't really know him, he just dragged me in here."'''
			elif "take" in next or ("bring" in next and "along" in next) or "follow" in next:
				print "She agrees to go along with you. Whenever you stop, she clings to your leg."
				miyu_with_you = True
			elif "avoid" in next or "ignore" in next or "leave" in next or "go back" in next or "west" in next:
				print "The girl runs over to you and clings to your leg."
			else:
				print "You do nothing."
			
	else:
		if not miyu_alive:
			print "In this room, you find the body of a fat man and the body of a little girl."
		else:
			print "In this room, you find the body of a fat man."
		
	print "There is only the exit to the west."
	print "What do you want to do?"
	
	while True:
		next = raw_input("> ")
		if "west" in next or "leave" in next or "go back" in next:
			print "You leave the room and travel 5 feet west before reaching a room."
			room6()
		elif "search" in next or "look around" in next:
			print "You find nothing of interest in this room."
		else:
			print "I don't know what you want to do... input something else."

def room12():
	global ninjas_alive
	if ninjas_alive:
		print "In this room, you find two people sitting cross-legged on the floor."
		print "What do you do?"
		while ninjas_alive:
			next = raw_input("> ")
			if "attack" in next or "kill" in next or "swing" in next or "swipe" in next:
				print "You swing your sword at the man on the right."
				print "Just before your strike hits, though, the man vanishes."
				print "Surprised, your swing continues until it hits the second man, making a \nmetallic clanging sound."
				print "You realize that this man is made of metal, and is actually an extremely \nlife-like statue."
				ninjas_alive = False
			elif "talk" in next or "ask" in next:
				print "You try to talk to the men, but there is no response."
			elif "leave" in next or "go back" in next or "north" in next:
				print "As you turn to leave, someone grabs your ankle and you fall to the ground."
				print "Getting back up, you turn around, but the men do not appear to have moved."
			else:
				print "Nothing happens."
			
	else:
		print "In this room, you find a statue of a man sitting cross-legged on the floor."
		
	print "The only exit to this room is where you came from, to the north."
	print "What do you want to do?"
	
	while True:
		next = raw_input("> ")
		if "north" in next or "leave" in next or "go back" in next:
			print "You leave the room and travel 5 feet north before reaching a room."
			room6()
		elif "search" in next or "look around" in next:
			print "You find nothing of interest in this room."
		else:
			print "I don't know what you want to do... input something else."

def eventB():
	global eventB_occured
	global player_health
	global snow_alive
	global scarecrow_alive
	if snow_alive:
		print "You travel 30 feet north before running into two people."
		print "One person, a woman, is clothed in red and has white hair."
		print "The other person, a man, was talking to the woman when you arrived."
		print "They turn to you, upset that you would disturb their discussions."
		print '''Woman: "Don't worry honey, I'll take care of this fool."'''
		print "What do you do?"
		snow_fight()
		print '''Man: "How dare you!"'''
		print "He immediately starts to attack you."
		print "What do you do?"
		scarecrow_fight()
	else:
		print "You travel 30 feet north before running into someone."
		print "The person, a man, is simply standing staring at you."
		print '''Man: "YOU! YOU KILLED MY WIFE!"'''
		print "He immediately starts to attack you."
		print "What do you do?"
		scarecrow_fight()
	
	eventB_occured = True
	print "Having dispatched the two bounty hunters, you continue another 20 feet down \nthe hallway and reach another room."
	room13()

def scarecrow_fight():
	global player_health
	global scarecrow_alive
	scarecrow_attacking = True
	scarecrow_dodging = True
	scarecrow_attacked_once = False
	scarecrow_health = 50
	while scarecrow_alive:
		next = raw_input("> ")
		if "talk" in next:
			print "As you try to speak, he hits you with his sword, dealing 7 damage."
			player_health -= 7
			dead()
			scarecrow_attacking = False
			scarecrow_dodging = True
		elif ("dodge" in next or "jump back" in next) and scarecrow_attacking and scarecrow_attacked_once:
			print "You dodge the attack."
			scarecrow_attacking = False
			scarecrow_attacked_once = False
		elif ("dodge" in next or "jump back" in next) and scarecrow_attacking and not scarecrow_attacked_once:
			print "You jump away, but the man comes after you."
			scarecrow_attacking = True
			scarecrow_attacked_once = True
		elif ("dodge" in next or "jump back" in next) and not scarecrow_attacking and scarecrow_attacked_once:
			first_turn = False
			print "You back away a bit. He starts moving in towards you."
			scarecrow_attacking = True
			scarecrow_attacked_once = False
		elif ("dodge" in next or "jump back" in next) and not scarecrow_attacking and not scarecrow_attacked_once:
			first_turn = False
			print "You jump back. He starts moving in towards you."
			scarecrow_attacking = True
			scarecrow_attacked_once = True
		elif ("attack" in next or "swing" in next or "slice" in next or "kill" in next) and not scarecrow_attacking and not scarecrow_dodging:
			print "You attack the man, dealing 10 damage."
			scarecrow_health -= 10
			first_turn = False
			if scarecrow_health == 0:
				print "Your last attack was enough to kill the man."
				scarecrow_alive = False
			else:
				print "He then starts to swing at you again."
				scarecrow_attacking = True
				scarecrow_dodging = True
		elif ("attack" in next or "swing" in next or "slice" in next or "kill" in next) and not scarecrow_attacking and scarecrow_dodging:
			print "He dodges your attack, but is now off balance."
			first_turn = False
			scarecrow_dodging = False
			scarecrow_attacking = False
		elif ("attack" in next or "swing" in next or "slice" in next or "kill" in next) and scarecrow_attacking and not scarecrow_dodging:
			print "Both of your attacks, hit, your attack dealing 10 damage, his dealing 7."
			scarecrow_health -= 10
			player_health -= 7
			dead()
			first_turn = False
			if scarecrow_health == 0:
				print "Your last attack was still enough to kill the man."
				scarecrow_alive = False
			else:
				print "He then starts to swing at you again."
				scarecrow_attacking = True
		elif ("attack" in next or "swing" in next or "slice" in next or "kill" in next) and scarecrow_attacking and scarecrow_dodging:
			print "He manages to dodge your attack and still hit you, dealing 5 damage."
			player_health -= 5
			dead()
			first_turn = False
			print "He then starts to swing at you again."
			scarecrow_attacking = True
			scarecrow_dodging = True
		else:
			print "He takes the opportunity to attack you, dealing 5 damage."
			player_health -= 5
			dead()
			scarecrow_attacking = False
			scarecrow_dodging = True
			scarecrow_attacked_once = False

def room13():
	global door2_closed
	global door3_closed
	print "This room is empty."
	if door2_closed and door3_closed:
		print "There are exits in all four directions."
		print "However, the north and east doors are locked."
	elif door2_closed and not door3_closed:
		print "There are exits in all four directions, but the north door is locked."
	elif not door2_closed and door3_closed:
		print "There are exits in all four directions, but the east door is locked."
	else: 
		print "There are exits in all four directions, and all doors are open."
	print "What do you want to do?"
	
	while True:
		next = raw_input("> ")
		if ("break down" in next or "unlock" in next) and "east" in next and door3_closed:
			print "You efforts to shove down the door succeed. The eastern passage is \nnow unobstructed."
			door3_closed = False
		elif "east" in next and door3_closed:
			print "This passage is blocked."
		elif "east" in next and not door3_closed:
			print "You travel 5 feet east, turn north, and travel another 5 feet before \nreaching a room."
			room15()
		elif "south" in next:
			print "You travel 50 feet south, passing two bodies in the hallway before \nreaching a room."
			room4()
		elif "west" in next:
			print "You travel 5 feet west, turn north, and travel another 5 feet before \nreaching a room."
			room14()
		elif ("break down" in next or "unlock" in next) and "north" in next and door2_closed:
			print "You are unable to break down or unlock this door. It is magically sealed."
		elif "north" in next and door2_closed:
			print "This passage is blocked."
		elif "north" in next and not door2_closed:
			print "You travel 10 feet north and reach a room."
			room18()
		elif "search" in next or "look around" in next:
			print "You search reveals nothing more about the room."
		else:
			print "I don't know what you want to do... input something else please."

def room14():
	print "This room is empty."
	if door1_closed:
		print "There are exits to the north, west, and south, but the north exit is locked."
	else:
		print "There are exits to the north, west, and south.\nAll doors are open."
	
	print "What do you want to do?"
	
	while True:
		next = raw_input("> ")
		if ("break down" in next or "unlock" in next) and "north" in next and door1_closed:
			print "You are unable to break down or unlock this door. It is magically sealed."
		elif "north" in next and door1_closed:
			print "This passage is blocked."
		elif "north" in next and not door1_closed:
			print "You travel 5 feet north, turn east, and travel another 5 feet before reaching a room."
			room18()
		elif "south" in next:
			print "You travel 5 feet south, turn east, and travel another 5 feet before reaching a room."
			room13()
		elif "west" in next:
			print "You travel 10 feet west before reaching another room."
			room16()
		elif "search" in next or "look around" in next:
			print "You search reveals nothing more about the room."
		else:
			print "I don't know what you want to do... input something else please."

def room15():
	global rouge_alive
	global player_health
	if rouge_alive:
		print "As you enter the room, a rouge warrior jumps down from the rafters."
		print "What do you do?"
		rouge_health = 30
		rouge_attacking = False
		while rouge_alive:
			next = raw_input("> ")
			if "flee" in next or "run" in next or "escape" in next or "go past" in next:
				print "You may not run away from a fight or you will die."
			elif ("attack" in next or "slice" in next or ("swing" in next and "sword" in next)) and not rouge_attacking:
				print "The rouge takes 10 damage from your attack."
				rouge_health -= 10
				if rouge_health == 0:
					rouge_alive = False
					print "The attack kills the rouge."
				else:
					print "He staggers back before moving to attack you."
					rouge_attacking = True
			elif ("attack" in next or "slice" in next or ("swing" in next and "sword" in next)) and rouge_attacking:
				print "The rouge takes 10 damage from your attack, but you also take 5 damage \nfrom its attack."
				rouge_health -= 10
				player_health -= 5
				dead()
				if rouge_health == 0:
					rouge_alive = False
					print "The attack still killed the rouge though."
				else:
					print "Both you and the rouge move back from each other."
					rouge_attacking = False
			elif ("dodge" in next or "jump back" in next) and rouge_attacking:
				print "The rouge's slash at you misses."
				rouge_attacking = False
			elif ("dodge" in next or "jump back" in next) and not rouge_attacking:
				print "You move back a little. The rouge starts running at you."
				rouge_attacking = True
			else:
				print "The rouge takes the opportunity to attack you and deals 5 damage."
				player_health -= 5
				dead()
				rouge_attacking = False
		
	else:
		print "You arrive in a room that has the body of a dead rouge."
	
	if door4_closed:
		print "There are exits to the north, east, and south, but the north exit is locked."
	else:
		print "There are exits to the north, east, and south.\nAll doors are open."
	
	print "What do you want to do?"
	
	while True:
		next = raw_input("> ")
		if ("break down" in next or "unlock" in next) and "north" in next and door4_closed:
			print "You are unable to break down or unlock this door. It is magically sealed."
		elif "north" in next and door4_closed:
			print "This passage is blocked."
		elif "north" in next and not door4_closed:
			print "You travel 5 feet north, turn west, and travel another 5 feet before \nreaching a room."
			room18()
		elif "south" in next:
			print "You travel 5 feet south, turn west, and travel another 5 feet before \nreaching a room."
			room13()
		elif "east" in next:
			print "You travel 10 feet east before reaching another room."
			room17()
		elif "search" in next or "look around" in next:
			print "You search reveals nothing more about the room."
		else:
			print "I don't know what you want to do... input something else please."

def room16():
	global room16_button_discovered
	global player_health
	global door3_closed
	pentagram_discovered = False
	exit_opened = False
	time = 0
	if room16_button_discovered:
		print "You arrive in a snow-covered room with a pentagram on the floor."
	else:
		print "As you enter this room, the doorway behind closes and disappears, leaving only \na solid wall behind."
		print "The temperature in the room starts to rapidly decrease and you start shivering."
		print "What do you do?"
		while not exit_opened:
			next = raw_input("> ")
			time += 1
			
			if "break down" in next or "unlock" in next:
				print "You are unable to move the wall."
			elif ("inspect" in next or "search" in next) and "wall" in next:
				print "You find nothing useful on the walls."
			elif ("inspect" in next or "search" in next) and "floor" in next and not pentagram_discovered:
				print "You find a pentagram carving on the floor."
				pentagram_discovered = True
			elif ("inspect" in next or "search" in next) and ("pentagram" in next or "floor" in next) and pentagram_discovered:
				print "Looking closer at the pentagram, you find a button in the center of it."
				room16_button_discovered = True
			elif ("search" in next or "look around" in next) and "room" in next:
				print "Your basic search uncovers nothing."
			elif ("push" in next or "press" in next or "activate" in next) and "button" in next:
				print "You push the button in the pentagram and the eastern wall suddenly \nvanishes, revealing the hallway you came from."
				print "The temperature also returns to normal."
				exit_opened = True
			else:
				print "I don't know what you want to do... input something else please."
			
			if time == 6:
				print "You are starting to freeze. You take 1 damage."
				player_health -= 1
			elif time > 6:
				print "You take 1 damage from freezing."
				player_health -= 1	
			dead()
	
	door3_closed = False
	print "The only exit is the one you came from, to the east."
	print "What do you want to do?"
	
	while True:
		next = raw_input("> ")
		if "east" in next or "leave" in next or "go back" in next:
			print "You leave the room and travel 10 feet east before reaching a room."
			room14()
		elif "search" in next or "look around" in next:
			print "You find nothing else of interest in this room."
		else:
			print "I don't know what you want to do... input something else."

def room17():
	print "In this room, you find 6 levers on the walls, 2 on each wall except the \nwestern wall."
	print "What do you want to do?"
	lever_fun()

def lever_fun():
	global room17_gold_taken
	global room17_healing_used
	global player_health
	global door1_closed
	global door2_closed
	global door4_closed
	next = raw_input("> ")
	if "pull" in next and "top left" in next:
		print "You pull the lever and spears shoot out of the ground in the top half \nof the room."
		print "As you were standing by that lever, the spears deal 10 damage to you."
		player_health -= 10
	elif "pull" in next and "top right" in next and not room17_healing_used:
		print "You pull the lever and water pours out of the ceiling, briefly covering the \nfloor before vanishing."
		print "The water heals you completely."
		player_health = 50
		room17_healing_used = True
	elif "pull" in next and "top right" in next and room17_healing_used:
		print "You pull the lever, but nothing happens."
	elif "pull" in next and "right top" in next:
		print "An absolutely massive spears shoots out of the eastern wall."
		print "It fills the majority of the bottom half of the room before retracting back \ninto the wall."
	elif "pull" in next and "right bottom" in next:
		print "You pull the lever and hear what sounds like a mechanism turning."
		print "Nothing in the room changes though."
		door1_closed = False
		door2_closed = False
		door4_closed = False
	elif "pull" in next and "bottom left" in next and not room17_gold_taken:
		gold("You pull the lever and gold starts pouring from the south wall.", 2000)
		room17_gold_taken = True
	elif "pull" in next and "bottom left" in next and room17_gold_taken:
		print "You pull the lever, but nothing happens."
	elif "pull" in next and "bottom right" in next:
		print "You pull the lever and an explosion goes off in the north-west corner \nof the room."
		print "There was no apparent cause and it left no damage."
	elif "west" in next or "go back" in next or "leave" in next:
		print "You leave the room, travelling 10 feet the east and arrive in another room."
		room15()
	else:
		print "I don't know what you want to do... input something else please."
	
	lever_fun()

def room18():
	print "This room is empty."
	print "To the north, there is an especially menacing-looking door."
	print "There are exits in all for directions."
	print "What do you want to do?"
	
	while True:
		next = raw_input("> ")
		if "north" in next:
			print "You go through the menacing door."
			room19()
		elif "south" in next:
			print "You travel 10 feet south before reaching another room."
			room13()
		elif "east" in next:
			print "You travel 5 feet east, turn south, and travel another 5 feet before reaching \na room."
			room15()
		elif "west" in next:
			print "You travel 5 feet west, turn south, and travel another 5 feet before reaching \na room."
			room14()
		elif "search" in next or "look around" in next:
			print "You find nothing of interest in this room."
		else:
			print "I don't know what you want to do... input something else please."

def room19():
	print "BOSS ROOM!"
	print "In this room, you find one person, who looks a lot like you."
	print '''Person: "It's about time you got here."'''
	print '''Person: "I know you're itching to fight me, but let's talk a little first."'''
	continue_allowed = False
	while True:
		next = raw_input("> ")
		if "who sent you" in next or "working" in next or "master" in next:
			print '''Dark You: "I was sent by Lucian. But he's not even the one in top command. \n\t   Even I don't know who that is."'''
			continue_allowed = True
		elif "who are you" in next:
			print '''Dark You: "I am you. A better version of you."'''
		elif "why are you doing" in next or "why are you working" in next or "why are you fighting" in next:
			print '''Dark You: "I'm not the one in control. I must obey the master."'''
		elif "black wing" in next:
			print '''Dark You: "Yes, I am also known as Black Wing."'''
		elif "bounty hunter" in next:
			print '''Dark You: "There were bounty hunters? I didn't know about them."'''
		elif "don't underestimate me" in next and continue_allowed:
			print '''Dark You: "Fine, but don't underestimate me either."'''
			print "Starting boss fight..."
			boss_fight()
		elif "don't underestimate me" in next and not continue_allowed:
			print '''Dark You: "Before we fight, don't you want to know who I'm working for?"'''
		elif "victory" in next and continue_allowed:
			print '''You: "My victory shall be swift!"'''
			print "Starting boss fight..."
			boss_fight()
		elif "victory" in next and not continue_allowed:
			print '''Dark You: "Before we fight, don't you want to know who I'm working for?"'''
		elif ("fight" in next or "attack" in next or "swing" in next or "slash" in next) and continue_allowed:
			print '''You: "Enough talk, let's fight!"'''
			print "Starting boss fight..."
			boss_fight()
		elif ("fight" in next or "attack" in next or "swing" in next or "slash" in next) and not continue_allowed:
			print '''Dark You: "Before we fight, don't you want to know who I'm working for?"'''
		else:
			print '''Dark You: "I don't know what you're saying."'''	

def boss_fight():
	global player_health
	global boss_alive
	boss_attacking = False
	boss_dodging = True
	boss_health = 100
	charging = False
	youre_off_balance = False
	
	# nonsense with a seed file for a different seed each time.
	if exists('seed.txt'):
		target = open('seed.txt', 'r')
		oldseed = int(target.read())
		seed(oldseed)
		target.close()
		target2 = open('seed.txt', 'w')
		target2.truncate()
		newseed = randint(1,1000000)
		target2.write(str(newseed))
		target2.close()
	else:
		seed(randint(1,1000000))
	
	# end nonsense	
	
	while boss_alive:
		next = raw_input("> ")
		num = randint(1,10)
		if "talk" in next:
			print "As you try to speak, he hits you with his sword, dealing 7 damage."
			player_health -= 7
			dead()
			boss_attacking = False
			boss_dodging = True
		
		elif charging and ("dodge" in next or "jump back" in next):
			print "Dark You starts to glow red and a wave of fire starts to spread out from him."
			print "As it spreads in all directions, you are unable to dodge."
			print "You take 8 damage from the fire."
			charging = False
		
		elif charging and ("attack" in  next or "swing" in next or "slice" in next or "kill" in next):
			print "Dark You starts to glow red, but before anything can happen, you attack him, \npreventing him from releasing his attack."
			print "You deal 15 damage."
			boss_health -= 15
			if boss_health <= 0:
				print "Your last attack was enough to kill your evil twin."
				boss_alive = False
			else:
				print "He then starts to swing at you again."
				boss_attacking = True
				boss_dodging = True
			charging = False
		
		elif ("dodge" in next or "jump back" in next) and boss_attacking and not youre_off_balance:
			if num > 3:
				print "You dodge the attack."
				boss_attacking = False
			elif num == 3:
				print "You barely dodge the attack, before Evil You starts to swing again."
				boss_attacking = True
			else:
				print "Evil You is too quick and you take 5 damage from his attack."
				player_health -= 5
				dead()
				boss_attacking = False
				
		elif ("dodge" in next or "jump back" in next) and boss_attacking and youre_off_balance:
			if num > 6:
				print "You dodge the attack."
				boss_attacking = False
			elif num == 6:
				print "You barely dodge the attack, before Evil You starts to swing again."
				boss_attacking = True
			else:
				print "Evil You is too quick and you take 5 damage from his attack."
				player_health -= 5
				dead()
				boss_attacking = False
		
		elif ("dodge" in next or "jump back" in next) and not boss_attacking:
			print "You back away a bit. He starts moving in towards you."
			boss_attacking = True
		
		elif ("attack" in next or "swing" in next or "slice" in next or "kill" in next) and not boss_attacking and not boss_dodging:
			if num > 3:
				print "You attack the Dark You, dealing 10 damage."
				boss_health -= 10
				if boss_health <= 0:
					print "Your last attack was enough to kill your evil twin."
					boss_alive = False
				else:
					print "He then starts to swing at you again."
					boss_attacking = True
					boss_dodging = True
			elif num == 3:
				print "Dark You teleports away and your attack misses entirely."
				print "Dark You now appears to be charging some kind of attack."
				charging = True
				boss_attacking = False
			else:
				print "Dark You is too quick and dodges your attack."
				print "He swings at you and you are off balance."
				boss_attacking = True
				boss_dodging = False
				youre_off_balance = True
		
		elif ("attack" in next or "swing" in next or "slice" in next or "kill" in next) and not boss_attacking and boss_dodging:
			if num > 3:
				print "He dodges your attack, but is now off balance."
				boss_dodging = False
				boss_attacking = False
			elif num == 3:
				print "He dodges your attack and starts a counter attack."
				boss_attacking = True
				boss_dodging = False
			else:
				print "You're attack was very swift and Dark You is unable to dodge."
				print "You deal 10 damage."
				boss_health -= 10
				if boss_health <= 0:
					print "Your last attack was still enough to kill your evil twin."
					boss_alive = False
				else:
					print "Dark You then backs away and appears to be preparing some kind of attack."
					charging = True
			
		elif ("attack" in next or "swing" in next or "slice" in next or "kill" in next) and boss_attacking and not boss_dodging:
			print "Both of your attacks, hit, your attack dealing 10 damage, his dealing 7."
			boss_health -= 10
			player_health -= 7
			dead()
			if boss_health <= 0:
				print "Your last attack was still enough to kill your evil twin."
				boss_alive = False
			else:
				print "He then starts to swing at you again."
				boss_attacking = True
		
		elif ("attack" in next or "swing" in next or "slice" in next or "kill" in next) and boss_attacking and boss_dodging:
			print "He manages to dodge your attack and still hit you, dealing 5 damage."
			player_health -= 5
			dead()
			print "He then starts to swing at you again."
			boss_attacking = True
			boss_dodging = True
		
		else:
			print "He takes the opportunity to attack you, dealing 5 damage."
			player_health -= 5
			dead()
			boss_attacking = False
			boss_dodging = True
				
	ending()

def ending():
	print "Black Wing is dead!"
	print "You are victorious!"
	print "Gold and diamonds and emeralds and rubies and all the gems you can think of \nflood the room."
	print "In fact, it starts to create an avalanche of gold and gems that will kill you \nif you don't run."
	print "So with the gold avalanche right behind you, you race out of the dungeon."
	if hina_alive:
		print "On the way, you find Hina and drag her with you, though she is desperate to \nget the gold."
	
	print "You make it out of the dungeon. The avalanche reaches a stop just at the \nentrance to the dungeon."
	if hina_alive:
		print "You have more gold than you could ever have imagined, as long as Hina doesn't \ntake it all first."
	else:
		print "You have more gold than you could ever have imagined."
		
	print '''You: "Hmmm, so the Dark Me wasn't in charge. So about that Lucian..."'''
	print "The End!"
	exit(0)

def start():
	print "You are about to enter a dungeon."
	print "On your person, you carry a sword that can be used to attack."
	print "You have 50 health, which does not regenerate naturally."
	print "Are you ready to enter this dungeon?"
	begin = raw_input("> ")
	if begin == "yes":
		room1()
	else:
		print "Too bad, there's nothing else to do outside so you're going in."
		room1()

room18()