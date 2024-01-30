# Functions and methods homework

# Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as:
# 4/3 * pi * radius ** 3

def vol(rad):
    return (4/3) * (3.14) * (rad ** 3)

print(vol(2)) # 33.49333333333333
print(vol(3)) # 113.03999999999999

# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f'{num} is in the range between {low} and {high}')
    else:
        print(f'{num} is not in the range between {low} and {high}')

ran_check(5,2,7) # 5 is in the range between 2 and 7

# If you only wanted to return a boolean:

def ran_bool(num,low,high):
    return num in range(low,high+1)

print(ran_bool(3,1,10)) # True

