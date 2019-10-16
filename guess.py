import random

r = random.randint(1, 100)
while True:
	num = int (input ("Guess Number: "))
	if num == r:
		print ("You guess right!")
		break
	elif num > r:
		print ("Big than number ")
	elif num < r:
		print ("Small than number")
