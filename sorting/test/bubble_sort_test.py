from load_module import *
from sorting.bubble_sort import fbubble_sort
from custom_messages import show_failed_message, show_success_message

if __name__ == "__main__":
    A = [2,4,6,7,1,2,3,5]
    fbubble_sort(A)
    assert A == [1,2,2,3,4,5,6,7], show_failed_message("Error: Bubble Sort test 1 failed")
    show_success_message("Bubble Sort test 1 success")

    A = [5,2,4,6,1,3]
    fbubble_sort(A)
    assert A == [1,2,3,4,5,6], show_failed_message("Bubble Sort Test 2 Failed")
    show_success_message("Bubble Sort algorithm test 2 success")