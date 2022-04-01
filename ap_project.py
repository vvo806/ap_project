"Making rock-paper-scissors project"

import random
import collections
import time

# Defines the winner into a list after comparing user's and computer's weapon
def results(x):
    # Respond with results when computer chooses rock
    if x == 'Rock': 
        if u_choice == 'R':
            round.append('tie')
        elif u_choice == 'P':
            round.append('user')
        else:
            round.append('computer')

    # Respond with results when computer chooses paper
    if x == 'Paper': 
        if u_choice == 'R':
            round.append('computer')
        elif u_choice == 'P':
            round.append('tie')
        else:
            round.append('user')

    # Respond with results when computer chooses scissor
    if x == 'Scissor': 
        if u_choice == 'R':
            round.append('user')
        elif u_choice == 'P':
            round.append('computer')
        else:
            round.append('tie')

# List of winners per round
round = []

# Introductions
print("Welcome to The Game of Rock, Papers, Scissors!")
print()
print("You will be playing 3 rounds with the computer. One with most wins is the winner.")
time.sleep(3)
print()
name = input('Name: ')
c_name = input("Computer's name: ")

# To count the rounds of the game
count = 1

# Playing 3 rounds
weapon = ['Rock', 'Paper', 'Scissor']
for i in range(3):
    u_choice = input(f'{count}. {name}, what do you want to choose? Rock, paper, or scissor? (R,P,S): ')

    computer = random.choice(weapon)

    rock = 'Rock'
    paper = 'Paper'
    scissor = 'Scissor'

    if computer == rock:
        results('Rock')
        count += 1

    elif computer == paper:
        results('Paper')
        count += 1

    else:
        results(scissor)
        count += 1

    print(f'{c_name} choose {computer}')
    print()

print(round)

# Finding who won at least 2/3 games to determine winner
# Credit for Line 75: 
for item in round:
    u = 'user'
    c = 'computer'
    t = 'tie'
    print(round)
    #if int(item) in round > 1:
     #   print(item)

most = [item for item, count in collections.Counter(round).items() if count > 1] # Finds duplicate in list
print()

# Prints out winner's name
if most == ['user']:
    print(f'{name} wins!')

elif most == ['computer']:
    print(f'{c_name} wins!')

else:
    print('It is a tie!')

print()
print('Good Game!')