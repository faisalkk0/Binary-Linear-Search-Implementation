def linear_search(arr, target):
    # Loop through each element in the array
    for index, value in enumerate(arr):
        if value == target:  # Check if the current element matches the target
            return index  # Return the index of the target
    return -1  # Return -1 if the target is not found

# Example usage
arr = [4, 2, 9, 1, 5, 6]
target = 5
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
def binary_search(arr, target):
    # Initial low and high indices
    low = 0
    high = len(arr) - 1
    
    # While the search space is valid
    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        if arr[mid] == target:    # Check if the target is at the mid
            return mid
        elif arr[mid] < target:   # Target is in the right half
            low = mid + 1
        else:                      # Target is in the left half
            high = mid - 1
    
    return -1  # Target not found

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
