# Mystery code solution 02_00

"""
    DONE
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write a descriptive docstring that tells what it does
        - Write one docstring example showing a test case
"""

def remove_odd_numbers(numbers: list[int]) -> list[int]:
    """
    Take a list of numbers and return only the even ones.

    >>> remove_odd_numbers([1, 2, 3])
    [2]
    >>> remove_odd_numbers([3, 4, 6])
    [4, 6]
    """
    
    even_numbers = []

    for number in numbers:

        # If the number is even (divisible by 2)
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers
