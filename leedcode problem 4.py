def length_of_last_word(s):
    words = s.strip().split()
    return len(words[-1]) if words else 0

# Example usage:
s = "Hi my dear friend"
output = length_of_last_word(s)
print(output)  # Output: 6

