# Mystery code solution 02_03

"""
    DONE
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write a descriptive docstring that tells what it does
        - Write one docstring example showing a test case
"""

def multiply_list(numbers: list) -> int:
    """
    Return the cumulative product of all the given numbers.

    >>> multiply_list([5, 7, 42])
    1470
    >>> multiply_list([5, 2, 0])
    0
    """
    
    product = 1
    for number in numbers:
        product *= number
    return product
