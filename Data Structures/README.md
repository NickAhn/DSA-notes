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
    <li> **Fixed Size**: You need to specify </li>
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
## Singly Linked List
## Doubly Linked List

# Stack

# Queue

# Trees

# Graphs

