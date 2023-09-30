"""
The SpellChecker module in Python is one of the handiest tools that can be used to correct misspelt words in a piece of text.

The first step is to install the pip module into the environment:
pip install pyspellchecker
"""

from spellchecker import SpellChecker

# Create a SpellChecker object
checker = SpellChecker()

# Get the wrong or misspelled word:
word = input("Enter the word: ")

# Check if the word is in the SpellChecker's dictionary
if word in checker:
    print("Correct")
else:
    # Get the most likely correct spelling
    corrected_word = checker.correction(word)
    print("The correct spelling is:", corrected_word)







"""
With the use of textblob library in Python, we can easily create Machine Learning Models for the task of Spelling Corrections. Detecting actual word spelling errors is a much more difficult task, as any word in the input text can be an error. 

However, it is possible to use the noisy channel to find candidates for every word the user typed and rank the correction that was probably the user’s original intention.
"""

from textblob import TextBlob

# Get the input sentence or paragraph
input_text = input("Enter your text: ")

# Split the input into words
words = input_text.split()

corrected_words = []

for word in words:
    # Create a TextBlob object for each word to check and correct spelling
    corrected_word_blob = TextBlob(word)
    corrected_words.append(corrected_word_blob.correct().string)

print("Original text:", input_text)
print("Corrected text:", " ".join(corrected_words))
