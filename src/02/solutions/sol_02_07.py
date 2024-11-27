# Mystery code solution 02_07

"""
    DONE
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write a descriptive docstring that tells what it does
        - Write one docstring example showing a test case
"""

def combine_names(first_name, second_name):
    """
    Combine strings first_name and second_name by taking
    the first half of first_name and the second half of second_name.

    >>> mister_e('nicholas', 'brouwer')
    'Nichuwer'
    >>> mister_e('samuel', 'debra')
    'Sambra'
    """
    i_first_half = len(first_name) // 2
    i_second_half = len(second_name) // 2
    new_name = first_name[:i_first_half] + second_name[i_second_half:]
    return new_name.title()
