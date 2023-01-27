from typing import List, Union

Number = Union[int, float]
NumberList =  List[Number]

def finsertion_sort(A: NumberList) -> NumberList:
    n: int = len(A)
    for i in range(1, n):
        key: Number = A[i]
        j: int = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A