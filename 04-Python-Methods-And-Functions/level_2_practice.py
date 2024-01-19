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
