# Mystery code solution 01_04

# DONE

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. If you like, change any inputs and prints to give clearer feedback to the user.

# This code defines a long list of numbers. Then it asks the user to enter
# some value. It goes through the list and retains all the numbers
# greater than or equal to the user's value by adding them to a new list.
# Finally, it shows them a ratio of how many numbers were retained over
# how many numbers there were at the beginning.

# Tip: Remember that variables at the top of a script that are intended
# not to change are called "constants" and are written in ALL CAPS.

VALUES = [-10, 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 154, 245, 1_000, 1_000_000]

threshold = int(input('Enter something: '))

values_over_threshold = []
for value in VALUES:
    if value >= threshold:
        values_over_threshold.append(value)

print(f'{len(values_over_threshold)} / {len(VALUES)}')
