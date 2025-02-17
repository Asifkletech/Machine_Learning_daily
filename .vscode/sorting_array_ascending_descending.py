# Function to print first half in ascending order
# and second half in descending order
def printOrder(arr, n):
    # Sorting the array
    arr.sort()

    # Printing first half in ascending order
    for i in range(n // 2):
        print(arr[i], end=" ")

    # Printing second half in descending order
    for j in range(n - 1, n // 2 - 1, -1):
        print(arr[j], end=" ")

# Driver code
arr = [5, 4, 6, 2, 1, 3, 8, 9, 7]
n = len(arr)

printOrder(arr, n)
#


