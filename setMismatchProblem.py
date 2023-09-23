"""
In the Set Mismatch problem, you will be given an array of positive integers with some elements missing or duplicated. You need to identify and return the missing and duplicated numbers to solve this problem.

Here’s an example of the input and output values of this problem:

Input: [1, 2, 3, 4, 4, 6] | Output: [5, 4]
"""

def findErrorNums(nums):
    n = len(nums)
    
    duplicate = -1
    for num in nums:
        if nums[abs(num) - 1] < 0:
            duplicate = abs(num)
        else:
            nums[abs(num) - 1] *= -1
    
    missing = -1
    for i in range(n):
        if nums[i] > 0:
            missing = i + 1
    return [duplicate, missing]

nums_str = input("Enter a list of numbers separated by spaces: ")
nums = [int(x) for x in nums_str.split()]

result = findErrorNums(nums)
print("Duplicate:", result[0])
print("Missing:", result[1])