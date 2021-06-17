import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) == 0:
        return None, None

    min_v, max_v = ints[0], ints[0]

    for num in ints[1:]:
        # in case null/empty values (not integers or floats), omit this element
        if not(type(num) == int or type(num) == float):
            continue
        if num < min_v:
            min_v = num
        if num > max_v:
            max_v = num

    return min_v, max_v


# Example Test Case of Ten Integers
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# Pass

# My test cases

# CASE #1 (edge case): Empty list, does not have min/max : returns a tuple of (None,None)
print(get_min_max([]) == (None, None))
# True

# CASE #2: List containing Null values,
alist = [1, 2, 3, None, 4, None, 5]
print(get_min_max(alist) == (1, 5))
# True

# CASE #3 List of all None values
aList = [None for i in range(10)]
print(get_min_max(aList) == (None, None))
# True

# CASE #4 (edge case): big input of randomly shuffled 20 million integers
a = [i for i in range(int(-1e6), int(1e6)+1, 1)]
random.shuffle(a)
print(get_min_max(a) == (-int(1e6), int(1e6)))
# True

# CASE #5 (edge case): input of identical numbers: min==max
a = [22 for i in range(100)]
print(get_min_max(a) == (22, 22))
# True

# CASE #6: a simple test case
a = [5, 4, 2, 1, -10, 12, 15, 235]
print(get_min_max(a) == (-10, 235))
# True
