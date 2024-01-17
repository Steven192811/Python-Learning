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


#7: is_greater
#Write a function called is_greater that takes in two arguments,
# and returns True if the first value is greater than the second,
# False if it is less than or equal to the second.

def is_greater(x,y):
    if x > y:
        return True
    else:
        return False

#8: *args
#Write a function called myfunc that takes in an arbitrary number of arguments,
# and returns the sum of those arguments.

def myfunc(*args):
    return sum(args)


#9: pick evens
#Write a function called myfunc that takes in an arbitrary number of arguments,
# and returns a list containing only those arguments that are even.

def myfunc(*args):
    mylist = []
    for num in args: # iterate through the tuple
        if num % 2 == 0: # if number is even
            mylist.append(num) # append/add the number to the list
    return mylist
