# Boolean and Conditional Operations in Python
def boolean_and(a: bool, b: bool) -> bool:
    """Returns the logical AND of two boolean values."""
    return a and b
def conditional_operation(condition: bool, true_value, false_value):
    """Returns true_value if condition is True, else returns false_value."""
    return true_value if condition else false_value
# Example usage

if __name__ == "__main__":
    # Boolean AND examples
    print(boolean_and(True, True))   # Output: True
    print(boolean_and(True, False))  # Output: False
    print(boolean_and(False, True))  # Output: False
    print(boolean_and(False, False)) # Output: False

    # Conditional operation examples
    print(conditional_operation(True, "It's True!", "It's False!"))   # Output: It's True!
    print(conditional_operation(False, "It's True!", "It's False!"))
    # Output: It's False!