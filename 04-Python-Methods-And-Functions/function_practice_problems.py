# Lesser of two evens: Write a function that returns the lesser of two given numbers
# if both numbers are even, but returns the greater if one or both numbers are odd


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        # Both numbers are even
        return min(a, b)
    else:
        # One or both numbers are odd
        return max(a, b)

# Example:
result = lesser_of_two_evens(4, 6)
print(result)  # 4

result = lesser_of_two_evens(5, 9)
print(result)  # 9


# Animal Crackers: Write a function that takes a two-word string and returns
# True if both words begin with the same letter

def animal_crackers(text):
 words = text.split()

# Check if the first letters of both words are the same
 return words[0][0].lower() == words[1][0].lower()

# Example:
result = animal_crackers("Lion Leopard")
print(result)  # True

result = animal_crackers("Elephant Tiger")
print(result)  # False


 # Makes twenty: Given two intergers, return True if the sum of the intergers
 # is 20 or if one of the integers is 20. If not, return False

def makes_twenty(number1, number2):
 return number1 + number2 == 20 or number1 == 20 or number2 == 20



#Level 1

#1
#OLD MACDONALD: Write a function that capitaizes the first and fourth
# letters of a name

def old_macdonald(name):
    if len(name) >= 4:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return "Name is too short!"

# Example:
result = old_macdonald("macdonald")
print(result)


#2
#Master Yoda: Given a sentence, return a sentence with words in reversed

def master_yoda(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    return " ".join(reverse_word_list)
