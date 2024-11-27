# Mystery code solution 01_02

# DONE

# 1. Read & figure out how the code works. You can also test it by running it.
# 2. Write a comment explaining what the code does.
# 3. Change the variable names to logical ones.
# 4. Change any inputs and prints to give clearer feedback to the user.
# 5. In a comment, add two example inputs and the output you would expect.

# Tip: The % operator is called modulo or mod for short.
# x % y means "Return the remainder after dividing x by y."
# 5 % 3 = 2 (5 / 3 = quotient 1, remainder 2)
# 13 % 4 = 1 (13 / 4 = quotient 3, remainder 1)
# So if you do any number % 2, you'll find out if it's even:
# even numbers have a remainder of 0; odd numbers have a remainder of 1.

# This code repeatedly asks the user to enter a number
# until they enter an even number.

# Example 1: User enters 6. Output: "That will do"
# Example 1: User enters 5. Output: "Try again". User enters 8. Output: "That will do"

n = int(input('Enter a number: '))

while n % 2 != 0:
    print('Try again')
    n = int(input('Enter a number: '))

print('That will do')
