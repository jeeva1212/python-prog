def count_characters(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1

    return char_count

input_string = "ABCABCABBCDE"
char_occurrences = count_characters(input_string)
output_string = ", ".join([f"{char}---{count}" for char, count in char_occurrences.items()])
print("output:",output_string)
