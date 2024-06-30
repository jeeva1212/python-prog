"""def reverse_order_of_words(sentence):
    words = []  # Create an empty list to store individual words
    word_start = 0  # Initialize the index where a word starts

    # Iterate through each character in the sentence
    for i, char in enumerate(sentence):
        # If the current character is a space or it's the last character
        if char == ' ' or i == len(sentence) - 1:
            # Extract the word from the sentence
            word = sentence[word_start:i+1].strip()
            words.append(word)  # Add the word to the list
            word_start = i + 1  # Update the starting index for the next word

    # Reverse the order of words
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence

# Test the function
input_sentence = "Learning Python is very Easy"
reversed_sentence = reverse_order_of_words(input_sentence)
print("Reversed Sentence:", reversed_sentence)"""

"""def reverse_words(sentence):
    words = sentence.split()  # Split the sentence into words
    reversed_sentence = ' '.join(reversed(words))  # Reverse the order of words and join them back into a sentence
    return reversed_sentence

# Test the function
input_sentence = "Learning Python is very Easy"
reversed_sentence = reverse_words(input_sentence)
print("Reversed Sentence:", reversed_sentence)"""


# not working this program
"""def  reverse_order_of_words(sentence):
    word = []
    word_start = 0

    for i in enumerate(sentence):
        i == len(sentence)
        # Extract the word from the sentence
        word = sentence[word_start:i+1].strip()
        word_start = i+1
    # Reverse the order of words
    reversed_sentence = ''.join(word[::-1])
    return reversed_sentence
# Test the function
input_sentences = "learning python is very Easy"
reverse_sentence = reverse_order_of_words(input_sentences)
print("Reversed sentence:", reverse_sentence)"""

# Input type reverse word of sentence

def my_function(x):
    words = x.split()
    reversed_words = words[::-1]
    reversed_text = ' '.join(reversed_words)
    return reversed_text

user_input = input("Enter the text:")
my_txt = my_function(user_input)
print(my_txt)

