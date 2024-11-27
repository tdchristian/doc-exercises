# Mystery code 01_02

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. If you like, change any inputs and prints to give clearer feedback to the user.

x = int(input('Input: '))

while x % 2 != 0:
    print('Try again')
    x = int(input('Input: '))

print('That will do')
