# left: LSB
# right: MSB

def binary_increment(B):
    k = len(B)
    j = 0

    while j < k and B[j] == 1:
        B[j] = 0
        j += 1

    if j == k:
        j = 0

    B[j] = 1

    return B

s = [0,0,0,0]
for r in range(16):
    print(s)
    s = binary_increment(s)

# overflow
print(s)
