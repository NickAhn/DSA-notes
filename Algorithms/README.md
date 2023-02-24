# Algorithms Notes
## Table of Contents

[//]: #[](#name-of-header)

1. [Searching](#searching)
2. [Sorting](#sorting)
3. [Hashing](#hashing)
4. [Greedy](#greedy)
5. [Recursion](#recursion)
6. [Backtracking](#backtracking)
7. [Dynamic Programming](#dynamic-programming)
8. [Advanced Algorithms](#advanced-algorithms)

## Searching
([Back to top](#table-of-contents))


## Sorting
### Bubble Sort
* Swap adjacent elements
* *In-place*
* *Not stable*

**Complexity Analysis**

|           |   |    |
|---------------| -- | - |
|  Best Case  | n | (list is already sorted) |
| Average Case | n^2 | | 
| Worst Case | n^2 |  |


**Pros**
* Easy to implement and understand
* O(1) space complexity

**Cons**
* Poor performance

([Back to top](#table-of-contents))

### Insertion Sort
* Like sorting playing cards in your hand
* Array is 'split' into a sorted and unsorted part, then values from the unsorted part gets picked and placed in their correct position in the sorted part
* In-place
* Stable

![Insertion Sort](imgs/insertionsort.png)

**Pseudo-code**
```
// A[0...n-1] = array of n integers
insertion_sort(A):
    for i = 1 to n-1 do:
        j = i
        while j > 0 and A[j] < A[j-1] do:
            swap A[j-1] and A[j]
            j = j - 1
```
Optimized version (only 1 swap performed per iteration)
```
// A[0...n-1] = array of n integers
insertion_sort(A):
    for i = 1 to n-1 do:
        key = A[i]
        j = i-1
        while j >= 0 and A[j] < A[j-1] do:
            swap A[j-1] and A[j]
            j = j-1
        A[j+1] = key
```

**Complexity Analysis**
|           |       |       |
|---------------| ------ | -----|
|  Best Case   | n  | (list is already sorted) |
| Average Case | n^2 | | 
| Worst Case   | n^2 |  (List is sorted in reverse order)|

**Pros**
* Simple
* O(1) space complexity (in-place)
* Faster than bubble sort (optimized version)

**Cons**
* Poor performance

**Use Cases**
* Small arrays
* Arrays that are almost sorted

## Hashing

([Back to top](#table-of-contents))


## Greedy

([Back to top](#table-of-contents))


## Recursion

([Back to top](#table-of-contents))


## Backtracking
Backtracking is often inefficient (a bit better than brute force)
* time complexity is often **exponential**
But sometimes is the only (or simplest) option.

### Example: Letter Case Permutation
* Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string
* Return a list of all possible strings we could create. Return the output in any order.
```
"a1b2", "A1b2", "a1B2", "A1B2"
```
Solution: 
1. Recursively create possibilities
3. If node is a leaf, add to answer list. Then backtrack

([Back to top](#table-of-contents))


## Dynamic Programming

([Back to top](#table-of-contents))


## Advanced Algorithms

([Back to top](#table-of-contents))