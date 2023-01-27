from load_module import *
from custom_messages import show_failed_message, show_success_message
from mathematics.horners_rule import horners


if __name__ == "__main__":
    # Let's evaluate value of
    # -1 + 2x - 6x2 + 2x3 for x = 3
    A = [-1, 2, -6, 2]
    x = 3
    result = horners(A, 3)
    print(result)
    assert result == 5, show_failed_message("Horners's Rule Test 1 Failed")
    show_success_message("Horner's Rule algorithm test 1 success")
    
    # -7 + x - 3x2 + 2x3 + 5x4 for x = 3
    A = [-7, 1, -3, 2, 5]
    x = 3
    result = horners(A, 3)
    assert result == 428, show_failed_message("Horners's Rule Test 2 Failed")
    show_success_message("Horner's Rule algorithm test 2 success")
