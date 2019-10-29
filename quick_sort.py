def partition(A, low, high):
    pivot = int(low + ((high - low)/2))

    i = low
    j = high

    while i < j:
        if A[i] < A[pivot]:
            i += 1
        elif A[j] > A[pivot]:
            j -= 1
        A[i], A[j] = A[j], A[i]

    return j

def __quick_sort(A, low, high):
    if low >= high:
        return A

    pivot = partition(A, low, high)
    __quick_sort(A, low, pivot)
    __quick_sort(A, pivot+1, high)

    return A

def quick_sort(A):
    return __quick_sort(A, 0, len(A) - 1)

print(quick_sort([5,4,3]))
