# Level 2

#1
# Given a list of ints, return True if the array contains a 3 next to a 3
# somewhere


def has_33(nums):

 for i in range (0,lens(nums)-1): # range goes from 0 to length of nums -1
    if nums[i] == 3 and nums[i+1] == 3: # if the current number is 3 and the next number is 3
        return True

 return False


#2
# Paper Doll: Given a string, return a string where for every character in the
# original there are three characters

def paper_doll(text):
    result = '' # create an empty string
    for char in text: # for every character in the text string
        result += char * 3 # add the character 3 times to the result string
    return result


#3
# Blackjack: Given three integers between 1 and 11, if their sum is less than
# or equal to 21, return their sum. If their sum exceeds 21 and there's an
# eleven, reduce the total sum by 10. Finally, if the sum (even after
# adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
    if sum((a,b,c)) <= 21: # if the sum of a, b, and c is less than or equal to 21
        return sum((a,b,c)) # return the sum of a, b, and c
    elif sum((a,b,c)) <= 31 and 11 in (a,b,c): # if the sum of a, b, and c is less than or equal to 31 and 11 is in a, b, or c
        return sum((a,b,c)) - 10 # return the sum of a, b, and c minus 10
    else:
        return 'BUST' # return 'BUST'


#4
# Summer of '69: Return the sum of the numbers in the array, except ignore
# sections of numbers starting with a 6 and extending to the next 9 (every 6
# will be followed by at least one 9). Return 0 for no numbers

def summer_69(arr):
    total = 0 # create a total variable and set it equal to 0
    add = True # create an add variable and set it equal to True

    for num in arr: # for every number in the array
        while add: # while add is True
            if num != 6: # if the number is not 6
                total += num # add the number to the total
                break # break out of the while loop
            else:
                add = False # set add equal to False
        while not add: # while add is False
            if num != 9: # if the number is not 9
                break # break out of the while loop
            else:
                add = True # set add equal to True
                break # break out of the while loop
    return total # return the total
