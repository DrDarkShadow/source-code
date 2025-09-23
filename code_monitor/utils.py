import re
from typing import Iterable, Iterator


def slugify(text: str) -> str:
    """Convert a string into a lowercase, hyphen-separated slug.

    Non-alphanumeric characters are collapsed into single hyphens.
    Leading and trailing hyphens are trimmed.
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def chunk_list(values: Iterable[int], size: int) -> Iterator[list[int]]:
    """Yield successive chunks (lists) from an iterable of integers.

    Parameters:
        values: Iterable of integers.
        size: Desired chunk length; must be positive.

    Yields:
        Lists of integers of length `size` (last may be shorter).
    """
    if size <= 0:
        raise ValueError("size must be positive")
    bucket: list[int] = []
    for value in values:
        bucket.append(int(value))
        if len(bucket) >= size:
            yield bucket
            bucket = []
    if bucket:
        yield bucket


def safe_int(value: str, default: int = 0) -> int:
    """Parse an integer from a string, returning `default` on failure."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


<<<<<<< HEAD
=======
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
            obj_type = "Class" if isinstance(node, ast.ClassDef) else "Function"
            objects[node.name] = {
                "type": obj_type,
                "name": node.name,
                "start_line": node.lineno,
                "end_line": node.end_lineno
            }
    return objects

def hello(name):
    print(name)


def calculate_fibonacci(n):
    """
    Calculates the n-th Fibonacci number using an iterative approach.

    This function is designed to be a clear example of a new, distinct piece of logic
    added to test the documentation agent's ability to intelligently place
    new documentation snippets.

    Args:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The n-th Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
>>>>>>> 1a169db0400747ca60eb75f65f768cc37c0f63f1
