from sys import argv
import bubble_sort
import bucket_sort
import insertion_sort
import quick_sort
import selection_sort
import merge_sort
import random
import sys
import time

arrlen = 100

if len(argv) < 3:
    arrlen = int(argv[1])

print(" ** array length: {}".format(arrlen))
print(" ** generating random array...")

random.seed(1)
randarr = [ random.randint(0, 100) for _ in range(arrlen) ]

test_on = {
        "BubbleSort": bubble_sort.bubble_sort, 
        "BucketSort": bucket_sort.bucket_sort, 
        "InsertionSort": insertion_sort.insertion_sort, 
        "QuickSort": quick_sort.quick_sort, 
        "SelectionSort": selection_sort.selection_sort,
        "MergeSort": merge_sort.merge_sort
        }

for key in test_on:
    print(" --> {}".format(key))
    bak = randarr
    algorithm_impl = test_on[key]

    before = time.time()
    algorithm_impl(bak)
    now = time.time()

    print("\telapsed time: {}s".format(now - before))
