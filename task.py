def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  
            break

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

optimized_bubble_sort(arr.copy())
print("Sorted array (optimized bubble sort):", arr)

insertion_sort(arr.copy())
print("Sorted array (insertion sort):", arr)