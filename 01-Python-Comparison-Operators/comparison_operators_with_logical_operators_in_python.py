print (1<2<3) # True
print (1<2>3) # False

# and operator, both conditions must be True
print (1<2 and 2<3) # True
print ("h" == "h") and (2==2) # True

# or operator, only one condition must be True
print (1==1 or 2==2) # True #
print (100==1 or 2==2) # True
print (100==1 or 2==200) # False

# not operator, inverts the boolean value of the condition
print (1==1) # True
print (not(1==1)) # False
print (400>5000) # False
print (not(400>5000)) # True
