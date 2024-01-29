# SPY GAME: Write a function that takes in a list of integers and returns
# True if it contains 007 in order

def spy_game(nums):
    code = [0,0,7,'x'] # create a code list
    for num in nums: # for every number in the nums list
        if num == code[0]: # if the number is equal to the first number in the code list
            code.pop(0) # remove the first number in the code list
    return len(code) == 1 # return True if the length of the code list is 1
