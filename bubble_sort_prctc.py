#Making  an array
arr  = (2, 5, 1, 2, 3)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
print(bubble_sort(arr))

