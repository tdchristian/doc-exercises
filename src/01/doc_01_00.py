# Mystery code 01_00

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. If you like, change any inputs and prints to give clearer feedback to the user.

x = input('Enter something: ')

y = 0
for z in x:
    if z in '.,!?;:':
        y = y + 1

print(y)
