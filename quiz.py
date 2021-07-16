from datetime import datetime
lives = 10
name = input ("Enter your name: ")
print ("Hello, " + name)
print ("You are here to solve the quiz!")
print ("Your goals are to answer the questions with less time and save all 10 lives.")
print ("\nTo start the game type 'GO'. Good luck!")
a = input ("Type here: ")
if a == "GO":
	print ("Time is started!")
	st = datetime.now()
	print (" ")
	ans = input ("How many days are there in a week? ")
	while ans.upper() !="SEVEN" and lives > 1:
		lives -= 1
		ans = input ("Wrong. Be careful you've only {0} lives. ".format(lives))
if lives <= 1:
	now = datetime.now()
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Right. Keep going!")
print (" ")
ans = int(input ("When 2x + 18 = 84 then x = "))
while ans !=33 and lives > 1:
	lives -= 1
	ans = int(input("Wrong. Be careful you've only {0} lives. ".format(lives)))
if lives <= 1:
	now = datetime.now() - st
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Awesome. Keep going!")
print (" ")
ans = int(input ("How many letters are there in the English Alphabet? "))
while ans != 26 and lives > 1:
	lives -= 1
	ans = int(input("Wrong. Be careful you've only {0} lives. ".format(lives)))
if lives <= 1:
	now = datetime.now() - st
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Good. Keep going!")
print (" ")
ans = int(input ("How many continents in the world? "))
while ans != 7 and lives > 1:
	lives -= 1
	ans = int(input("Wrong. Be careful you've only {0} lives. ".format(lives)))
if lives <= 1:
	now = datetime.now() - st
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Cool. Keep going!")
print (" ")
ans = input ("Name of the first president of INDIA: ")
while ans.upper() != "DR RAJENDRA PRASAD" and lives > 1:
	lives -= 1
	ans = input("Wrong. Be careful you've only {0} lives. ".format(lives))
if lives <= 1:
	now = datetime.now() - st
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Cool. Keep going!")
print (" ")
ans = input ("What is the top color of the rainbow? ")
while ans.upper() != "RED" and lives > 1:
	lives -= 1
	ans = input("Wrong. Be careful you've only {0} lives. ".format(lives))
if lives <= 1:
	now = datetime.now()
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Right. Keep going!")
print (" ")
ans = int(input ("How many weeks are there in a year? "))
while ans !=52 and lives > 1:
	lives -= 1
	ans = int(input("Wrong. Be careful you've only {0} lives. ".format(lives)))
if lives <= 1:
	now = datetime.now() - st
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Awesome. Keep going!")
print (" ")
ans = input ("Chemical formula of hydrochloric acid: ")
while ans.upper() != "HCL" and lives > 1:
	lives -= 1
	ans = input("Wrong. Be careful you've only {0} lives. ".format(lives))
if lives <= 1:
	now = datetime.now()
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Right. Keep going!")
print (" ")
ans = int(input ("How many players are there in the football team? "))
while ans !=11 and lives > 1:
	lives -= 1
	ans = int(input("Wrong. Be careful you've only {0} lives. ".format(lives)))
if lives <= 1:
	now = datetime.now() - st
	print ("Unfortunately, you lose! Try again.")
	print ("Time: {0}".format(now))
else:
	now = datetime.now() - st
	print (" ")
	print ("You win! Great job!".format(now, lives))