# Explanation

Search in a Rotated Sorted Array is implemented as a binary search on two sorted arrays.

First, the pivot point is found utilizing the fact that the input array is sorted, but shifted (i.e. "pivoted"). The strategy is similar to a binary search, only the condition is different. We check whether the beginning of the considered interval is smaller than the end. If it is - the interval is sorted, and the pivot point is at the start.

If the beginning of the list is bigger than the end, we anticipate a pivot point in between this interval. A midpoint is calculated. Next we discard half of the array, checking whether the range from `start` to `midpoint` or from `midpoint` until `end` is sorted. 

After obtaining the pivot, we can calculate two binary searches: 1) one on the array from start until pivot, 2) second on the array from the pivot until the end of the array.

The worst case scenario is when the input array has a pivot in the middle. However, the time complexity still simplifies to `O(log n)`. 

As `O(log 0.5n) + O(log 0.5n)` = ` O( log(  0.25n**2)  )` = `O (2 log(0.25n))` $\approx$ `O(log n)`.

We see the time complexity remains that of binary search. 

---

# Complexity analysis

## Time complexity
As discussed above, time complexity of the algorithm is `O(log n)`

## Space complexity 
We do not create any intermediate data structures to hold the results. A constant amount of memory is needed to run the search algorithm. Therefore, the space complexity is `O(1)`.