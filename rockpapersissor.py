import random


options = ['rock', 'paper','sissor']

random_pick = random.choices(options)
user1 = input("pick rock,paper or sissor:")


if user1 == random_pick:
	 "draw"
elif user1 == 'paper' and random_pick == "rock":
	print("user1 won")
elif user1 == 'sissor' and random_pick == 'paper':
	print("user1 won")
elif user1 == 'rock' and random_pick == 'sissor':
	print("user1 won")
else:
	print("computer won")


print(f"\nYou chose {user1}, computer chose {random_pick}.\n")

