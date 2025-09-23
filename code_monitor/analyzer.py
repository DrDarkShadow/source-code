from typing import Iterable, Dict


def word_frequencies(lines: Iterable[str]) -> Dict[str, int]:
    """Compute case-insensitive word frequencies from an iterable of lines.

    Parameters:
        lines: An iterable yielding strings to analyze.

    Returns:
        A dictionary mapping each lowercase word to its occurrence count.
    """
    counts: Dict[str, int] = {}
    for line in lines:
        for token in line.split():
            key = token.strip().lower()
            if not key:
                continue
            counts[key] = counts.get(key, 0) + 1
    return counts


def longest_line_length(lines: Iterable[str]) -> int:
    """Return the maximum length among the provided lines.

    Parameters:
        lines: An iterable of strings.

    Returns:
        The length of the longest string, or 0 if `lines` is empty.
    """
    max_len = 0
    for line in lines:
        if len(line) > max_len:
            max_len = len(line)
    return max_len


def average_line_length(lines: Iterable[str]) -> float:
    """Return the average line length with safe handling of empty input.

    Parameters:
        lines: An iterable of strings.

    Returns:
        The arithmetic mean of line lengths, or 0.0 when no lines are given.
    """
    total = 0
    count = 0
    for line in lines:
        total += len(line)
        count += 1
    return float(total) / count if count else 0.0


