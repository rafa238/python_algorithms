from typing import List, Union

Number = Union[int, float]
NumberList =  List[Number]

def merge(A: NumberList, p: int, q: int, r: int) -> NumberList:
    nl: int = q - p + 1
    nr: int = r - q

    L: NumberList = [0] * nl
    R: NumberList = [0] * nr
    
    for i in range(0, nl):
        L[i] = A[p + i]
 
    for j in range(0, nr):
        R[j] = A[q + 1 + j]
    
    i: int = 0
    j: int = 0
    k: int = p
    while i < nl and j < nr:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else :
            A[k] = R[j]
            j = j + 1
        k = k + 1

    while i < nl:
        A[k] = L[i]
        i = i + 1
        k = k + 1
    
    while j < nr:
        A[k] = R[j]
        j = j + 1
        k = k + 1
    
    return A

def fmerge_sort(A: NumberList, p: int, r: int) -> NumberList:
    if p >= r:
        return
    q: int = (p + r) // 2
    fmerge_sort(A, p, q)
    fmerge_sort(A, q+1, r)
    return merge(A, p, q, r)