# Explanation

In order to sort an array of 3 unique elements (`0,1,2`), we utilize this fact to speed up the sorting to `O(n)` time complexity **with a single list traversal**.

The idea is to iterate once, keeping pointers to the next index of `0` and `2` digits, as well as the current `i` element of the list. 

If the current element of the list is equal to `0`, then we move this zero to the position of the next `0`, while the value being replaced is moved to the current index. 

We do this accordingly with `2`s, while increasing/decreasing `0` and `2` next index positions, and increasing the current index.

The result is a single traversal through the list, without the need of additional data structures.




---

# Complexity analysis

## Time Complexity
A single traversal through the list is `O(n)`.


## Space Complexity
No additional data-depended structures need to be created, hence the space complexity is `O(1)` (constant).