# Mystery code solution 02_08

"""
    DONE
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write a descriptive docstring that tells what it does
        - Write one docstring example showing a test case
"""

def get_chars_occurring_n_times(s: str, n: int) -> list:
    """
    Return a list of the characters in s that occur exactly n times.

    >>> get_chars_occurring_n_times('tynan', 2)
    ['n']
    >>> get_chars_occurring_n_times('tynan', 1)
    ['t', 'y', 'a']
    """
    counts = {}
    s = s.lower()
    
    for char in s:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1

    result = []
    for char in counts:
        if counts[char] == n:
            result.append(f)

    return result
