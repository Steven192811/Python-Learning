class Animal():
    def __init__(self):
        print('Animal Created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

# myanimal = Animal() # Animal Created
# myanimal.eat() # I am eating
# myanimal.who_am_i() # I am an animal

class Dog(Animal): # Inheritance
    def __init__(self): # Overwriting the Animal class
        Animal.__init__(self) # Animal Created
        print('Dog Created')

    def who_am_i(self): # Overwriting the Animal class
        print('I am a dog!')

    def bark(self): # New method
        print('WOOF!')
