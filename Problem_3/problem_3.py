def mergesort_reversed(list):
    """
    A mergesort implementation. The only difference is that it sorts the input list in a REVERSED ORDER.
    I.e. the elements are sorted in a DESCENDING order.

    :param list:
    :type list: list
    :return: list sorted in descending order
    :rtype: list
    """

    def _merge(left,right):
        """
        The "conquert" part of merge-sort. Compare two lists item, by item, and append the one that is greater.
        This ensures the descending order of this implementation of mergesort.

        :param left: an input sorted with mergesort
        :type left: list
        :param right: an input sorted with mergesort
        :type right: list

        :return: merged and sorted list (in descending order) or all elements from left and right lists
        """
        merged = []
        left_index,right_index = 0,0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(right[right_index])
                right_index += 1
            else:
                merged.append(left[left_index])
                left_index += 1

        merged += left[left_index:]
        merged += right[right_index:]

        return merged

    def _mergesort(items):
        """
        The "divide" part of the mergesort. Recurrently calls mergesort to split array into a single element lists
        (left and right). Merges those two lists, returning a sorted list in a descending order.
        """
        if len(items) <= 1:
            return items

        mid = len(items) // 2
        left = items[:mid]
        right = items[mid:]

        left = _mergesort(left)
        right = _mergesort(right)

        return _merge(left, right)

    return _mergesort(list)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List, where I can assume that all array elements are in the range [0, 9]
    Returns:
       (int),(int): Two maximum sums
    """

    # Special cases: O(1) time complexity
    if len(input_list)==0:
        return [None,None]
    elif len(input_list)==1:
        return [input_list[0],None]
    elif len(input_list)==2:
        return [input_list[0], input_list[1]]

    # Breaking if input list contains numbers not digits: O(n) time complexity
    for i in input_list:
        if i<0 or i>9:
            return "Input list must contain digits, not numbers"

    # First mergesort in descending order: O(n log(n)) time complexity
    input_list = mergesort_reversed(input_list)

    # O(n) SPACE complexity
    a,b = [],[]

    # O(n) time complexity
    for i,n in enumerate(input_list):
        if i%2:
            a.append(n)
        else:
            b.append(n)

    # O(n) time complexity
    a = int(  ''.join(( [ str(i) for i in a]  ))  )
    b = int(  ''.join(( [ str(i) for i in b]  ))  )

    return [a,b]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
# Pass

### My tests

# Case #0: provided test_case
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
# Pass


# Case #1: edge case: empty list
print(rearrange_digits([]))
# [None,None]

# Case #2: edge case: list of one element
print(rearrange_digits([1]))
#[1,None]

# Case #3: edge case: list of two elements:
print(rearrange_digits([5,2]))
# [5,2]

# Case 4: full set of integers
print(rearrange_digits( [i for i in range(0,10)] ))
# [86420, 97531]

# Case 5: invalid input - list containing numbers not digits
print(rearrange_digits([12,15,16]))
#return "Input list must contain digits, not numbers"
