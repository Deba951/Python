"""
Anagrams are words formed by rearranging the letters of another word, For example, car and arc, cat and act, etc. Grouping anagrams is one of the popular questions in coding interviews.

Given a list of words, and write an algorithm to group all the words which are anagrams of each other.
"""

from collections import defaultdict

def group_anagrams(a):
    
    dfdict = defaultdict(list)
    
    for i in a:
        # Remove spaces from the word before sorting and joining
        sorted_i = "".join(sorted(i.replace(" ", "")))

        # Append the original word to the list associated with the sorted version
        dfdict[sorted_i].append(i)
    
    return dfdict.values()

# Get user input for a list of words (comma-separated)
user_input = input("Enter a list of words (comma-separated): ")

# Split the user input into a list of words
words = user_input.split(',')

# Group anagrams and print the result
anagram_groups = group_anagrams(words)

for group in anagram_groups:
    print("Anagram Group:", group)