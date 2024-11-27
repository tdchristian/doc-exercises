# Mystery code 01_01

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. Change any inputs and prints to give clearer feedback to the user.
# 5. In a comment, add two example inputs and the output you would expect.

x = input('Enter something: ')

y = ''
for z in x:
    if z in 'aeiouAEIOU':
        y = y + z

print(y)
