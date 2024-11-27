# Mystery code solution 01_04

# DONE

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. If you like, change any inputs and prints to give clearer feedback to the user.

x = [19, 13, 15, 18, 22, 21, 14, 16, 19]
y = []

for z in x:
    if z >= 18:
        y.append(z)

print(f'Found {len(y)} people old enough to vote out of {len(x)} total')
