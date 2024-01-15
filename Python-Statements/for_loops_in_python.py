mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist: # num is a variable name
    print(num) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

for num in mylist:
    # Check for even
    if num % 2 == 0: # % is the modulo operator (remainder)
        print(num) # 2, 4, 6, 8, 10
    else:
        print(f'Odd Number: {num}') # Odd Number: 1, Odd Number: 3, Odd Number: 5, Odd Number: 7, Odd Number: 9

list_sum = 0
for num in mylist:
    list_sum = list_sum + num # 0 + 1, 1 + 2, 3 + 3, 6 + 4, 10 + 5, 15 + 6, 21 + 7, 28 + 8, 36 + 9, 45 + 10

print(list_sum) # 55

mystring = 'Hello World'
for letter in mystring:
    print(letter) # H, e, l, l, o, , W, o, r, l, d

tup = (1,2,3) # tuple unpacking
for item in tup:
    print(item) # 1, 2, 3

mylist = [(1,2),(3,4),(5,6),(7,8)] # tuple unpacking
len(mylist) # 4 items in mylist (4 tuples)
for (a,b) in mylist: # tuple unpacking
    print(a) # 1, 3, 5, 7
    print(b) # 2, 4, 6, 8

mylist = [(1,2,3),(5,6,7),(8,9,10)] # tuple unpacking
for a,b,c in mylist: # tuple unpacking
    print(b) # 2, 6, 9

d = {'k1':1,'k2':2,'k3':3} # dictionary unpacking
for item in d.items(): # dictionary unpacking
    print(item) # ('k1', 1), ('k2', 2), ('k3', 3)

for key,value in d.items(): # dictionary unpacking
    print(value) # 1, 2, 3
    
