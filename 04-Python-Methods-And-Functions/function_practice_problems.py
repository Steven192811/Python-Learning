# Lesser of two evens: Write a function that returns the lesser of two given numbers
# if both numbers are even, but returns the greater if one or both numbers are odd


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        # Both numbers are even
        return min(a, b)
    else:
        # One or both numbers are odd
        return max(a, b)

# Example:
result = lesser_of_two_evens(4, 6)
print(result)  # 4

result = lesser_of_two_evens(5, 9)
print(result)  # 9



