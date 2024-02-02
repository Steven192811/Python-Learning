my_list = [1, 2, 3]
print(my_list)

myset = set()

type(myset)

class Dog(): # class keyword

# Class Object Attribute
# Same for any instance of a class
    species = 'mammal'

def __init__(self, breed, name):

    # Attributes
    # We take in the argument
    # Assign it using self.attribute_name
    self.breed = breed
    self.name = name

# my_dog = Dog(mybreed='Puddle', name='Niño')
# print(my_dog)

# Operations/Acctions ---> Methods

def bark(self, number): # Method
    print('WOOF! My name is {} and the number is {}'.format(self.name, number))

# my_dog.bark(10)

    class Circle():

    # Class Object Attribute
        pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius*radius*Circle.pi

#Method
def get_circumference(self):
    return self.radius * self.pi * 2
    my_circle = Circle(30) # radius = 30
    my_circle.pi # 3.14
    my_circle.radius # 30
    my_circle.area # 2826.0
    my_circle.get_circumference() # 188.4
