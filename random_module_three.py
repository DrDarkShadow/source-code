from typing import Dict


def fibonacci(n: int) -> int:
    """Compute the nth Fibonacci number using an iterative approach.

    Parameters:
        n: Index of the Fibonacci number (0-indexed).

    Returns:
        The nth Fibonacci value.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def invert_dictionary(mapping: Dict[str, int]) -> Dict[int, str]:
    """Invert a dictionary with unique values.

    Parameters:
        mapping: Dictionary mapping strings to integers with unique values.

    Returns:
        A new dictionary mapping integers to strings.
    """
    if len(mapping.values()) != len(set(mapping.values())):
        raise ValueError("Values must be unique to invert dictionary")
    return {value: key for key, value in mapping.items()}


def is_palindrome(text: str) -> bool:
    """Return True if the given text is a palindrome, ignoring casing and spaces.

    Parameters:
        text: The string to check.

    Returns:
        True if `text` reads the same forwards and backwards after normalization.
    """
    normalized = ''.join(ch.lower() for ch in text if not ch.isspace())
    return normalized == normalized[::-1]


