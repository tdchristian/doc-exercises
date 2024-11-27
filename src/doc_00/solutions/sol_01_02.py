# Mystery code solution 00_02

# DONE

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. Change any inputs and prints to give clearer feedback to the user.
# 5. In a comment, add two example inputs and the output you would expect.

# This code asks the user for some text and then a number of characters to print.
# Then, it prints that many characters of the string, each on their own line.

# Example 1: User enters "hello" and 3. Output: "h" / "e" / "l"
# Example 2: User enters "joy" and 1. Output: "j"

text = input('Enter text: ')
upper = int(input('Enter how many characters to print:'))

for i in range(upper):
    print(text[i])
