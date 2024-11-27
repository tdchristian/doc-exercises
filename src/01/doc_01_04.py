# Mystery code 01_04

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. If you like, change any inputs and prints to give clearer feedback to the user.

X = [-10, 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 154, 245, 1_000, 1_000_000]

y = int(input('Enter something: '))

z = []
for a in X:
    if a >= y:
        z.append(a)

print(f'{len(z)} / {len(X)}')
