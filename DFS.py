def dfs_metki(n, matr):
    metki = [0] * n 
    cur_m = 1 
    visited = [False] * n 

    def dfs(v):
        nonlocal cur_m 
        visited[v] = True 
        
        metki[v] = cur_m
        cur_m += 1

        for neighbor in range(n):
            if matr[v][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)  #рекурсивно DFS для соседа

    for v in range(n): 
        if not visited[v]:
            dfs(v)

    return metki

with open("input.txt", "r") as input:
    n = int(input.readline().strip())
    matr = [list(map(int, input.readline().strip().split())) for _ in range(n)]

metki = dfs_metki(n, matr)

with open("output.txt", "w") as output:
    output.write(" ".join(map(str, metki)) + "\n")
