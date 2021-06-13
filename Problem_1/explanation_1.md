# Explanation

Finding the Square Root of an input integer '`number`' is implemented as a **binary search**. 

The method starts by producing  the midpoint value - a floor value of the division by two: `number//2`. An initial guess is the midpoint squared. 

Then the guess is compared to the input `number`. Depending on whether the produced guess is smaller or bigger than the input `number` a new midpoint is calculated. The algorithm stops when we find an approximate square root of a given number.


---
# Complexity analysis

## Time complexity
The binary search time complexity, the basis of the solution of this problem is `O(logn)`.

## Space complexity
The algorithm uses only three additional variables (`low, mid, high`). The amount of space needed is constant w.r.t the input number. Hence, the space complexity is `O(1)`