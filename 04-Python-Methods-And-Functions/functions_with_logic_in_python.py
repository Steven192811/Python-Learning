print(2 % 2) # 0
print(3 % 2) # 1
print(41 % 40) # 1
print(20 % 2) # 0
print(20 % 2 == 0) # True
print(21 % 2 == 0) # False

def even_check(number):
  return number % 2 == 0

print(even_check(20)) # True
print(even_check(21)) # False

# Return true if any number is even inside a list

def check_even_list(num_list):
  # return all the even numbers in a list
  # placeholder variables
  even_numbers = [] # empty list
  for number in num_list: # iterate through the list
    if number % 2 == 0: # if number is even
      even_numbers.append(number) # append the number to the list
    else:
      pass # do nothing
  return even_numbers # return the list

print(check_even_list([1,2,3,4,5])) # [2, 4]
