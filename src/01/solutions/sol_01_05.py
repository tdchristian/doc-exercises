# Mystery code solution 01_05

# DONE

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. Change any inputs and prints to give clearer feedback to the user.
# 5. In a comment, add two example inputs and the output you would expect.

# This code repeatedly asks the user to enter names. If they enter "Q",
# it stops. Each name is checked that it only consists of alphabetic
# characters, and if so, it's converted to title case and added to a list.
# Once the user stops, it prints each of the names that were retained.

# Example 1: User enters "Bob" then "Jane" then "Me!" then "Q". Output: "Bob" / "Jane"
# Example 2: User enters "L33T" then "??" then "Q". No output is shown.

valid_names = []

name = input('Enter a name, or Q to stop: ').upper().strip()
while name != 'Q':
    if name.isalpha():
        valid_names.append(name.title())

    name = input('Enter a name, or Q to stop: ').upper().strip()

print(f'Valid names:')
for name in valid_names:
    print(name)
