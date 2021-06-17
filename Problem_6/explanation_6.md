# Explanation
Max and Min in a Unsorted Array is implemented as a single traversal through the list. Two tracking variables (`min_v/max_v`) store initially the first value of the list. Next each value from the list is compared with these min/max variables and are replaced after successive comparisons of iterated elements from the list.

---

# Complexity analysis

## Time complexity
`O(n)` - a single traversal through the list, with a constant amount of work per each iteration.

## Space complexity
`O(1)` - constant memory required, as we only keep track of two (min/max) variables.