#Level 1

#1
#OLD MACDONALD: Write a function that capitaizes the first and fourth
# letters of a name

def old_macdonald(name):
    if len(name) >= 4: # if the length of the name is greater than or equal to 4
        return name[:3].capitalize() + name[3:].capitalize() # return the first 3 letters of the name capitalized and the rest of the name capitalized
    else:
        return "Name is too short!"

# Example:
result = old_macdonald("macdonald")
print(result) # MacDonald


#2
#Master Yoda: Given a sentence, return a sentence with words in reversed

def master_yoda(text):
    wordlist = text.split() # split the text into a list of words
    reverse_word_list = wordlist[::-1] # reverse the list of words
    return " ".join(reverse_word_list) # join the list of words into a sentence


#3
#Almost there: Given an interger n, return True if n is within 10 of
# either 100 or 200

def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)
# if the absolute value
#of 100 - n is less than or equal to 10 or the absolute value of 200 - n is less
# than or equal to 10, return True
