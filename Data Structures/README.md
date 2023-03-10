# Data Structure Notes
# Table of Contents

[//]: #[](#name-of-header)

1. [Arrays (Static/Dynamic)](#arrays-staticdynamic)
2. [Linked Lists](#linked-lists)
3. [Stack](#stack)
4. [Queue](#queue)
5. [Trees](#trees)
6. [Graphs](#graphs)

# Arrays (Static/Dynamic)
## Static Arrays
Arrays store homogeneous data sequentially in memory.

Each element has an **index**, starting at 0.

### Strengths
* **Fast look-ups**: O(1) Time regardless of length
* **Fast Appending**: O(1) time to add element in the **end** of the array
* **Cache-Friendly**: Since data is stored sequentially

### Weaknesses
<ul>
    <li> <strong>Fixed Size</strong>: You need to specify the length of the array </li>
    <li>
    <strong>Costly Insertion/Deletion</strong>: In order to insert/delete elements, the rest of the elements need to "scoot over" to fill the empty cell. Worst case being O(n) time when preppending or deleting 1st element.

Array Insertion             |  Array Deletion
:-------------------------:|:-------------------------:
![](/Data%20Structures/imgs/arrays-insertion.png)  |  ![](/Data%20Structures/imgs/arrays-deletion.png)
</li>
</ul>

## Dynamic Arrays
Arrays with *automatic resizing* 

### Strengths
* **Fast Look-ups**: O(1) Time
* **Variable Size**: Array will expand as you add elements to it
* **Cache-Friendly**: Since data is stored sequentially

### Weaknesses
* **Costly Insertion/Deletion**: Just like static Arrays, data needs to move when inserting/deleting elements that are not in the end of the array.

([Back to top](#table-of-contents))

# Linked Lists
Linked List is a linear data structure in which elements are not stored at contiguous memory locations. Rather, the items in a linked list are *linked* through pointers.

Items in a linked list are called **nodes**, the first node being the **head** and the last node being the **tail**.

Analogy: linked lists are like a chain of paper clips. 

### Strengths
* **Dynamic Size**: You can increase/decrease the size of the array during runtime.
* **Faster insertion/deletion operations**: To insert/delete, you don't need to shift elements. Only change the pointer from one node to another. 
Adding/removing elements in the head or tail takes O(1) time.
* **Implementation**: Linear data structures like stacks and queues are easily implemented with linked lists. They also only need fast operations in the ends, so linked lists are ideal.
* **No memory wastage**: The size of a linked list is dynamic so there is no need to pre-allocate memory.

### Weaknesses
* **Costly look-ups**: *Random access* is not possible due to its dynamic memory allocation. To access the ith element, you need to traverse the array from the head, taking O(i) time.
* **Memory usage**: More memory is required in a linked list compared to an array. A pointer not only store the address of another node, but it also requires extra memory for itself.

### Uses
* When you need fast insertion/deletion of elements in a list
* When lookups and ordering is not extremely important
* The decision between arrays and linked lists comes down to the insertion/deletion cost, search cost (and space cost, if comparing to a static array).


## Singly Linked List
Singly Linked Lists only have one pointer linking one node to another. Therefore, items can only be navigated forward.
![Singly Linked List](imgs/singly-linked-list.png)

### Implementation

<<<<<<< HEAD
=======
[``` singly-linked-list.py ```](https://github.com/NickAhn/DSA-notes/blob/main/Data%20Structures/singly-linked-list.py)

>>>>>>> 3510593b7338dce14ed79bc2781a5c3b2ecf0911
([Back to top](#table-of-contents))

## Doubly Linked List

([Back to top](#table-of-contents))

# Stack
Stack is a data structure that stores items in a First-in, last-out (FILO) order. As the name implies, you can imagine that you are stacking items in a container, and you can only add or remove items from the top of the stack.

![stack](imgs/stack.png)

Its main opeartions are:
* pop() - remove top of stack (last element)
* push() - add element to stack
* peek() - see top element of stack

## Analysis
### Space and Time complexities 
|             |  Worst Case |
| ----------- | ----------- |
| space       |   O(n)     |
| push        |   O(1)      |
| pop         |   O(1)      |
| peek        |   O(1)      |
## Strenghts
* Fast operations

## Weaknesses
* Random Accessing is not possible

## Use Cases
* Helps you manage data in a more particular way than arrays and lists.
* Good for when **LIFO** principle is needed (ex: *DFS*)

## Implementation
You can implement stacks with both dynamic arrays or linked lists.
|           |   Push |  Pop      |
| --------- | --------- | --------|
| Linked Lists   | Insert at head | remove at head      |
| Dynamic Arrays | append         | remove last element |

([Back to top](#table-of-contents))

# Queue

# Trees

# Graphs

