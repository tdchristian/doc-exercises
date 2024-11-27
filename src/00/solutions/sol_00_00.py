# Mystery code solution 00_00

# DONE

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. If you like, change any inputs and prints to give clearer feedback to the user.

# This code asks the user for two string inputs.
# It then combines the first letter of the first string
# and the last letter of the second string, and prints that.

text_1 = input('Enter a sentence: ')
text_2 = input('Enter another sentence: ')
first_and_last = text_1[0] + text_2[-1]

print(first_and_last)
