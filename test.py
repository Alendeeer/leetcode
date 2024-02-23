import random

# Generate a list of 300 random natural numbers (assuming natural numbers start from 1)
a = [random.randint(1, 1000) for _ in range(10000)]


def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [i for i in arr if i < pivot]
    mid = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]
    return quickSort(left) + mid + quickSort(right)


print(quickSort(a)) 