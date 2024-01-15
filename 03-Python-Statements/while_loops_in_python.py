x = 0
while x < 5:
    print(f'The current value of x is {x}') # 0, 1, 2, 3, 4
    x += 1 # x = x + 1 (increment x by 1)
else:
    print("X IS NOT LESS THAN 5")

#break: # break out of the current closest enclosing loop
#continue: # goes to the top of the closest enclosing loop
#pass: # does nothing at all (placeholder)

#pass:
x = [1,2,3]
for item in x:
    # comment
    pass #(no error) (no output) (no effect)

#continue:
mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter) # S, m, m, y (no a)

#break:
x = 0
while x < 5:
    if x == 2:
        break
    print(x) # 0, 1
    x += 1 # x = x + 1 (increment x by 1)

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        break
    print(letter) # S (no a, m, m, y) (break out of the current closest enclosing loop)
