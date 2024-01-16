mystring = "hello"
mylist = []
for letter in mystring: # for loop
    mylist.append(letter) # append to list
print(mylist) # print list

mylist = [letter for letter in mystring] # list comprehension
print (mylist) # ['h', 'e', 'l', 'l', 'o']

mylist = [x for x in 'word'] # list comprehension
print(mylist) # ['w', 'o', 'r', 'd']

mylist = [num for num in range(0,11)] # range of numbers
print(mylist) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mylist = [num**2 for num in range(0,11)] # square of numbers
print(mylist) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

mylist = [x for x in range(0,11) if x%2==0] # even numbers
print(mylist) #[0, 2, 4, 6, 8, 10]

mylist = [x**2 for x in range(0,11) if x%2==0] # square of even numbers
print(mylist) #[0, 4, 16, 36, 64, 100]

celcius = [0,10,20,34.5] # celcius  to fahrenheit
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit) #[32.0, 50.0, 68.0, 94.1]

fahrenheit = [] # celcius  to fahrenheit
for temp in celcius: # for loop
    fahrenheit.append(((9/5)*temp + 32)) # append to list
print(fahrenheit) #[32.0, 50.0, 68.0, 94.1]

results = [x if x%2==0 else 'ODD' for x in range(0,11)] # if else
print(results) #[0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]

mylist = [] # nested loop
for x in [2,4,6]: # for loop
    for y in [100,200,300]: # for loop
        mylist.append(x*y) # append to list
print(mylist) #[200, 400, 600, 400, 800, 1200, 600, 1200, 1800]

mylist = [x*y for x in [2,4,6] for y in [1,10,1000]] # nested list comprehension
print(mylist) #[2, 20, 2000, 4, 40, 4000, 6, 60, 6000]

