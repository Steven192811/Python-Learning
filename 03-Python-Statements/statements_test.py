# Use for , .split(), and if to create a Statement that will print out words that start with 's':
# st = 'Print only the words that start with s in this sentence'

# Solution:
st = 'Print only the words that start with s in this sentence'
for word in st.split(): # for loop
    if word[0].lower == 's': # if statement
        print(word) # print word that starts with s

# Use range() to print all the even numbers from 0 to 10.

# Solution:
for num in range(0,11,2): # for loop
    if num%2 == 0: # if statement
        print(num) # print even numbers from 0 to 10

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

# Solution:
mylist = [num for num in range(1,51) if num%3 == 0] # list comprehension
print(mylist) # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

# Go through the string below and if the length of a word is even print "even!"

# Solution:
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split(): # for loop
    if len(word)%2 == 0: # if statement
        print(word +" <-- has an even length!") # print even length words

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# Solution:
for num in range(1,101): # for loop
    if num%3 == 0 and num%5 == 0: # if statement
        print('FizzBuzz') # print FizzBuzz
    elif num%3 == 0: # elif statement
        print('Fizz') # print Fizz
    elif num%5 == 0: # elif statement
        print('Buzz') # print Buzz
    else: # else statement
        print(num) # print number

# Use List Comprehension to create a list of the first letters of every word in the string below:

# Solution:
st = 'Create a list of the first letters of every word in this string'
mylist = [word[0] for word in st.split()] # list comprehension
print(mylist) # ['C', 'a', 'l', 'o', 't', 'f', 'l', 'o', 'e', 'w', 'i', 't', 's']
