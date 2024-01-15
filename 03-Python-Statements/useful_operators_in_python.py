mylist = [1,2,3]
for num in range(10):
    print(num) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

for num in range(3,10):
    print(num) # 3, 4, 5, 6, 7, 8, 9

for num in range(0,10,2):
    print(num) # 0, 2, 4, 6, 8

list(range(0,11,2)) # [0, 2, 4, 6, 8, 10]
print(list(range(0,11,2))) # [0, 2, 4, 6, 8, 10]

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    # At index 0 the letter is a, At index 1 the letter is b,
    # At index 2 the letter is c, At index 3 the letter is d,
    # At index 4 the letter is e
    index_count += 1 # index_count = index_count + 1 (increment index_count by 1)

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count]) # a, b, c, d, e
    index_count += 1 # index_count = index_count + 1 (increment index_count by 1)

word = 'abcde'
for item in enumerate(word): # enumerate() returns a tuple (index,letter)
    print(item) # (0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')

word = 'abcde'
for index,letter in enumerate(word): # tuple unpacking
    print(index) # 0, 1, 2, 3, 4
    print(letter) # a, b, c, d, e
    print('\n') # \n, \n, \n, \n, \n

# zip() function (zip together two or more lists) (zip() returns a tuple) (zip() stops at the shortest list)
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

for item in zip(mylist1,mylist2,mylist3): # zip() returns a tuple (item1,item2,item3)
    print(item) # (1, 'a', 100), (2, 'b', 200), (3, 'c', 300)

for item in zip(mylist1,mylist2): # zip() returns a tuple (item1,item2)
    print(item) # (1, 'a'), (2, 'b'), (3, 'c')

# in operator (boolean) (in operator checks if an item is in a list) (in operator checks if a key is in a dictionary)
'x' in [1,2,3] # False
2 in [1,2,3] # True
'x' in ['x','y','z'] # True
"a" in "a world" # True
"mykey" in {"mykey":345} # True

d = {"mykey":345}
345 in d.values() # True
345 in d.keys() # False

# min() and max() functions (min() returns the minimum value) (max() returns the maximum value)
mylist = [10,20,30,40,100]
min(mylist) # 10
max(mylist) # 100

# random library (shuffle() function) (randint() function)
from random import shuffle # import shuffle() function from random library
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist) # shuffle() function shuffles the list
print(mylist) # [2, 5, 6, 7, 1, 4, 9, 3, 10, 8]

from random import randint # import randint() function from random library (randint() function returns a random integer)
randint(0,100) # 0 to 100 (inclusive)
mynum = randint(0,10) # 0 to 10 (inclusive)
print(mynum) # 7

# input() function (input() function takes in a user input)
input('Enter a number here: ') # Enter a number here: 50
result = input('What is your name? ') # What is your name? Steven
print(result) # Steven

result = input('Favorite Number: ') # Favorite Number: 30
type(result) # <class 'str'>
float(result) # 30.0
int(result) # 30

result = int(input('Favorite Number: ')) # Favorite Number: 20
type(result) # <class 'int'>
