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


#3
#Almost there: Given an interger n, return True if n is within 10 of
# either 100 or 200

def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)
