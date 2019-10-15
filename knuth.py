import sys

def knuth(a,b,n):
    print("call knuth({},{},{})".format(a,b,n))
    if n > 0 and b == 0: # 1
        return 1 # 1
    elif n == 1: # 1
        return a ** b # 2

    return knuth(a, knuth(a, b - 1, n), n - 1)

if len(sys.argv) < 4:
    print("{} a b n".format(sys.argv[0]))
    sys.exit(1)

sys.setrecursionlimit(100000)
print(knuth(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
