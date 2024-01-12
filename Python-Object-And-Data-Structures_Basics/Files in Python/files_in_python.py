# If the file is in the same directory as the .py file, you can just pass in the name of the file. Oherwise, you need to pass in the full path of the file as shown below.
# myfile = open("\Users\stevenmarquez\code\Steven192811\Python-Learning\Python-Object-And-Data-Structures_Basics\Files in Python\myfile.txt")

myfile = open('myfile.txt') # Open the text file myfile.txt in the same directory
print(myfile.read()) # Hello this is a text file
print(myfile.read()) # '' (empty string)
myfile.seek(0) # 0
print(myfile.read()) # Hello this is a text file
myfile.seek(0)
contents = myfile.read()
print(contents) # Hello this is a text file
myfile.seek(0)
myfile.readlines() # ['Hello this is a text file']

myfile.close() # Close the file
# The above code is not ideal because if there is an error in the code, the file will not close. Instead, use the with statement as shown below.
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
print(contents) # Hello this is a text file
# The with statement automatically closes the file after the code block is executed.

with open('myfile.txt', mode='r') as myfile:
    contents = myfile.read() # Read the file

#with open('myfile.txt', mode='w') as myfile: # Error operation not supported
#contents = myfile.read() # Write to the file

# mode='r' is read only
# mode='w' is write only (will overwrite files or create new!)
# mode='a' is append only (will add on to files)
# mode='r+' is reading and writing
# mode='w+' is writing and reading (Overwrites existing files or creates a new file!)

with open("my_new_file.txt", mode='r') as f:
    print(f.read()) # One on first line Two on second line Three on third line.
with open("my_new_file.txt", mode='a') as f:
    f.write('Four on fourth line.') # Write to the file
with open("my_new_file.txt", mode='r') as f:
    print(f.read()) # One on first line Two on second line Three on third line. Four on fourth line.

with open("asdasdasd.txt", mode='w') as f:
    f.write('I created this file!') # Write to the file
with open("asdasdasd.txt", mode='r') as f:
    print(f.read()) # I created this file!
