import random
print("Number Guessing v.0.1")
print("Getting random number... ", end="")
random_int = random.randrange(0,101)
print("Done!")

counter = 1
while True:
	guess = input("Enter a number: ")
	try:
		guess = int(guess)
		if(guess > random_int):
			print("Too high!")
		elif guess < random_int:
			print("Too low!")
		else:
			print("Correct! Number of tries is: " + str(counter))
			break
	except ValueError:
		print("Please enter a valid integer")
	counter+=1
