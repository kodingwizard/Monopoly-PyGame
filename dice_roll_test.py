import random
def diceroll():

	Diceroll = [ ]
	for i in range (1):
		N = random.randint(1,6)
		A = random.randint(1,6)

		Diceroll.append(N)
		Diceroll.append(A)
	print(Diceroll)
	dice_sum = N + A
	print("You rolled a total of  %s" %dice_sum)
	if dice_sum < 10:
		print("yay no taxes")

	else:
		print("boooo taxes")
diceroll()

