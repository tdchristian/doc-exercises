# Mystery code 01_04

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. Change any inputs and prints to give clearer feedback to the user.
# 5. In a comment, add two example inputs and the output you would expect.

# Tip: Remember that variables at the top of a script that are intended
# not to change are called "constants" and are written in ALL CAPS.

X = [-10, 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 154, 245, 1_000, 1_000_000]

y = int(input('Enter something: '))

z = []
for a in X:
    if a >= y:
        z.append(a)

print(f'{len(z)} / {len(X)}')
