def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square,my_nums): # map() returns a map object which is an iterator that yields items on demand instead of returning a list of items
    print(item) # 1 4 9 16 25

print(list(map(square,my_nums))) # [1, 4, 9, 16, 25]

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy','Eve','Sally']

print(list(map(splicer,names))) # ['EVEN', 'E', 'S']

def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]

print(list(filter(check_even,mynums))) # [2, 4, 6]

for n in filter(check_even,mynums):
    print(n) # 2 4 6


    def square(num):
        result = num**2
        return result

print(list(map(lambda num:num**2,mynums))) # [1, 4, 9, 16, 25, 36]

names = ['Andy','Eve','Sally']

print(list(map(lambda x:x[0],names))) # ['A', 'E', 'S']
