# versione iterativa
def binsearch(l, e):
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = int(((high + low) / 2))
        if e > l[mid]:
            low = mid + 1
        elif e < l[mid]:
            high = mid - 1
        else:
            return e
          
    return False

# prima versione ricorsiva,
# utilizza la notazione e[a:b:c] di python
# effettua un operazione di slicing sulla lista
def binsearch_recursive(l, e):
    low = 0
    high = len(l)
    mid = int(((high + low) / 2))

    if e > l[mid]:
        return binsearch_recursive(l[mid:], e)
    elif e < l[mid]:
        return binsearch_recursive(l[:mid], e)
    else:
        return e
    
# seconda vesione ricorsiva,
# richiama se stessa modificando low e high
# la lista viene copiata e non vengono effettuate
# ulteriori modifiche
def binsearch_recursive_v2(l, e):
    return __binsearch_rec_v2(l, e, 0, len(l))

def __binsearch_rec_v2(l, e, low, high):
    mid = int(((high + low) / 2))

    if e > l[mid]:
        return __binsearch_rec_v2(l, e, mid + 1, high)
    elif e < l[mid]:
        return __binsearch_rec_v2(l, e, low, mid - 1)
    else:
        return e
