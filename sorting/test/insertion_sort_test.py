from load_module import *
from sorting.insertion_sort import finsertion_sort

if __name__ == "__main__":
    A = [5,2,4,6,1,3]
    sorted_A = finsertion_sort(A)
    
    assert sorted_A == [1,2,3,4,5,6], "Error: Insertion Sort Test Failed"
    print("✓ Insertion Sort algorithm test success")
