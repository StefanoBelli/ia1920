def selection_sort(L):
    n = len(L)
    end = n - 1

    for i in range(n):
        globalMinIndex = end
        for cur in range(i, n - 1):
            nxt = cur + 1
            localMinIndex = 0
            if L[nxt] < L[cur]:
                localMinIndex = nxt
            else:
                localMinIndex = cur

            if L[localMinIndex] < L[globalMinIndex]:
                globalMinIndex = localMinIndex

        if globalMinIndex != i:
            L[i], L[globalMinIndex] = L[globalMinIndex], L[i]

    return L
