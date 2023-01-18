# Algorithms Notes
# Table of Contents

[//]: #[](#name-of-header)

1. [Searching](#searching)
2. [Sorting](#sorting)
3. [Hashing](#hashing)
4. [Greedy](#greedy)
5. [Recursion](#recursion)
6. [Backtracking](#backtracking)
7. [Dynamic Programming](#dynamic-programming)
8. [Advanced Algorithms](#advanced-algorithms)

# Searching
## Depth-First Search (DFS)
* Recursive backtracking algorithm
* Explore graph as far as possible along each branch. If a dead-end is found, backtrack until we see a path not attempted before (then repeat until done).

DFS usually uses a stack data structure. Each node of the graph will fall into two categories:
* Visited
* Not visited

### Algorithm:
1. Start at any vertex
2. Take top item of the stack and add it to the visited list
3. Add adjacent nodes that have not been visited to stack
4. repeat steps 2 and 3 until done

### Implementation
* Python
    ```
    graph = {
        1 : [2, 3],
        2 : [5, 6],
        3 : [4],
        4 : [5, 6],
        5 : [],
        6 : []
    }

    def dfs(visited: list[int], v: int):
        if v in visited:
            return
        
        visited.append(v)
        print(v)
        for node in graph[v]:
            dfs(visited, node)
        
        return
    ```


([Back to top](#table-of-contents))

# Sorting

([Back to top](#table-of-contents))


# Hashing

([Back to top](#table-of-contents))


# Greedy

([Back to top](#table-of-contents))


# Recursion

([Back to top](#table-of-contents))


# Backtracking

([Back to top](#table-of-contents))


# Dynamic Programming

([Back to top](#table-of-contents))


# Advanced Algorithms

([Back to top](#table-of-contents))