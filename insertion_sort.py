def insertion_sort(L):
    n = len(L)
    for i in range(n):
        j = i - 1
        while j >= 0 and L[j] > L[j + 1]:
            current = L[j + 1]
            L[j + 1] = L[j]
            L[j] = current

            j -= 1

    return L
