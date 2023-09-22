def binarySearch(arr, target):
    
    arr.sort()  
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  

        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  

    return -1  


arr = input("Enter elements of the array separated by spaces: ").split()
arr = [int(x) for x in arr] 
target = int(input("Enter the element to search for: "))

result = binarySearch(arr, target)

if result != -1:
    print(f"Element {target} found at index {result} that is position {result+1} in the soorted array!!")
else:
    print(f"Element {target} not found in the array")