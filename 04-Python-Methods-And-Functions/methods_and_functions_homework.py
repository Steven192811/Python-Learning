# Functions and methods homework

# Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as:
# 4/3 * pi * radius ** 3

def vol(rad):
    return (4/3) * (3.14) * (rad ** 3)

print(vol(2)) # 33.49333333333333
print(vol(3)) # 113.03999999999999

# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f'{num} is in the range between {low} and {high}')
    else:
        print(f'{num} is not in the range between {low} and {high}')

ran_check(5,2,7) # 5 is in the range between 2 and 7

# If you only wanted to return a boolean:

def ran_bool(num,low,high):
    return num in range(low,high+1)

print(ran_bool(3,1,10)) # True

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'

# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

def up_low(s):
    d = {'upper':0, 'lower':0}
    for char in s:
        if char.isupper():
            d["upper"] += 1
        elif char.islower():
            d['lower'] += 1
        else:
            pass
    print(f'Original String : {s}')
    print(f'No. of Upper case characters : {d["upper"]}')
    print(f'No. of Lower case characters : {d["lower"]}')

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
# Original String : Hello Mr. Rogers, how are you this fine Tuesday?
# No. of Upper case characters : 4
# No. of Lower case characters : 33

# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]

# Unique List : [1, 2, 3, 4, 5]

def unique_list(lst):
    return list(set(lst))


print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5])) # [1, 2, 3, 4, 5]

# Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]

# Expected Output : -24

def multiply(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

print(multiply([1,2,3,-4])) # -24
print(multiply([1,2,3,-4,10])) # -240

# Write a Python function that checks whether a passed in string is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def palindrome(s):
    s = s.replace(' ','') # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1]

print(palindrome('helleh')) # True
print(palindrome('steven')) # False

# Write a Python function to check whether a string is pangram or not.

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.

# For example : "The quick brown fox jumps over the lazy dog"

def ispangram(str1, alphabet=string.ascii_lowercase):
# Create a set of the alphabet
    alphaset = set(alphabet)
# Remove any spaces from the input string
    str1 = str1.replace(' ','')
# Convert into all lowercase
    str1 = str1.lower()
# Grab all unique letters from the string set()
    str1 = set(str1)
# Alphabet set == string set input
    return str1 == alphaset

print(ispangram('The quick brown fox jumps over the lazy dog')) # True
print(ispangram('The quick brown fox jumps over the lazy cat')) # False
