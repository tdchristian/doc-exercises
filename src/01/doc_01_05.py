# Mystery code 01_06

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. If you like, change any inputs and prints to give clearer feedback to the user.

x = []

y = input('Enter something, or Q to stop: ').upper().strip()
while y != 'Q':
    if y.isalpha():
        x.append(y.title())

    y = input('Enter something, or Q to stop: ').upper().strip()

print(f'Result:')
for z in x:
    print(z)
