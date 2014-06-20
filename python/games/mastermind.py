# The classic game of Mastermind.
# 
# The computer creates a code of 4 colors.  You have 10 tries
# to guess the code.  The computer gives you hints: first is the number
# of colors you have guessed correctly in each position, and secondly
# the number of colors that you guessed correctly but are in the wrong
# position.
#
# Official rules: 
#    http://www.pressmantoy.com/instructions/instruct_mastermind.html

import random

colors = {
    0 : 'R',  # Red
    1 : 'B',  # Blue
    2 : 'G',  # Green
    3 : 'W',  # White
    4 : 'Y',  # Yellow
    5 : 'O' } # Orange

# Generate the code.
code = []    
for i in range(4):
    code.append(colors[int(random.random() * 6.0)])

# Give the player 10 tries to guess it.
guesses = 0
won = False
while guesses < 10 and not won:
    guess = [x.upper() for x in list(raw_input('Enter your guess:'))][0:4]
    guesses += 1

    # Score their guess.
    red = 0
    white = 0
    counted = [False]*4

    # Look for correct color in correct position.
    # Mark any matches as already counted.
    for i in range(4):
        if guess[i] == code[i]:
            red += 1
            counted[i] = True

    # Look for correct color in wrong position
    # (and not already counted in the right position.
    for i in range(4):
        if code[i] in guess and not counted[i]:
            white += 1

    # Give them their hints.
    print '[', guesses, ']', ''.join(guess), red, white

    # Detect victory, otherwise give them another guess.
    if red == 4:
        print "You win!"
        won = True

# Detect defeat, and tell them how they did.
if guesses == 10 and not won:
    print 'You lose.  The code was ', ''.join(code)
