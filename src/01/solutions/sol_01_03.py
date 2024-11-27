# Mystery code solution 01_03

# DONE

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. Change any inputs and prints to give clearer feedback to the user.
# 5. In a comment, add two example inputs and the output you would expect.

# Tip: Remember that variables at the top of a script that are intended
# not to change are called "constants" and are written in ALL CAPS.

# This code asks the user to enter some text. It then goes through
# a predefined constant of symbols, and for each one, it replaces it
# with an underscore in the user's text. Finally it prints the result.

# Example 1: User enters "Where is Paris?" Output: "Where_is_Paris_"
# Example 2: User enters "Equation: 7 * 5 > 30 / 6". Output: "7___5___30___6"

ILLEGAL_CHARS = '<>:"/\|?* '
REPLACEMENT_CHAR = '_'

text = input('Enter some text: ')

for char in ILLEGAL_CHARS:
    text = text.replace(char, REPLACEMENT_CHAR)

print(f'Result: {text}')
