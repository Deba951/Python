"""
Find Missing Number using Python
Finding the missing number in an array is a popular coding interview question. 

Given an array containing a range of numbers from 0 to n with a missing number, find the missing number in the input array.

Finding the missing number in an array means finding the numbers missing from the array according to the range of values inside the array.

To find the missing number in an array, we need to iterate over the input array and store the numbers that are not present or missing in the array in another array. Returning the second array will give the desired answer.
"""

def find_missing_numbers(arr):
    # Converting the input array to a set for faster iteration
    input_set = set(arr)
    
    # Find the maximum number in the input array
    max_num = max(input_set)
    
    # Create a set of all numbers from 0 to the maximum number in the input array
    full_set = set(range(max_num + 1))
    
    # Find the missing numbers by taking the difference of the two sets
    missing_numbers = list(full_set - input_set)
    
    return missing_numbers

# Get user input as a comma-separated list of integers
user_input = input("Enter a list of numbers comma-separated: ")

# Split the user input into a list of integers
input_array = [int(x) for x in user_input.split(',')]

missing_numbers = find_missing_numbers(input_array)
print("Missing numbers:", missing_numbers)