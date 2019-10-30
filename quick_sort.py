def partition(A, low, high):
    pivot = A[int(low + ((high - low)/2))]
    i = low
    j = high + 1

    while i < j:
        while A[i] < pivot:
            i += 1

        j -= 1
        while A[j] > pivot:
            j -= 1

        A[i], A[j] = A[j], A[i]

    return j

def __quick_sort(A, low, high):
    if low < high:
        pivot = partition(A, low, high)
        __quick_sort(A, low, pivot)
        __quick_sort(A, pivot + 1, high)

def quick_sort(A):
    __quick_sort(A, 0, len(A) - 1)
    return A

print(quick_sort([5,4,3,5,1,5]))
