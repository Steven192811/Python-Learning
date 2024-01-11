t = (1,2,3) # tuple is immutable and uses parenthesis instead of square brackets like list
mylist = [1,2,3] # list is mutable and uses square brackets instead of parenthesis like tuple

print(type(t)) # <class 'tuple'>
print(type(mylist)) # <class 'list'>
print(len(t)) # 3
print(len(mylist)) # 3
t = ('one',2) # tuple can have different data types
print(t) # ('one', 2)
print(t[0]) # one
print(t[-1]) # 2
t = ('a','a','b') # tuple can have duplicate values
print(t.count('a')) # 2
print(t.index('a')) # 0
print(t.index('b')) # 2
t[0] = 'NEW' # TypeError: 'tuple' object does not support item assignment

mylist[0] = 'NEW' # list is mutable
print(mylist) # ['NEW', 2, 3]
