from load_module import *
from sorting.insertion_sort import finsertion_sort
from custom_messages import show_success_message, show_failed_message

if __name__ == "__main__":
    A = [5,2,4,6,1,3]
    sorted_A = finsertion_sort(A)
    
    assert sorted_A == [1,2,3,4,5,6], show_failed_message("Insertion Sort Test Failed")
    show_success_message("Insertion Sort algorithm test success")
