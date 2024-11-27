# Mystery code 01_03

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. Change any inputs and prints to give clearer feedback to the user.
# 5. In a comment, add two example inputs and the output you would expect.

# Tip: Remember that variables at the top of a script that are intended
# not to change are called "constants" and are written in ALL CAPS.

X = '<>:"/\|?* '
Y = '_'

z = input('Enter something: ')

for a in x:
    z = z.replace(a, y)

print(f'Result: {z}')
