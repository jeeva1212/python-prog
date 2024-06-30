def encode_password(password, shift):
    encoded_password = []
    for char in password:
        # Shift each character by 'shift' positions in ASCII
        encoded_char = chr(ord(char) + shift)
        encoded_password.append(encoded_char)
    return ''.join(encoded_password)

# Example usage

password = "mysecretpassword"
shift = 3
encoded_password = encode_password(password, shift)
print(f"Original Password: {password}")
print(f"Encoded Password: {encoded_password}")
