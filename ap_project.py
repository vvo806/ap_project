"Making rock-paper-scissors project"

import random
import time

# Defines the winner into a list after comparing user's and computer's weapon
def results(x):
    # Respond with results when computer chooses rock
    if x == 'Rock': 
        if u_choice == 'R':
            rounds.append('tie')
        elif u_choice == 'P':
            rounds.append('user')
        else:
            rounds.append('computer')

    # Respond with results when computer chooses paper
    elif x == 'Paper': 
        if u_choice == 'R':
            rounds.append('computer')
        elif u_choice == 'P':
            rounds.append('tie')
        else:
            rounds.append('user')

    # Respond with results when computer chooses scissor
    else: 
        if u_choice == 'R':
            rounds.append('user')
        elif u_choice == 'P':
            rounds.append('computer')
        else:
            rounds.append('tie')

# List of winners per round
rounds = []

# Introductions
print("Welcome to The Game of Rock, Papers, Scissors!")
print()
print("You will be playing as many rounds as you like with the computer. One with most wins is the winner.")
time.sleep(3)
print()
name = input('Name: ')
c_name = input("Computer's name: ")

# To count the rounds of the game
count = 1

# Playing rounds
weapon = ['Rock', 'Paper', 'Scissor']
num = int(input("How many rounds would you like to play: "))
for i in range(num):
    u_choice = input(f'{count}. {name}, what do you want to choose? Rock, paper, or scissor? (R,P,S): ')

    # Computer chooses random weapon
    computer = random.choice(weapon)

    # Calling result function when the random weapo is chosen
    if computer == 'Rock':
        results('Rock')
        count += 1

    elif computer == 'Paper':
        results('Paper')
        count += 1

    else:
        results('Scissor')
        count += 1
    
    # Printing what the computer chose
    print(f'{c_name} choose {computer}')
    print()

print(rounds)

# Counting number of times a word has been appended in the list
u = rounds.count('user')
c = rounds.count('computer')
t = rounds.count('tie')

# Finding who won the most games to determine winner
if u > c and t < u:
    print(f"{name} wins!")
elif c > u and t < c:
    print(f"{c_name} wins!")
else:
    print("It is a tie!")

# Ending game with respects
print()
print("Good Game!")