def biSearch(lista, el):
    """Necesita ser una lista ordenada""" 

    ub = len(lista) -1
    lb = 0

    while(lb < ub+1):
        mid = (ub + lb) // 2

        if lista[mid] == el:
            return True
        elif lista[mid] > el:
            ub = mid -1
        elif lista[mid] < el:
            lb = mid +1

    return False


