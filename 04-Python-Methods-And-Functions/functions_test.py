#1: print Hello World
#Write a function called myfunc that prints the string 'Hello World'

def myfunc():
    print('Hello World')

#2: print Hello Name
#Write a function called myfunc that takes in a name and prints 'Hello Name'

def myfunc(Name):
    print(f'Hello {Name}')

#3: simple boolean
#Write a function called myfunc that takes in a boolean value (True or False).
# If True, return 'Hello', and if False, return 'Goodbye'

def myfunc(boolean):
    if boolean == True:
        return 'Hello'
    else:
        return 'Goodbye'

#4: Using Booleans
#Write a function called myfunc that takes three arguments, x, y, and z.
# If z is True, return x. If z is False, return y.

def myfunc(x,y,z):
    if z == True:
        return x
    else:
        return y


#5: Simple Math
#Write a function called myfunc that takes in two arguments and returns their sum.

def myfunc(x,y):
    return x+y


#6: is_even
#Write a function called is_even that takes in one argument,
# and returns True if the passed-in value is even, False if it is not.

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
