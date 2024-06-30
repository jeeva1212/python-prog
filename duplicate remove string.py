"""def remove_duplicates(input_string):
    # Use an ordered set to maintain the order of characters
    seen = set()
    result = []
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

# Example usage
input_string = "ABCDABBCDABBBCCCDDEEEF"
output_string = remove_duplicates(input_string)
print(f"Input: {input_string}")
print(f"Output: {output_string}")"""


def remove_duplicates(input_string):
    seen = set()
    result = ''
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result += char
    return result

input_string  = "ABCDABBCDABLLLABBBCCCDDEEEEFG"
output_string = remove_duplicates(input_string)
print("output:",output_string)

