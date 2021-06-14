# Explanation
Rearranging Array Elements to form two numbers such that their sum is maximum.

The implementation uses a "reversed" merge sort. I.e. a mergesort that sorts an input array in a descending (reversed) order. This requires `O(n log(n)` time complexity. 

With sorted array, we loop over each item. In order to maximize sum, we have to start from the biggest digit present, i.e. the first element in the sorted list.

We append the digits to helper lists `a` and `b`, alternating between them after each iteration. This ensures that these two lists differ maximally by one digit. This requires `O(n)` space complexity. 

Finally, the lists of digits are formatted in such a way, as to return an integer, representing the concatenation of those two lists.

---

# Complexity analysis
As discussed above:
## Time complexity
`O(n log n)` as we use mergesort to sort the input array. This is the most computationally expensive operation.
## Space complexity
`O(n)` - as we're creating two lists of size `n/2`. Hence the total space complexity is `O(n)`.
