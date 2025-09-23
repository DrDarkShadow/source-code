from .analyzer import average_line_length, longest_line_length, word_frequencies


def demo_text_metrics() -> dict:
    """Provide a small demonstration of text analytics helpers.

    Returns:
        A dictionary containing frequency, longest length, and average length
        for a fixed set of example lines.
    """
    lines = [
        "Hello world",
        "hello again",
        "WORLD of code",
    ]
    return {
        "freq": word_frequencies(lines),
        "longest": longest_line_length(lines),
        "avg": average_line_length(lines),
    }


def is_passing_example() -> bool:
    """Return True if demo metrics meet simple sanity constraints."""
    metrics = demo_text_metrics()
    return bool(metrics["freq"]) and metrics["longest"] >= 5 and metrics["avg"] > 0


