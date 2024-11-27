# Mystery code solution 02_04

"""
    DONE
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write a descriptive docstring that tells what it does
        - Write one docstring example showing a test case
"""

def print_facing_triangles(n: int) -> None:
    """
    Print two facing triangles with height and base of n - 1.

    >>> print_facing_triangles(3)
    x
    xx
      x
     xx
    >>> print_facing_triangles(1)
    """
    for i in range(1, n): # could call i 'row'
        print('x' * i)
        
    for i in range(1, n):
        print((' ' * (n - i)) + ('x' * i))

