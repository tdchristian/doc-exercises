# Mystery code 01_01

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. If you like, change any inputs and prints to give clearer feedback to the user.

x = input('Enter something: ')

y = ''
for z in x:
    if z in 'aeiouAEIOU':
        y = y + z

print(y)
