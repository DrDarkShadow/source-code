def choose_random_item(items: List[str]) -> str:
    """Choose a single random item from a non-empty sequence.

    Parameters:
        items: A list of strings to choose from.

    Returns:
        A single string chosen uniformly at random.
    """
    if not items:
        raise ValueError("items must not be empty")
    return random.choice(items)

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
    
def shuffle_copy(items: List[int]) -> List[int]:
    """Return a shuffled copy of the given list without mutating the input.

    Parameters:
        items: A list of integers.

    Returns:
        A new list containing the same integers in random order.
    """
    copy = list(items)
    random.shuffle(copy)
    return copy
