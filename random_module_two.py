def reverse_words(sentence):
    words = sentence.split()
    return " ".join(reversed(words))

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d)**power for d in digits)
