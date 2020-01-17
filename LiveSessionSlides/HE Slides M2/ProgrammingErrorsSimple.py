#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MODULE 2
PRACTICE USING PYTHON FUNCTIONS AND CONDITIONAL STATEMENTS
PRACTICAL APPLICATIONS:
    WORKING WITH STRINGS
    MAKING CALCULATIONS WITH LESS USED OPERATORS
    PRINTING UPDATES
    CONSIDERING HOW TO STOP A FUNCTION
    CONSIDERING HOW TO SIMPLIFY CODE
"""

########## BASIC TASKS THAT HAVE ERRORS THAT STUDENTS NEED TO CORRECT #########
#%% Get names from users
# Error: inconsistent naming convention (not as much of an error as a style problem).
# Error: misspelling of a variable
firstName = input('What is your first name?\n')
last_name = input('What is your last name?\n')

print('Hello ' + lastname)
# Replace firstname with firstName
# Replace last_name and lastname with lastName and then move on
#%% Function to combine first and last name
# Error: uses print instead of return
# Error: The order of the names when the function is called
def combine_names(fn, ln):
    fullName = fn + ' ' + ln
    print(fullName)
    
fullName = combine_names(lastName, firstName)
print('Your full name is ' + fullName)
# Replace print in the function with return
# Either replace lastName with ln = lastName and firstName with fn = firstName, or
# Change the order of firstName and lastName
#%% Add documention to the combine_names function using a doc string so that the user of the function can see what it does
# Error: incorrect way to add documentation for the user of the function
# Error: incorrect white space
def combine_names(fn, ln):
    # This function combines the first and last name.
   fullName = fn + ' ' + ln
    return(fullName)
help(combine_names)
# Replace the # with ''' and then put ''' after the documentation.
# Make sure that all lines of the function are indented four spaces.
#%% Count the number of characters in fullName and determine if it's odd or even
# Error: Uses division operator instead of modulus operator
# Uses assignment instead of evaluation
fnLength = len(fullName)
if fnLength/2 = 0:
    print('Even number of characters')
else:
    print('Odd number of characters')
# Replace fnLength/2 with fnLength%2
# Replace = with ==
#%% Calculate the integer and the remainder of the length of characters
# Error: Uses wrong operators
lfn = len(firstName) + 142
lln = len(lastName) + 100
print(str(lfn) + ' divided by ' + str(lln) + ' is equal to ' + str(lfn / lln) + \
      ' with a remainder of ' + str(lfn ** lln) + '. Wow! That is super cool!' )
# Replace / with // to convert it from division to integer division operator
# Replace ** to % to convert it from raising to a power to the modulus operator
#%% Create a function to combine names and calculate the number of characters.
# Error: Global variable vs local variable
# Error: Incorrect way to assign multiple variables
lengthFullName = str(len(fullName)+1000)
def combine_names(fn, ln):
    '''
    This function combines the first and last name and returns a statement \
    indicating the number of characters in the full name.
    '''
    fullName = fn + ' ' + ln
    statement = 'Your full name has ' + lengthFullName + \
    ' characters, including white spaces.'
    return(fullName, statement)
fname s = combine_names(firstName, lastName)
fname
s
# Replace lengthFullName in the function with str(len(fullName))
# Insert a comma between the fname and the s
#%% Create a function that allows you to guess a random number
import random
# Error: conditional statement error
# Error: Lots of repetitive code
# Error: Function continues until the end even when the correct number is guessed.

def guess_number(lowestNum = 1, highestNum = 10):
    '''
    This function creates a random integer between 1 and 100
    , or whatever other bound you set, 
    and then gives you 5 chances to guess what it is.
    '''
    rn = random.randint(lowestNum, highestNum)
    guess1 = int(input('Take your first guess.\n'))
    if guess1 == rn:
        print('You guessed it on your first try. Kudos!')
    elif guess1 > rn
        print('Your first guess is too high. ')
    else:
        print('Your first guess is too low. ')
    
    guess2 = int(input('Take your second guess.\n'))
    if guess2 == rn:
        print('You guessed it on your second try. Kudos!')
    elif guess2 > rn
        print('Your second guess is too high. ')
    else:
        print('Your second guess is too low. ')
            
    guess3 = int(input('Take your third guess.\n'))
    if guess3 == rn:
        print('You guessed it on your third try. Kudos!')
    elif guess3 > rn
        print('Your third guess is too high. ')
    else:
        print('Your third guess is too low. ')   
         
    guess4 = int(input('Take your fourth guess.\n'))
    if guess4 == rn
        print('You guessed it on your fourth try. Kudos!')
    elif guess4 > rn
        print('Your fourth guess is too high. ')
    else:
        print('Your fourth guess is too low. ')
         
    guess5 = int(input('Take your fifth and final guess.\n'))
    if guess5 == rn
        print('You guessed it on your fifth try. Kudos!')
    elif guess5 > rn
        print('Your fifth guess is too high. ')
    else:
        print('Your fifth guess is too low. ')
    print('The number was ' + str(rn) + ' Time is up :(')
 # Add a colon after the if, elif, and else lines.
# Add a return after the line where the number is guessed, or nest the if statements as below.   
#%% Nested if statements
import random
def guess_number(lowestNum = 1, highestNum = 10):
    '''
    This function creates a random integer between 1 and 100
    , or whatever other bound you set, 
    and then gives you 5 chances to guess what it is.
    '''
    rn = random.randint(lowestNum, highestNum)
    guess1 = int(input('Take your first guess.\n'))
    if guess1 == rn:
        print('You guessed it on your first try. Kudos!')
    else:
        if guess1 > rn:
            print('Your guess is too high.')
        else:
            print('Your guess is too low.')
        guess2 = int(input('Take your second guess.\n'))
        if guess2 == rn:
            print('You guessed it on your second try. Kudos!')
        else:
            if guess2 > rn:
                print('Your guess is too high.')
            else:
                print('Your guess is too low.')
            guess3 = int(input('Take your third guess.\n'))
            if guess3 == rn:
                print('You guessed it on your third try. Nice job.')
            else:
                if guess3 > rn:
                    print('Your guess is too high.')
                else:
                    print('Your guess is too low.')
                guess4 = int(input('Take your fourth guess.\n'))
                if guess4 == rn:
                    print('You guessed it on your fourth try. Nice job.')
                else:
                    if guess4 > rn:
                        print('Your guess is too high.')
                    else:
                        print('Your guess is too low.')
                    guess5 = int(input('Take your fifth and final guess.\n'))
                    if guess5 == rn:
                        print('You guessed it on your fifth try. You barely got it!')
                    else:
                        if guess5 > rn:
                            print('Your guess is too high.')
                        else:
                            print('Your guess is too low.')
                        print('The number was ' + str(rn) + '. Time is up :(')
#%% More efficient approach is to create variables and multiple functions
# This introduces a for loop, which they haven't seen, but the key is to show a function called within another function.
import random
def high_low_equal(rn, guess):
    if guess == rn:
        print('You guessed it. Kudos!')
    elif guess > rn:
        print('Your guess is too high.')
    else:
        print('Your guess is too low.')
    return guess - rn
def guess_number(lowestNum = 1, highestNum = 10):
    rn = random.randint(lowestNum, highestNum)
    attemptLabels = ['first', 'second', 'third', 'fourth', 'fifth']
    for attempt in attemptLabels:
        userGuess = int(input('Take your ' + attempt + ' guess.\n'))
        thisDiff = high_low_equal(rn, userGuess)
        if thisDiff == 0:
            break

# End by indicating that they'll be learning more about lists and loops next time.
# Also end by asking what would happen if a lot of code depended on the high_low_equal function,
# and we wanted to make a change to it. It could break the other functions
# that depend on it
        