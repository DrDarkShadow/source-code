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

def chaotic_transform(input_data, memo=None, depth=0):
    """
    Extremely messy function for parser testing.
    Performs:
    - Recursion
    - Multithreading
    - Random branching and exceptions
    - Mixed-type processing
    - State mutation through memo
    """
    if memo is None:
        memo = {}

    print(f"Depth {depth} | Input: {input_data}")  # I/O behavior

    # Stop condition with memo cache
    if isinstance(input_data, int):
        if input_data in memo:
            return memo[input_data]

        if input_data < 0:
            raise ValueError("Negative number encountered!")

        # Recursion to compute pseudo-fibonacci-like result
        if input_data in (0, 1):
            memo[input_data] = input_data
        else:
            memo[input_data] = (
                chaotic_transform(input_data - 1, memo, depth + 1) +
                chaotic_transform(input_data - 2, memo, depth + 1)
            )
        return memo[input_data]

    elif isinstance(input_data, list):
        # Thread worker to mutate list concurrently (nasty!)
        def worker(lst):
            for i in range(len(lst)):
                if isinstance(lst[i], int):
                    lst[i] *= 2
                elif isinstance(lst[i], str) and lst[i].isdigit():
                    lst[i] = int(lst[i]) + 5
                else:
                    lst[i] = None

        t = threading.Thread(target=worker, args=(input_data,))
        t.start()
        t.join()

        # Random chaos — recurse on results
        return [chaotic_transform(x, memo, depth + 1) if isinstance(x, int)
                else x for x in input_data]

    elif isinstance(input_data, str):
        # Random chance of failure
        if random.random() > 0.8:
            raise TypeError("Random string processing error!")

        stripped = input_data.strip().lower()
        if stripped.isdigit():
            return chaotic_transform(int(stripped), memo, depth + 1)
        return stripped[::-1]  # reverse string

    elif input_data is None:
        print("Encountered None — skipping")
        time.sleep(0.01)
        return None

    else:
        # Unknown type fallback
        return repr(input_data)
    
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
