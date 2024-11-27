# Mystery code solution 00_01

# DONE

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. Change any inputs and prints to give clearer feedback to the user.
# 5. In a comment, add two example inputs and the output you would expect.

# This code asks the user for some text, and then for a phrase.
# If the phrase occurs in the text, it prints how many times it occurs.
# Otherwise, it prints a message informing them of the fact.

# Example 1: User enters "hello" and "l". Output: 2
# Example 2: User enters "bye" and "l". Output: "Not found"

text = input('Enter text: ')
subtext = input('Enter text phrase to search for: ')

if subtext in text:
    print(text.count(subtext))
else:
    print('Not found')

