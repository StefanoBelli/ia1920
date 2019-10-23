def list_copyat(to, fr, beg, end):
    while beg < end:
        to.append(fr[beg])
        beg += 1

    return to

def sorted_merge(a, b):
    new = []
    end_a = len(a)
    end_b = len(b)
    idx_a = 0
    idx_b = 0

    while idx_a < end_a and idx_b < end_b:
        if a[idx_a] < b[idx_b]:
            new.append(a[idx_a])
            idx_a += 1
        elif b[idx_b] < a[idx_a]:
            new.append(b[idx_b])
            idx_b += 1

    if idx_a < end_a:
        new = list_copyat(new, a, idx_a, end_a)
    elif idx_b < end_b:
        new = list_copyat(new, b, idx_b, end_b)

    return new

def merge_sort(L):
    n = len(L)

    if n < 2:
        return L

    mid = int(n/2)
    first_half = merge_sort(L[:mid])
    last_half = merge_sort(L[mid:])

    return sorted_merge(first_half, last_half)

print(merge_sort([7,2,4,3,5,1]))
