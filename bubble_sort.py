def bubble_sort(L):
    n = len(L) - 1
    swapped_once = True

    while swapped_once:
        swapped_once = False

        for i in range(n):
            n = i + 1

            if L[i] > L[n]:
                L[n], L[i] = L[i], L[n]
                swapped_once = True

    return L

print(bubble_sort([7,2,4,5,3,1]))
