import os
import random


def show_message(msg):
	os.system("clear")
	os.system("figlet " + msg)
	
show_message("Loading...")
# load data from file
f = open("questions.txt")
data = f.read().replace("\r", "").split("\n")
keywords = data[::2]
definitions = data[1::2]
NUM_QUESTIONS = len(keywords)
f.close()

# load message data
f = open("message.csv")
coords = f.read().replace("\r", "").split("\n")
f.close()

# create link to minecraft
import minecraft
import block
mc = minecraft.Minecraft.create()

show_message("Welcome")
print """The aim of this quiz is to help you remember and understand 
the key words in Computer Hardware

Hopefully, we'll also learn a bit about how computers work and 
have some fun with minecraft along the way too.

Press Enter to continue..."""
while True:
	option = raw_input()
	
	if option == "o:clues":
		clues = coords[:]
		while len(clues) > 10:
			clues.pop()
			random.shuffle(clues)
		for line in clues:
				c = line.split(",")
				x = int(c[0])
				y = int(c[1])
				z = int(c[2])
				mc.setBlock(x,y,z,random.choice((block.LEAVES, block.WOOD, block.TNT)))
		mc.postToChat("10 clues added")
	elif option == "o:clear":
		mc.setBlocks(0, 0, -1, 90, 80, 1, block.AIR)
	elif option == "o:board":
		mc.setBlocks(0, 0, -1, 90, 80, -1, block.GLASS)
	elif option == "o:test LEAVES":
		try:
			for line in coords:
				c = line.split(",")
				x = int(c[0])
				y = int(c[1])
				z = int(c[2])
				mc.setBlock(x,y,z,block.LEAVES)
		except:
			pass
	elif option == "o:test WOOD":
		try:
			for line in coords:
				c = line.split(",")
				x = int(c[0])
				y = int(c[1])
				z = int(c[2])
				mc.setBlock(x,y,z,block.WOOD)
		except:
			pass
	elif option == "o:test TNT":
		try:
			for line in coords:
				c = line.split(",")
				x = int(c[0])
				y = int(c[1])
				z = int(c[2])
				mc.setBlock(x,y,z,block.TNT)
		except:
			pass
	elif option == "o:test":
		try:
			for line in coords:
				c = line.split(",")
				x = int(c[0])
				y = int(c[1])
				z = int(c[2])
				mc.setBlock(x,y,z,random.choice((block.LEAVES, block.WOOD, block.TNT)))
		except:
			pass
	else:
		break
show_message("Setup")
print "This is going to be a competition, so first we need to know your name and what team you're on"
print

while True:
	names = raw_input("Please enter your names (e.g. Mike):")
	
	if len(names) == 0:
		print "Try again, you must enter your name"
	else:
		break

while True:
	team = raw_input("""
	Which team are you in?
	1: Leaves
	2: Wood
	3: TNT

	Please choose your team by typing 1, 2 or 3 (then press enter)
	""").strip()
	teams = ['Leaves', 'Wood', 'TNT']
	if team in "123":
		try:
			team = teams[int(team) - 1]
			print "Thank you. You are in team:", team
			break
		except:
			pass
	print "Please try again - you must choose 1, 2 or 3"
q = 0
score = 0



# setup minecraft
mc.postToChat(names + " in team " + team + " just joined the quiz")

if team == "Leaves":
	b = block.LEAVES
elif team == "Wood":
	b = block.WOOD
else:
	b = block.TNT




while True:
	q += 1
	show_message("Score: " + str(score))
	print "Name:", names
	print "Team:", team
	print
	print "In order to get points you need to enter minecraft coordinates correctly"
	print "In order to enter minecraft coordinates, you need to answer this question correctly:"
	
	i = random.randint(0, NUM_QUESTIONS - 1)
	print
	print "Keyword:", keywords[i]
	print
	print "is it:"
	
	options = data[1::2]
	options.remove(definitions[i])
	while(len(options) > 3):
		options.pop()
		random.shuffle(options)
	options.append(definitions[i])
	random.shuffle(options)
	
	letters = "abcd"
	for j in range(4):
		print "  ", letters[j] + ":", options[j]
	print
	while True:
		option = raw_input("Which is the correct definition: (a, b, c or d)?").strip().lower()
		if option in letters:
			break
		else:
			print "Please type a, b, c or d"
		
	chosen_index = letters.index(option)
	print options[chosen_index], definitions[i]
	correct = options[chosen_index] == definitions[i]
	if correct:
		show_message("Correct")
		print "Well done!"
		print "The right definition of", keywords[i], "is:"
		print " ", definitions[i]
	else:
		show_message("Wrong")
		print "The right definition of", keywords[i], "is:"
		print " ", definitions[i]
		
	print 
	raw_input("Press ENTER to continue")
	
	if correct:
		show_message("Score: " + str(score))
		print "Name(s):", names
		print "Team:", team
		print

		cx,cy,cz = random.choice(coords).split(",")
		
		q_type = random.choice(("b2d", "d2b"))
		
		if q_type == "b2d":
			# convert binary to decimal
			cx_bin = bin(int(cx))[2:]
			cy_bin = bin(int(cy))[2:]
			
			print "You can now enter a minecraft coordinate in decimal."
			print "If you enter both numbers correctly, you will get a point"
			
			print
			print "Your randomly chosen coordinate is x:" + cx_bin + ", y:"+ cy_bin
			print
			print "Convert these numbers from binary and enter them carefully below:"
			x_dec = raw_input("Carefully enter the X coordinate:").strip()
			y_dec = raw_input("Carefully enter the Y coordinate:").strip()
			
			
			print
			print "You entered:", x_dec, y_dec
			try:
				print "When you convert ", cx_bin, "to binary you get x =", cx
				print "When you convert ", cy_bin, "to binary you get y =", cy
				
				if x_dec == cx and y_dec == cy:
					print "Well done - your block has now been sent to minecraft"
					mc.setBlock(int(cx),int(cy),0,b)
					score +=1 
					mc.postToChat(names+" just built some "+team+ " at x=" + cx + ", y=" + cy + " score=" + str(score))
				else:
					raise
			except:
				print "I'm sorry, you typed in one of the coordinates wrong. Please try again"

		else:
			# convert decimal to binary
		
		
			print "You can now enter a minecraft coordinate in binary."
			print "If you enter both numbers correctly, you will get a point"
			
			print
			print "Your randomly chosen coordinate is x:" + cx + ", y:"+ cy
			print
			print "Convert these numbers to binary and enter them carefully below:"
			x_bin = raw_input("Carefully enter the X coordinate:").replace(" ", "")
			y_bin = raw_input("Carefully enter the Y coordinate:").replace(" ", "")
			
			
			print
			print "You entered:", x_bin, y_bin
			try:
				x = int(x_bin,2)
				y = int(y_bin,2)
				print "When you convert ", x_bin, "from binary you get x =", x
				print "When you convert ", y_bin, "from binary you get y =", y
				
				if int(cx) == x and int(cy) == y:
					print "Well done - your block has now been sent to minecraft"
					mc.setBlock(x,y,0,b)
					score +=1 
					mc.postToChat(names+" just built some "+team+ " at x=" + str(x) + ", y=" + str(y) + " score=" + str(score))
				else:
					raise
			except:
				print "I'm sorry, you typed in one of the coordinates wrong. Please try again"
	
		print
		raw_input("Press ENTER for your next question")
