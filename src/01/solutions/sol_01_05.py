# Mystery code solution 01_05

# DONE

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. If you like, change any inputs and prints to give clearer feedback to the user.

x = []

y = input('Enter a name or Q to quit: ')
while y.upper() != 'Q':
    if y.isalpha():
        x.append(y.title())

    y = input('Enter a name or Q to quit: ')

print(f'Valid names:')
for z in x:
    print(z)
