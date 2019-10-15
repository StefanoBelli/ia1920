def isort(L):
    n = len(L)
    for i in range(n):
        j = i - 1
        while j >= 0 and L[j] > L[j + 1]:
            current = L[j + 1]
            L[j + 1] = L[j]
            L[j] = current

            j -= 1

    return L

print(isort([1,2,3,4,5])) # best case: O(n) (each element accessed)
print(isort([1,3,2,4,5]))
print(isort([1,3,4,2,5]))
print(isort([5,4,3,2,1])) # worst case: O(n^2)
