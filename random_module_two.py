def reverse_words(sentence):
    words = sentence.split()
    return " ".join(reversed(words))

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d)**power for d in digits)

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid        # index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1   # not found

