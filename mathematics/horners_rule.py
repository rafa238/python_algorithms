from typing import List, Union

Number = Union[int, float]
NumberList =  List[Number]

"""
A: Polynomial of the form (a0, a1*x1, a2*x2, .. , an*xn)
x: Number to evaluate A(x)
"""
def horners(A: NumberList, x: Number):
    n: int = len(A) - 1
    p: Number = 0
    #let's traverse A from A[n] to A[0]
    for i in range(n, 0-1, -1):
        p = A[i] + x * p

    return p