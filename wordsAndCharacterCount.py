# Get the input paragraph from the user
paragraph = input("Enter a paragraph: ")

# Number of words
words = paragraph.split()
word_count = len(words)

# Number of characters including spaces
char_count = len(paragraph)

# Number of characters excluding spaces
char_count_without_spaces = len(paragraph.replace(" ", ""))

# Number of special characters
special_char_count = sum(1 for char in paragraph if not char.isalnum() and not char.isspace())

print("Number of words in the paragraph:", word_count)
print("Number of characters in the paragraph (including spaces):", char_count)
print("Number of characters in the paragraph (excluding spaces):", char_count_without_spaces)
print("Number of special characters in the paragraph:", special_char_count)