my_list = [1, 2, 3]
len(my_list)
print(my_list)

class Sample():
    pass

mysample = Sample() # Instance of the Sample class
print(mysample)
print(type(mysample)) # <class '__main__.Sample'>

class book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')

b = book('Python rocks', 'Jose', 200)
print(b) # Python rocks by Jose
print(len(b)) # 200
del b # A book object has been deleted 
