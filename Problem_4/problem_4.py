def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    if type(input_list)!=list:
        return "Inappropriate input type"

    next0,next2 = 0, len(input_list)-1 # helper indices, init: next 0 at the beginning, next 2 at the end
    i = 0  # index, used for A SINGLE TRAVERSAL

    # O(n) AND A SINGLE LIST TRAVERSAL
    while i <= next2:

        if input_list[i] == 0:  # if at current index we have 0, then...
            input_list[i]=input_list[next0]  # at current index store the value that is replacing 0
            input_list[next0]=0  # place 0 at the next 0'th position
            next0+=1  # and increment both counters
            i+=1
        elif input_list[i] == 2:
            input_list[i]=input_list[next2]
            input_list[next2] = 2
            next2-=1
        else:  # we have 1, so leave it, as sorting only 0s and 2s, will place 1s in place
            i+=1

    return input_list



def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# Pass

# My tests

# CASE #1: edge case - empty list input
print(sort_012([]))
# []

# CASE #2: edge case - null input
print(sort_012(None))
#"Inappropriate input type"

# CASE #3: edge case - big array 1 million elements
import numpy as np
test_function(list(np.random.choice([0,1,2],size=int(1e6))))
# Pass

# CASE #4: manual case
print(sort_012([0,1,2,0,1,2,0,0])==[0,0,0,0,1,1,2,2])
# True
