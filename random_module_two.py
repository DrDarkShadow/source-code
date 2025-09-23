from typing import Iterable, Tuple


def count_vowels(text: str) -> int:
    """Count vowels in the given text in a case-insensitive manner.

    Parameters:
        text: Input string to scan.

    Returns:
        The number of characters in `text` that are vowels (a, e, i, o, u).
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in text if ch in vowels)


def pairwise_sum(numbers: Iterable[float]) -> float:
    """Compute the sum of numbers using a numerically stable approach.

    Parameters:
        numbers: Any iterable of floats or ints.

    Returns:
        The arithmetic sum of the values.
    """
    # Kahan summation for improved precision
    total = 0.0
    compensation = 0.0
    for value in numbers:
        y = float(value) - compensation
        t = total + y
        compensation = (t - total) - y
        total = t
    return total


def split_into_chunks(text: str, size: int) -> Tuple[str, ...]:
    """Split text into fixed-size chunks.

    Parameters:
        text: The string to split.
        size: The chunk length; must be positive.

    Returns:
        A tuple of substrings of length `size` (last may be shorter).
    """
    if size <= 0:
        raise ValueError("size must be positive")
    return tuple(text[i : i + size] for i in range(0, len(text), size))


