import random

def main():

    '''
    variables for the computer:

    - create an array that holds the words "Rock" "Paper" "Scissors"
        * this array represents all the possible choices in the game

    - create a variable to store the selection of the computer
        * this will be use to store the string of Rock, Paper or Scissors later

    - create a variable that will store the score of the computer
        * this is a way for us keep track of the number
        of wins the computer has
    '''

    '''
    user variables:

    - create a dictonary that will hold the player options
        the dictionary should hold hold the following keys and values...
        key: 1 value: "Rock"
        key: 2 value: "Paper"
        key: 3 value: "Scissors"

    - create a variable to store the selection of the user and set it to None
        * this will be use to store the string of Rock, Paper or Scissors

    - create a variable to store the score of the user and set it to 0
        * this is a way for us to keep track of the number of wins the
            user / player has
    '''

    # create a variable called is_game_over and set it to false.
    
    # Create a variable that will hold the number of rounds


    while(True):
        
        '''
        create a check to see if the game is over...

        - if the game is over figure out if ther user has a score greater than
            than the computer score, or is the computer score greater than the user score
            or if the user score is equal to the computer score.

        - if the user score is greater, then print out a message that the user
            wins with the score of the user and the computer

        - if the computer score is greater, then print a message that the computer wins
            with the score of the user and the computer

        - if its a tie, print a message with the score of the user and the computer
        '''
        
        '''
        - print out a menu for the user, ask them to make a selection
            and provide a set of options being
            1. Rock, 2. Paper, 3. Scissors
        '''
        

        '''
        - prompt the user to make a selection and assign the result to your 
            user seleciton variable.

            HINT: assume the user will pass in 1, 2 or 3 as input,
            you will need to use the "input" method to take user input, also keep
            in mind that input from the user will come in as a string.
            You will need to convert the string to a number. 

        - use the **user seletion** to grab a value from your **user optoins** dictionary
            and store the result in your **user action** variable.
        '''

        '''
        - generate a random number between 0 and 2, youll want to use random.randint
        to do this. Assign the result to your **computer selection** variable

        - use the **computer selection** variable to get a value from your 
            **computer options** array.
        '''

        '''
        - print a message telling what the user selected
        - print a message telling what the computer selected
        '''

        '''
        - determine the winner of the round
            TIP: use the function determineWinner
            and assign the returned value in a variable.
            
            The function should
            take in your **user action** and **computer action** variables.
        '''

        '''
        - write a set of conditions to check...
            if the user won, if the computer won, or if there is a tie

        - print a message saying if the user won, if the computer won or if its a tie
        '''
        
        # increment your variable that holds the number of **rounds** played by 1
        

        '''
        - check if your the number of rounds played is equal to 3
            if rounds it equal to 3 then change your **is_game_over**
            variable from False to True
        '''

'''
 the function below needs two parameters...
 - your **user action** and **computer action** 
    
    HINT: the value in your **user action** will either be
    Rock, Paper or Scissors, same goes for the **computer action**

ex: def sumTwoNums(num1, num2): num1 and num2 are parameters for the
    sumTwoNums function
'''
def determineWinner(user_action, computer_action):
    '''
    This function is used to determine the winner of a round

    RULES: 
        - Rock beats Scissors
        - Paper beats Rock
        - Scissors beats Paper
        - if both the user and computer have the same action its a tie.
    
    example scenarios:

        user action -> rock
        computer action -> paper
        computer wins
        =========================

        user action -> scissors
        computer action -> paper
        user wins
        =========================

        user action -> paper
        computer actin -> paper
        tie, nobody wins
    '''

    '''
    create a set of checks for all possible winning combinations for the user.
        if the user wins, return the string "user"
    '''
    
    '''
    create a set of checks for all possible winning combinations for the computer
        if the computer wins, return the string "computer"
    '''
    
    '''
    create a set of checks for all possible combinations for a tie.
        if there is a tie, return the string "tie"
    '''


# call the main function
