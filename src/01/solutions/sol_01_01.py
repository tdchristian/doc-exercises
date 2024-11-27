# Mystery code solution 01_01

# DONE

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. If you like, change any inputs and prints to give clearer feedback to the user.

# This code asks the user to enter some text.
# Then, it finds all the vowel characters, stores them in a new string,
# and shows them to the user.

text = input('Enter text: ')

vowels = ''
for char in text:
    if char in 'aeiouAEIOU':
        vowels = vowels + char

print(vowels)
