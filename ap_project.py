"Making rock-paper-scissors project"

import random
from re import U
from tracemalloc import stop
import collections
import time

def rock(): #respond with results when computer chooses rock
    if u_choice == 'R':
        round.append('tie')
    elif u_choice == 'P':
        round.append('user')
    else:
        round.append('computer')
def paper(): #respond with results when computer chooses paper
    if u_choice == 'R':
        round.append('computer')
    elif u_choice == 'P':
        round.append('tie')
    else:
        round.append('user')
def scissor(): #respond with results when computer chooses scissor
    if u_choice == 'R':
        round.append('user')
    elif u_choice == 'P':
        round.append('computer')
    else:
        round.append('tie')

round = []

print("Welcome to The Game of Rock, Papers, Scissoers!")
print()
print("You will be playing 3 games with the computer. One with most wins is the winner.")
time.sleep(4)
print()
name = input('Name: ')
c_name = input("Computer's name: ")

count = 1
for i in range(3):
    weapon = ['Rock', 'Paper', 'Scissor']
    u_choice = input(f'{count}. {name}, what do you want to choose? Rock, paper, or scissor? (R,P,S): ')

    computer = random.choice(weapon)

    if computer == 'Rock':
        rock()
        count += 1

    elif computer == 'Paper':
        paper()
        count += 1

    else:
        scissor()
        count += 1

    print(f'{c_name} choose {computer}')
    print()

print(round)

#Finding the who won 2/3 games to determine winner
most = [item for item, count in collections.Counter(round).items() if count > 1] #finds duplicate in list
print()

if most == ['user']:
    print(f'{name} wins!')

elif most == ['computer']:
    print(f'{c_name} wins!')

else:
    print('It is a tie!')

print()
print('Good Game!')