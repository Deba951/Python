"""
The mean is the average value of all the values in a dataset. 

The Median is the middle value among all the values in sorted order.
    when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2
    when the total number of values is odd: Median = {(n+1)/2}thterm

Mode is the most frequently occurring value among all the values.
"""


# Using libraries:-
import statistics

# Input: Taking a list of numbers as input from the user
input_numbers = input("Enter a list of numbers separated by spaces: ")
numbers = [float(x) for x in input_numbers.split()]

# Calculate the mean
mean = statistics.mean(numbers)

# Calculate the median
median = statistics.median(numbers)

# Calculate the mode
try:
    mode = statistics.mode(numbers)
except statistics.StatisticsError:
    mode = "No unique mode found"

# Display the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")



# Without using libraries:-
# Function to calculate the mean
def calculate_mean(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    return mean

# Function to calculate the median
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        # If the array has an even length, average the two middle values
        middle1 = numbers[n // 2 - 1]
        middle2 = numbers[n // 2]
        median = (middle1 + middle2) / 2
    else:
        # If the array has an odd length, take the middle value
        median = numbers[n // 2]
    return median

# Function to calculate the mode
def calculate_mode(numbers):
    from collections import Counter
    # Count the frequency of each number
    frequency = Counter(numbers)
    # Find the number with the highest frequency
    mode = [k for k, v in frequency.items() if v == max(frequency.values())]
    return mode

user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

# Calculate and display the mean, median, and mode
mean = calculate_mean(numbers)
median = calculate_median(numbers)
mode = calculate_mode(numbers)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)