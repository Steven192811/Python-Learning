x =  25

def printer():
    x = 50
    return x

print(x) # 25
print(printer()) # 50

# LEGB Rule:
# L: Local - Names assigned in any way within a function (def or lambda), and not declared global in that function
# E: Enclosing function locals - Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer
# G: Global (module) - Names assigned at the top-level of a module file, or declared global in a def within the file
# B: Built-in (Python) - Names preassigned in the built-in names module: open, range, SyntaxError, etc

# lambda num:num**2

name = 'THIS IS A GLOBAL STRING'

def greet():

    name = 'Steven'

    def hello():
        name = 'IM A LOCAL'
        print('Hello '+name)

    hello() # Hello Steven # Hello IM a LOCAL

greet() # Hello Steven

print(name) # THIS IS A GLOBAL STRING

name = 'THIS IS A GLOBAL STRING'

def greet():

    # name = 'Steven'

    def hello():
        print('Hello '+name)

    hello() # Hello THIS IS A GLOBAL STRING

greet() # Hello THIS IS A GLOBAL STRING

x = 50

def func(x):
    print(f'X is {x}')

    # Local reassignment on a global variable
    x = "new value"
    print(f'I just locally changed X global x to {x}')
    return x

print(x) # 50
