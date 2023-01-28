from typing import List, Union

Number = Union[int, float]
NumberList =  List[Number]

def exchange(A: NumberList, i, j):
    aux: Number = A[i]
    A[i] = A[j]
    A[j] = aux

def fbubble_sort(A: NumberList):
    n: int = len(A) - 1
    for _ in range(n):
        for j in range(n, 0, -1):
            if A[j] < A[j-1]:
                exchange(A, j, j-1)

fbubble_sort([10,5,7,8,3,2,1,3,0])