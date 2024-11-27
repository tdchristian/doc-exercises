# Mystery code solution 02_02

"""
    DONE
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write a descriptive docstring that tells what it does
        - Write one docstring example showing a test case
"""

def is_mixed_case(s: str) -> bool:
    """
    Return True iff a contains at least one lowercase
    and one uppercase letter.
    """
    
    found_upper = False
    found_lower = False
    
    for char in s:
        
        if char.isupper():
            found_upper = True
            
        elif char.islower():
            found_lower = True
            
    return found_upper and found_lower
