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

dfs([], 1)