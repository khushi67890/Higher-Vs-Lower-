from art import logo, vs

from game_data import data
import random

A = random.choice(data)
current_score = 0
from replit import clear

game_over = False
while not game_over:
	print(logo)
	print("compare A: " + A['name'] + ", " + A['description'] + ", " +
	      A['country'])
	print(vs)
	B = random.choice(data)
	print("Against B: " + B['name'] + ", " + B['description'] + ", " +
	      B['country'])

	choose = input("Who has more followers? Type 'A' or 'B': ")

	if A['follower_count'] > B['follower_count'] and choose == 'A':
		current_score += 1
		print(f"You are right! Current score: {current_score}")
	elif A['follower_count'] > B['follower_count'] and choose == 'B':
		current_score += 0
		print(f"Sorry, that's wrong. Final score: {current_score}")
		game_over = True
	elif A['follower_count'] < B['follower_count'] and choose == 'B':

		current_score += 1
		print(f"You are right! Current score: {current_score}")
	else:
		current_score += 0
		print(f"Sorry, that'wrong. Final score: {current_score}")
		game_over = True

	A = B
