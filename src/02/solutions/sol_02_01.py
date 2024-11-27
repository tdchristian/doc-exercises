# Mystery code solution 02_01

"""
    DONE
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write a descriptive docstring that tells what it does
        - Write one docstring example showing a test case
"""

def exclude(a: list, b: list) -> set:
    """
    Return the items in a that are not b.

    >>> exclude([1, 2, 3], [4, 5, 6])
    [1, 2, 3]
    >>> exclude([1, 2, 3], [1, 2, 3])
    []
    >>> exclude([1, 2, 3], [1, 2])
    [3]
    """

    only_in_a = []
    for item in a:
        if item not in b:
            only_in_a.append(item)
    return only_in_a
