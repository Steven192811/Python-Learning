myset = set()
print (myset) # set()
myset.add(1)
print (myset) # {1}
myset.add(2) # set is unordered
print (myset) # {1, 2}
myset.add(2) # set cannot have duplicate values
print (myset) # {1, 2} # no change
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3] # list can have duplicate values
print(set(mylist)) # {1, 2, 3} # set can be used to get unique values from a list
