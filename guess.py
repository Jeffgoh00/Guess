import random
start = int (input ("Please decide start of the answer range: "))
end = int (input ("Please decide end of the answer range: "))


r = random.randint(1, 100)
count = 0

while True:
	count += 1 # count = count + 1
	num = int (input ("Guess Number: "))
	if num == r:
		print ("You guess right!")
		print ("You have guess", count, "time")
		break
	elif num > r:
		print ("Big than number ")
	elif num < r:
		print ("Small than number")
	print ("You have guess", count, "time")