from .utils import slugify, chunk_list
from .config import AppConfig


def build_title(config: AppConfig, *parts: str) -> str:
    """Build a display title from config name and extra parts.

    Parameters:
        config: Application configuration instance.
        parts: Additional strings to append.

    Returns:
        A hyphen-separated slug suitable for identifiers or filenames.
    """
    base = config.app_name
    tokens = [base, *parts]
    return slugify(" ".join(tokens)).replace("-", "-")


<<<<<<< HEAD
def sample_chunks(values: list[int], size: int) -> list[list[int]]:
    """Split a list of integers into non-overlapping chunks.
=======
def sub_numbers(a: int, b: int) -> int:
    """
    Substract two integers and returns the result.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The diff of a and b.

    Example:
        >>> sub_numbers(5, 3)
        2
    """
    return a - b
>>>>>>> 1a169db0400747ca60eb75f65f768cc37c0f63f1

    Parameters:
        values: List of integers.
        size: Chunk size, must be positive.

    Returns:
        A list of lists, each at most `size` long.
    """
    return [list(chunk) for chunk in chunk_list(values, size)]


if __name__ == "__main__":
<<<<<<< HEAD
    # Minimal demo run
    cfg = AppConfig(app_name="CodeMonitor", debug=True, max_items=42)
    print(build_title(cfg, "demo", "run"))
    print(sample_chunks(list(range(10)), 3))


=======
    analyze()
>>>>>>> 1a169db0400747ca60eb75f65f768cc37c0f63f1
