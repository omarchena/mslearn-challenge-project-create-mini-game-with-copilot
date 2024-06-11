import random
# write 'hello world' to the console
# print('hello world')

# Create a game Rock, Scissors, paper
# the rules are: Rock beats Scissors, Scissors beats Paper, Paper beats Rock
# the game should be played by two players
# The players should be able to input their choice if the choice is not Rock, Scissors or Paper the game should print 'Invalid choice'
# The game should print the winner
# the player two should be the computer
# the computer should randomly select Rock, Scissors or Paper
# the game should print the computer choice
# the game should print the score of the game at the final
# the game should ask the players if they want to play again
# if the player wants to play again the game should reset the score and start again
print('Welcome to Rock, Scissors, Paper game')
player_one = input('Player 1 please enter your choice \nRock, \nScissors, \nPaper: ')
print('Player 2 please enter your choice: \nRock, \nScissors, \nPaper')
player_two = random.choice(['Rock', 'Scissors', 'Paper'])
score = {'player_one': 0, 'player_two': 0}
while True:
    if player_one == player_two:
        print('It\'s a tie')
    elif player_one.lower == 'Rock'.lower and player_two.lower == 'Scissors'.lower:
        print('Player 1 wins')
        score['player_one'] += 1
    elif player_one.lower == 'Scissors'.lower and player_two.lower == 'Paper'.lower:
        print('Player 1 wins')
        score['player_one'] += 1
    elif player_one.lower == 'Paper'.lower and player_two.lower == 'Rock'.lower:
        print('Player 1 wins')
        score['player_one'] += 1
    elif player_two.lower == 'Rock'.lower and player_one.lower == 'Scissors'.lower:
        print('Player 2 wins')
        score['player_two'] += 1
    elif player_two.lower == 'Scissors'.lower and player_one.lower == 'Paper'.lower:
        print('Player 2 wins')
        score['player_two'] += 1
    elif player_two.lower == 'Paper'.lower and player_one.lower == 'Rock'.lower:
        print('Player 2 wins')
        score['player_two'] += 1
    else:
        print('Invalid choice')
    print('Player 1 choice: ', player_one)
    print('Player 2 choice: ', player_two)
    print('Player 1 score: ', score['player_one'])
    print('Player 2 score: ', score['player_two'])
    play_again = input('Do you want to play again? \nYes \nNo')
    if play_again == 'Yes':
        # score['player_one'] = 0
        # score['player_two'] = 0
        player_one = input('Player 1 please enter your choice \nRock, \nScissors, \nPaper: ')
        print('Player 2 please enter your choice: \nRock, \nScissors, \nPaper')
        player_two = random.choice(['Rock', 'Scissors', 'Paper'])
    else:
        break