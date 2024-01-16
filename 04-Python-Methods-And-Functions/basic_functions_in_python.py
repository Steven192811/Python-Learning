def say_hello():
    print('hello')

say_hello() # hello

def say_hello(name):
    print(f'hello {name}')

say_hello('Steven') # hello Steven

def say_hello(name='Default'):
    print(f'hello {name}')

say_hello() # hello Default

def add_num(num1,num2):
    return num1+num2

result = add_num(10,20)
print(result) # 30

def print_result(a,b):
    print(a+b)

def return_result(a,b):
    return a+b

print_result(10,20) # 30
result = return_result(10,20)
print(result) # 30

def myfunc(a,b):
    print(a+b)
    return a+b

result = myfunc(10,20) # 30
print(result) # 30

def sum_numbers(num1,num2):
    return num1+num2

sum_numbers(10,20) # 30
sum_numbers('10','20') # '1020'
