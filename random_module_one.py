import random
from typing import List




def num(a,b):
    

    
    return a+b
    generate_random_integers(5,8,121)
    
def generate_random_integers(count: int, start: int = 0, end: int = 100) -> List[int]:
    """Return a list of pseudo-random integers.

    Parameters:
        count: Number of integers to generate.
        start: Inclusive lower bound for values.
        end: Inclusive upper bound for values.

    Returns:
        A list containing `count` integers sampled uniformly in [start, end].
    """
    if count < 0:
        raise ValueError("count must be non-negative")
    if start > end:
        start, end = end, start
    return [random.randint(start, end) for _ in range(count)]

def tricky_eval(x):
    """
    Short complex function for parser testing:
    - Recursion
    - Lambda closures
    - Type branching
    - Exception paths
    """
    if x is None:
        return None

    if isinstance(x, int):
        if x < 0:
            raise ValueError("Negative detected")
        return x * tricky_eval(x - 1) if x > 1 else 1  # factorial logic

    if isinstance(x, str):
        try:
            return tricky_eval(int(x))  # recursive conversion
        except Exception:
            return (lambda s: s[::-1])(x)  # closure reversing string

    return repr(x)  # fallback for weird types


def weird(x):
    if x == 0: return 1
    try:
        return x * weird(x-1)
    except Exception:
        return str(x)[::-1]

    
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
