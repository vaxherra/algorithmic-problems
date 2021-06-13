def sqrt(number=None):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number is None or number < 0:
        return None

    low = 1
    high = number

    while low <= high:
        mid = (low+high)//2
        mid2 = mid**2  # a mid value squared

        if mid2 == number:
            return mid
        elif mid2 > number:
            high = mid-1
        else:
            low = mid+1

    return high

""" TESTING """
# CASE #1: a square root of 1296 is 36 (clean example)
print(sqrt(1296))
# 36

# CASE #2: edge case: empty input
print(sqrt())
# None

# CASE #3:edge case, negative input
print(sqrt(-123))
# None

# CASE #4: sqrt(1300) = 36.0555127546, so 36 in this implementation
print(sqrt(1300))
# 36

# CASE #5: sqrt(123456789) = 11111.1110606
print(sqrt(123456789))
# 11111