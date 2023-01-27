from load_module import *
from sorting.merge_sort import merge, fmerge_sort
from custom_messages import show_success_message, show_failed_message

if __name__ == "__main__": 
    A = [2,4,6,7,1,2,3,5]
    p = 0
    r = len(A)-1
    q = p + (r-p) // 2 
    
    sorted_A = merge(A, p, q, r)
    assert sorted_A == [1,2,2,3,4,5,6,7], show_failed_message("Merge function in merge sort isn't working well")
    show_success_message("Merge function test success")

    B = [12,3,7,9,14,6,11,2]
    sorted_B = fmerge_sort(B, 0, len(B)-1)
    assert sorted_B == [2, 3, 6, 7, 9, 11, 12, 14], show_failed_message("Error: Merge Sort test failed")
    show_success_message("Merge Sort algorithm test success")
    
    

