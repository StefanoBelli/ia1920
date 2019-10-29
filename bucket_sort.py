def list_copyat(to, fr):
    beg = 0
    end = len(fr)

    while beg < end:
        to.append(fr[beg])
        beg += 1

    return to

def interval_split(max, by, min):
    intvl = list()
    while min < max:
        oldmin = min + 1
        min += by
        intvl.append((oldmin, min))

    return intvl

def create_buckets(m, b, minel):
    bcks = dict()
    i = 0
    intervals = interval_split(m, b, minel)
    maxbcks = len(intervals)

    while i < maxbcks:
        bcks[intervals[i]] = list()
        i += 1

    return bcks

def in_range(e, i):
    return i[0] <= e and i[1] >= e

def bucket_sort(A, min=0, incby=10, sort=sorted):
    buckets = create_buckets(max(A), incby, min)

    for elem in A:
        for intvl in buckets:
            if in_range(elem, intvl):
                buckets[intvl].append(elem)

    sortedA = list()
    for key in buckets:
        list_copyat(sortedA, sort(buckets[key]))

    return sortedA

print(bucket_sort([20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]))
