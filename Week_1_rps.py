import random

# Define the possble choices
choices = ['rock', 'paper', 'scissors']

# Get user's choice, strip added to remove spacing and lower added to decapitalize the user's input
user_choice = input('Enter your choice (rock, paper or scissors): ').strip().lower()

# incase user chooses another option, f allows me to insert variables into strings and exit stops the program immediately
if user_choice not in choices:
    print(f'Your choice {user_choice} is invalid, choose between {choices}')
    exit()

# get computer choice
computer_choice = random.choice(choices)
print(f'computer chose {computer_choice}')

# determine the winner 
def get_winner(user, computer):
    if user == computer:
        return 'It is a tie'
    wins = {
        'rock' : 'scissors', # rock crushes scissors
        'paper' : 'rock', # paper swallows rock
        'scissors' : 'paper' # scissors cuts paper
    }
    if wins[user] == computer:  
        return 'You Win!'
    else:
        return 'Computer Wins!'

# announce winner
result = get_winner(user_choice, computer_choice)
print(result, 'best of 3?') 

