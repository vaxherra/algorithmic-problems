def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
    :param input_list: Input array to search
    :type input_list: list

    :param number:  the target
    :type number: int

    :return: Index or -1 for valid inputs, 'None' for invalid inputs
    :rtype: int or None

    """

    # Handling edge and base cases
    if type(input_list)!=list:
        return None
    elif len(input_list) == 0:
        return None
    elif len(input_list)== 1:
        return 0 if input_list[0]==number else -1

    # find pivot
    p = find_pivot(input_list)

    # perform binary search in two halves split by pivot
    # this is equivalent to a full binary search in the number of operations needed
    bs1 = binary_search(input_list[:p],number)
    if bs1 is None or bs1==-1:
        bs2 =  binary_search(input_list[p:],number)
        if bs2 is None or bs2==-1:
            return bs2
        else:
            return bs2+p
    else:
        return bs1


def find_pivot(input_list):
    """Find the pivot point of the sorted yet "shifted" list.
    A simple divide and conquer strategy to find the pivot point of the list.

    Time complexity O(log n)

    :param input_list: a sorted and pivoted list (i.e. "shifted")
    :type input_list: list

    :return: an index of the list being the pivot point
    :rtype: int
    """

    start = 0
    end = len(input_list)-1

    while start<=end:
        mid = (start+end)//2

        if input_list[start] <= input_list[end]:
            return start
        # the interval start-mid is sorted, then a pivot point is somewhere between mid-end
        elif input_list[start] <= input_list[mid]:
            start = mid+1
        # the interval mid-end is sorted, then a pivot point is somewhere between start-mid
        else:
            end = mid

    return start

def binary_search(input_list,x):
    """Binary search implementation

    :param input_list: an input sorted list of elements
    :param x: a number searched
    :return: index of the number found or -1 if not found
    """
    low,high = 0, len(input_list)-1

    while low <= high:
        mid = (low+high)//2

        if input_list[mid]==x:
            return mid
        elif x > input_list[mid]:
            low = mid+1
        else:
            high = mid - 1
    return -1



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


# CASE #1: invalid input type
print(rotated_array_search(input_list={1:2}, number=2))
# None

# CASE #2: empty list
print(rotated_array_search(input_list=[],number=5))
# None

# CASE #3: list with a single element (matching)
print(rotated_array_search(input_list=[1],number=1))
# 0

# CASE #4: list with a single element (non-matching)
print(rotated_array_search(input_list=[1],number=2))
# -1

# CASE #5: bigger list
# Create an array of 100 elements, and arrange them like this:
# a = [246, 247, ... 999, 0, 1, ... 245]
# the pivot is at the 246th index position
a = [i for i in range(0,1000)]
a = a[246:]+a[:246] # an artificial pivot point

print(rotated_array_search(a,1000)) # numbers are from 0-999 only, 1000 is not present
# None

print(rotated_array_search(a,999)) # 999th is at the 1000-246-1 position
# 753

print(rotated_array_search(a,245)) # 245 number is at the last position
# 999

print(rotated_array_search(a,246)) # 246 number is at the first position
# 0

