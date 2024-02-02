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

# mydog = Dog() # Animal Created, Dog Created

class Dog():
    def __init__(self, name): # Overwriting the Animal class
        self.name = name

    def speak(self):
        return self.name + ' says woof!'

class Cat():
    def __init__(self, name): # Overwriting the Animal class
        self.name = name

    def speak(self):
        return self.name + ' says meow!'

niko = Dog('niko')
felix = Cat('felix')

print(niko.speak()) # niko says woof!
print(felix.speak()) # felix says meow!

for pet in [niko, felix]:
    print(type(pet)) # <class '__main__.Dog'>, <class '__main__.Cat'>
    print(pet.speak()) # niko says woof!, felix says meow!

    class Animal():
        def __init__(self, name):
            self.name = name

        def speak(self):
            raise NotImplementedError('Subclass must implement this abstract method')

        class Dog(Animal):
            def speak(self):
                return self.name + ' says woof!'

        class Cat(Animal):
            def speak(self):
                return self.name + ' says meow!'

        fido = Dog('Fido')
        minino = Cat('Minino')

        print(fido.speak())
        print(minino.speak())
