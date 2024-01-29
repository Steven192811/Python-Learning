# SPY GAME: Write a function that takes in a list of integers and returns
# True if it contains 007 in order

def spy_game(nums):
    code = [0,0,7,'x'] # create a code list
    for num in nums: # for every number in the nums list
        if num == code[0]: # if the number is equal to the first number in the code list
            code.pop(0) # remove the first number in the code list
    return len(code) == 1 # return True if the length of the code list is 1

print (spy_game([1,2,4,0,0,7,5])) # True because 007 is in the list
print (spy_game([1,0,2,4,0,5,7])) # True because 007 is in the list
print (spy_game([1,7,2,0,4,5,0])) # False because 007 is not in the list


# COUNT PRIMES: Write a function that returns the number of prime numbers
# that exist up to and including a given number

def count_primes(num):
    primes = [2] # create a primes list and set it equal to 2
    x = 3 # create an x variable and set it equal to 3
    if num < 2: # if the number is less than 2
        return 0 # return 0
    while x <= num: # while x is less than or equal to the number
        for y in range(3,x,2): # for every number in the range of 3 to x by 2
            if x%y == 0: # if x divided by y has a remainder of 0
                x += 2 # add 2 to x
                break # break out of the for loop
        else:
            primes.append(x) # append x to the primes list
            x += 2 # add 2 to x
    print(primes) # print the primes list
    return len(primes) # return the length of the primes list

print (count_primes(100)) # 25 because there are 25 prime numbers between 0 and 100
print (count_primes(1000)) # 168 because there are 168 prime numbers between 0 and 1000
print (count_primes(10000)) # 1229 because there are 1229 prime numbers between 0 and 10000

