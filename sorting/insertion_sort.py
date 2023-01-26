from typing import List, Union

NumberList =  List[Union[int, float]]

def finsertion_sort(A: NumberList) -> NumberList:
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A