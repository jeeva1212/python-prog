def decode_string(s):
    decode_string =" "
    i = 0
    while i< len(s):
        char = s[i]
        count = int(s[i+1])
        decode_string += char * count
        i += 2
    return decode_string

input_string = "a4b3c2"
output_string = decode_string(input_string)
print("output:",output_string)