from _name_and_main_ import first

print ("TOP LEVEL in two.py")

first.func()

if __name__ == "__main__": # if this file is being run directly
    print("two.py is being run directly")
else:
    print("two.py has been imported")
