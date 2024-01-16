# write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

# Solution:
x = (60 + (10 ** 2) / 4 * 7) - 134.75  # 100.25
print (x) # 100.25

# answer these 3 questions without typing code. then type code to check your answer.

# What is the value of the expression 4 * (6 + 5) # 44
# What is the value of the expression 4 * 6 + 5 # 29
# What is the value of the expression 4 + 6 * 5 # 34

# What is the type of the result of the expression 3 + 1.5 + 4? # float

# What would you use to find a number’s square root, as well as its square?

# Solution:
# Square root:
print(100 ** 0.5) # 10.0

# Square:
print(10 ** 2) # 100

# Given the string 'hello' give an index command that returns 'e'.

# Solution:
s = 'hello'
print(s[1]) # e

# Reverse the string 'hello' using slicing:

# Solution:
s ='hello'
print(s[::-1]) # olleh

# Given the string hello, give two methods of producing the letter 'o' using indexing.

# Solution:
s ='hello'
print(s[4]) # o
print(s[-1]) # o

# Build this list [0,0,0] two separate ways.

# Solution:
mylist = [0,0,0]
print(mylist) # [0, 0, 0]

mylist = [0]*3
print(mylist) # [0, 0, 0]

# Reassign 'hello' in this nested list to say 'goodbye' instead:

# Solution:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3) # [1, 2, [3, 4, 'goodbye']]

# Sort the list below:

# list4 = [5,3,4,6,1]

# Solution:
#1
list4 = [5,3,4,6,1]
list4.sort()
print(list4) # [1, 3, 4, 5, 6]
#2
list4 = [5,3,4,6,1]
my_sorted_list = sorted(list4)
print(my_sorted_list) # [1, 3, 4, 5, 6]

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}
#Grab 'hello'
print(d['simple_key']) # hello

d = {'k1':{'k2':'hello'}}
#Grab hello
print(d['k1']['k2']) # hello

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello
print(d['k1'][0]['nest_key'][1][0]) # hello

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#Grab hello
print(d['k1'][2]['k2'][1]['tough'][2][0]) # hello


# Can you sort a dictionary? Why or why not?
#anwer: No! Because normal dictionaries are mappings not a sequence.

# What is the major difference between tuples and lists?
#answer: Tuples are immutable.

# How do you create a tuple?
#answer: t = (1,2,3)

# What is unique about a set?
#answer: Sets are unordered collections of unique elements.

# Use a set to find the unique values of the list below:

# list5 = [1,2,2,33,4,4,11,22,3,3,2]

# Solution:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
myset = set(list5) # set
print(myset) # {1, 2, 33, 4, 3, 11, 22}

# What will be the resulting Boolean of the following pieces of code

2 > 3 # False
3 <= 2 # False
3 == 2.0 # False
3.0 == 3 # True
4**0.5 != 2 # False

# Final Question: What is the boolean output of the cell block below?

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
# True or False?
l_one[2][0] >= l_two[2]['k1'] # False
