                        # Displaying Information
def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

display(row1, row2, row3)

row2[1] = "X"

display(row1, row2, row3)

                        # Accepting User Input
input("Please enter a value: ")

result = input("Please enter a value: ")

type(result) # str

result = int(input("Please enter a value: "))

result_int = int(result)

type(result_int) # int

type(2.3) # float

float("3.14") # 3.14

position_index = int(input("Choose an index position: "))

row1[position_index]

row2[position_index]

result = input("Enter a number here: ")

input("Enter a number here: ")

                        # Validating User Input
def user_choice():

# VARIABLES

    # Initial
    choice = "WRONG"
    acceptable_range = range(0, 10)
    within_range = False

# Two Conditions to Check
# Digit or Within_Range == False

    while choice.isdigit() == False or within_range == False:

        choice = input("Please enter a number (0-10): ")

# DIGIT CHECK
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")

# RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of acceptable range (0-10)")
                within_range = False

    return int(choice)

user_choice() # 5

some_value = "100"

some_value.isdigit() # True

result = "WRONG VALUE"

acceptable_values = [0, 1, 2]

result in acceptable_values # False

result not in acceptable_values # True
