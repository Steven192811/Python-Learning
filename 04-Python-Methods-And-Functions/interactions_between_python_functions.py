example = [1, 2, 3, 4, 5, 6, 7]

from random import shuffle

result = shuffle(example)
print(example)  # [4, 2, 6, 5, 7, 3, 1]

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example) # It's calling the function and passing in the list
print(result) # [2, 4, 5, 1, 3, 7, 6]

mylist = ['', 'O', '']
shuffle_list(mylist)
print(mylist) # ['', '', 'O']

def player_guess():
    guess = '' # placeholder variable

    while guess not in ['0', '1', '2']: # while guess is not in the list
        guess = input('Pick a number: 0, 1, or 2: ') # input always returns a string

    return int(guess) # return the integer version of guess

player_guess() # Pick a number: 0, 1, or 2: 1

myindex = player_guess() # Pick a number: 0, 1, or 2: 1
print(myindex) # 1

def check_guess(mylist, guess):
    if mylist[guess] == 'O': # if the guess is correct
        print('Correct!') # print 'Correct!'
    else:
        print('Wrong guess!') # print 'Wrong guess!'
        print(mylist) # print the list

        #SUDO CODE + CONNECTING ALL THE FUNCTIONS
        #Initial list
        mylist = ['', 'O', '']
        #Shuffle list
        mixedup_list = shuffle_list(mylist)
        #User guess
        guess = player_guess()
        #Check guess
        check_guess(mixedup_list, guess)

        # OUTPUT:
        # Pick a number: 0, 1, or 2: 1 # User input
        # 5
        # Wrong guess!
        # ['', '', 'O']
        # Pick a number: 0, 1, or 2: 1 # User input
        # 1
        # Correct!
