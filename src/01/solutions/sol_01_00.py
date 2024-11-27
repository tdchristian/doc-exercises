# Mystery code solution 01_00

# DONE

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. If you like, change any inputs and prints to give clearer feedback to the user.

# This code asks the user to enter some text.
# Then, it tallies the number of punctuation characters in the text
# and prints the result.

text = input('Enter text: ')

n_punctuation = 0
for char in text:
    if char in '.,!?;:':
        n_punctuation = n_punctuation + 1

print(n_punctuation)
