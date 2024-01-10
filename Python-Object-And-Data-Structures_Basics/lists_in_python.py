my_list = [1,2,3]
my_list = ['STRING', 100, 23.2]
print (len(my_list))
my_list = ['one', 'two', 'three']
my_list[0]
my_list[1:]
print (my_list)
another_list = ['four', 'five']
my_list + another_list
new_list = my_list + another_list
print (new_list)
new_list[0] = 'ONE ALL CAPS' # This is a method used to change an item in a list.
print (new_list)
new_list.append('six') # This is a method used to add an item to the end of a list.
print (new_list)
new_list.append('seven')
new_list.pop() # This is a method used to remove an item from the end of a list.
print (new_list)
popped_item = new_list.pop()
print (popped_item)
print (new_list)
new_list.pop(0) # This is a method used to remove an item from a specific index position in a list.
print (new_list) # ['two', 'three', 'four', 'five', 'six']

new_list = ['a', 'e', 'x', 'b', 'c']
new_list.sort() # This is a method used to sort a list in alphabetical order.
print (new_list) # ['a', 'b', 'c', 'e', 'x']
my_sorted_list = new_list.sort()
type(my_sorted_list) # <class 'NoneType'>
new_list.sort()
my_sorted_list = new_list
print (my_sorted_list) # ['a', 'b', 'c', 'e', 'x']

num_list = [4,1,8,3]
print (num_list)
num_list.sort() # This is a method used to sort a list in numerical order.
print (num_list)
num_list.reverse() # This is a method used to reverse a list.
print (num_list)
