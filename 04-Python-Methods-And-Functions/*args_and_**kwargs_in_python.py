def myfunc(a,b,c=0,d=0,e=0):
    # Returns 5% of the sum of a and b
    return sum((a,b)) * 0.05

result = myfunc(40,60,100,100,34)

def myfunc(*args): # args is a tuple of arguments
    return sum(args) * 0.05

result = myfunc(40,60,100,100,34)

def myfunc(*args): # args is a tuple of arguments
    for item in args: # iterate through the tuple
        print(item)

myfunc(40,60,100,1,34) # 40 60 100 1 34


def myfunc(**kwargs): # kwargs is a dictionary of arguments
    if 'fruit' in kwargs: # if 'fruit' is a key in kwargs
        print('My fruit of choice is {}'.format(kwargs['fruit'])) # print the value of 'fruit' in kwargs
    else:
        print('I did not find any fruit here')

myfunc(fruit='apple') # My fruit of choice is apple
myfunc(fruit='apple',veggie='lettuce') # My fruit of choice is apple


def myfunc(*args,**kwargs): # args is a tuple of arguments, kwargs is a dictionary of arguments
    print(args) # tuple of arguments
    print(kwargs) # dictionary of arguments
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30,fruit='orange',food='eggs',animal='dog') # I would like 10 eggs
