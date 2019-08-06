"""
This is educational code for a 2 player game that looks at who has the highest dice roll. Each player must roll a die
five times and have that total saved to a dictionary. Then we need to repeat that procedure 10 times over. After that,
we must go through our dictionary and see who won each roll!
Python 3.6

"""
player_one_roll_totals = {}  # Holds our totals for player 1
player_two_roll_totals = {}  # Holds our totals for player 2

import random

playerOne = input('What is player 1\'s name?')  # We take in our players names here
playerTwo = input('What is player 2\'s name?')

print('Welcome to the game ' + playerOne + ' and ' + playerTwo)  # Greeting message...just because

counter = 0  # see below
# We set a variable called counter, which will be used to control our 'while' loop we're about to run
# if no variable was set, then the code would run without pause as there would be no escape condition to make the
# while loop false.
# The while loop below is the ten times that we need to repeat rolling 5 dice
while counter < 10:  # here we tell the computer to check and if counter is less than 10 if so, then loop again
    new_key = counter + 1  # This could be thought of as which round we're on. It also plays a role later in dynamically
    # adding the round to our dictionary key names.

    """
    Okay, so, we're already in a loop at this point in the code because we need to repeat the same procedure 10 times. 
    However, we now need to have what you might call a sub-procedure. That is to say, we need to roll a die 5 times 
    first. So we have a loop within a loop. This is known as a nested loop. 
    
    Alright, below we're starting our nested loops! So, per our instructions, we need to roll a single dice 5 times. 
    the code below is mini loop for player one to roll their dice 5 times. The playerOneCounter is a way of keeping
    track how many times the loop has gone through. We want to go  through 5 times. So, this code starting at 
    'while playerOnecounter < 5:' starts by rolling a random number between 1 and 6 it then adds that number to 
    'playerOneTotal' so, after five rounds you have the sum of all five roles. Notice again the playerOneCounter, which
    adds one each time we go around to ensure we stop at 5. 
    """
    playerOneCounter = 0  # How many times player 1 has rolled the dice
    playerOneTotal = 0  # The total of the dice
    while playerOneCounter < 5:  # Once we roll 5 times this wont run anymore
        playerOneRoll = random.randint(1, 6)  # Generates a random number between 1-6
        playerOneTotal += playerOneRoll  # Adds whatever number is randomly generated to playerOneTotal
        playerOneCounter += 1  # Adds one to show we've rolled the dice one more time

    """
    At this point in the code, we've shaken the dice 5 times. Our total is captured in playerOneTotal. That number is 
    then appended to our dictionary called player_one_roll_totals. The key of the dictionary is the roll number, which 
    is created by adding the  word roll to 'new_key' which is our counter number. The value is playerOneTotal. They are 
    now saved in the dictionary for later.
    """
    new_key_creation = 'roll ' + str(new_key)  # Adds the word roll to how many times we've gone through the loop
    player_one_roll_totals[new_key_creation] = playerOneTotal  # Adds our data to the dictionary

    """
    At this point, we do  the same thing we did for player one, but for player two. The code is identical in logic. The
    only difference is that this data gets saved to the dictionary player_two_roll_totals. I'm not going to comment
    on each part as it's truly the same process again just with different names. 
    
    """

    playerTwoCounter = 0
    playerTwoTotal = 0
    while playerTwoCounter < 5:
        playerTwoRoll = random.randint(1, 6)
        playerTwoTotal += playerTwoRoll
        playerTwoCounter += 1

    new_key_creation = 'roll ' + str(new_key)
    player_two_roll_totals[new_key_creation] = playerTwoTotal

    """
    At this point we've rolled the dice for each player 1 time. The counter below adds 1 to our counter. We now go back
    to the top and repeat this whole thing over again because we need to run it ten times per our instructions. 
    """
    counter += 1



"""
So, here we are, we've run the previous loop 10 times with our mini loops running to roll for each player. We now have
two dictionaries loaded with data and ready to be compared. Below, prints off all the numbers in each dictionary for 
each player. 

"""
print('Player 1 final totals:')
result_player_one = "".join(' ' + str(value) for key, value in player_one_roll_totals.items())
print(result_player_one)
print('Player 2 final totals:')
result_player_two = "".join(' ' + str(value) for key, value in player_two_roll_totals.items())
print(result_player_two)

"""
I know below looks really, really dicey. It's not as bad as it looks though. So, here's what's happening in plain 
English. We have two dictionaries and we need to go through both of them. The first two lines are essentially the same
thing. It says for keys, values in player_one_roll_totals and for keys, values in player_two_roll_totals
which is basically telling  the computer to go through the data we've saved at this point.  Next, we tell the computer
to compare the roll numbers. In other words, we want to make sure that we're comparing the proper numbers together. Like
player 1s first roll to player 2s first roll and not to player 2s last roll. The computer first looks at player ones
dictionary and says 'okay roll 1' then it looks at player 2s dictionary and says ' roll 1' it then compares the values
to see which is greater. It then prints off the roll number that was compared and who the victor was! The computer
compares each piece of data that way. Until it runs out thus letting us know who's won each round!

"""

for player_one_roll_number, player_one_roll_value in player_one_roll_totals.items():
    for player_two_roll_number, player_two_roll_value in player_two_roll_totals.items():
        if player_one_roll_number == player_two_roll_number:
            if player_one_roll_value > player_two_roll_value:
                print(str(player_one_roll_number) + ' Player 1 is the Winner!')
            elif player_two_roll_value > player_one_roll_value:
                print(str(player_two_roll_number) + ' Player 2 is the Winner!')
            else:
                print("It's a tie!")



"""
To help you see what we end up with. The two print statements below will print off the whole dictionaries once they're 
completed. This will show you how we built our data. I know this whole thing seems overwhelming, but I assure you that
it's just a lot of noise. There's really only a few key principals at play:

1) Loops - We have a main loop and nested loops. This is where most people's heads will spin. It's hard to grasp having
one process cycling then starting a sub-process. Imagine it like this though. You're bagging groceries. First you fill
up a bag, then you load that bag into your cart. You then repeat the process of filling a bag until it is full. You then
add it to your cart. This is the essence of loops. 

2) Iteration - Iteration is a key word anytime you're going through anything in programming. It doesn't matter what data
type you're dealing with. If you need to go through it, then you're iterating. Imagine the shopping metaphor again. 
Say you've finished packing your groceries in your cart, but then realize you put your money in one of the bags! Oh, the
horror! You will now need to iterate through the cart and through the  bags. You start by grabbing one bag, then you
iterate through the items. Then you go on to  the next bag until you've completed the task 

That's more or less what we're doing with our dictionaries, but with a few more comparisons. 


"""
print(player_one_roll_totals)
print(player_two_roll_totals)











