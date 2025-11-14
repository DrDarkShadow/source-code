def reverse_words(sentence):
    words = sentence.split()
    return " ".join(reversed(words))


def second_largest(lst):
    if len(lst) < 2:
        raise ValueError("Need at least two elements")

    first = second = None
    for x in lst:
        if first is None or x > first:
            second = first
            first = x
        elif x != first and (second is None or x > second):
            second = x

    if second is None:
        raise ValueError("All elements are equal")
    return second

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
