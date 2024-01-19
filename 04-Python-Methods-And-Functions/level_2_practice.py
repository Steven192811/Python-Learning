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
