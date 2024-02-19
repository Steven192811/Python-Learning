print("hello")

def func():
    print("FUNC() in first.py")

print ("TOP LEVEL in first.py")

if __name__ == "__main__": # if this file is being run directly
    print("first.py is being run directly")
else:
    print("first.py has been imported")
