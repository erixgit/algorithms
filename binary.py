def binary(lista, low, high, x):
    if low > high:
        return -1

    mid = low + ((high - low) // 2)

    if x == lista[mid]:
        return mid
    elif x < lista[mid]:
        return binary(lista, low, mid - 1, x)
    else:
        return binary(lista, mid + 1, high, x)
