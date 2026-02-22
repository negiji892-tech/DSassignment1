"""
ETCCDS202 - Data Structures
Unit 1 Assignment
Program 4: Recursive Binary Search

Recurrence Relation: T(n) = T(n/2) + O(1)
Time Complexity: O(log n)
Space Complexity: O(log n)
"""

def binary_search(arr, key, low, high):
    # Base Case: Element not found
    if low > high:
        return -1

    mid = (low + high) // 2

    # Element found
    if arr[mid] == key:
        return mid

    # Search left half
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)

    # Search right half
    else:
        return binary_search(arr, key, mid + 1, high)


# -------- Main Program --------
if __name__ == "__main__":
    try:
        arr = list(map(int, input("Enter sorted elements separated by space: ").split()))
        key = int(input("Enter element to search: "))

        result = binary_search(arr, key, 0, len(arr) - 1)

        if result != -1:
            print(f"Element found at index {result}")
        else:
            print("Element not found in the list.")

    except ValueError:
        print("Invalid Input! Please enter valid integers.")