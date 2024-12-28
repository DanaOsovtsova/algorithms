from collections import deque

def bfs_metki(n, matr):
    metki = [0] * n
    cur_m = 1
    visited = [False] * n

    for v in range(n):
        if not visited[v]:
            queue = deque([v])
            visited[v] = True 
            
            while queue: 
                cur = queue.popleft()
                
                metki[cur] = cur_m
                cur_m += 1

                for neighbor in range(n):
                    if matr[cur][neighbor] == 1 and not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

    return metki

with open("input.txt", "r") as input:
    n = int(input.readline().strip())
    matr = [list(map(int, input.readline().strip().split())) for _ in range(n)]

metki = bfs_metki(n, matr)

with open("output.txt", "w") as output:
    output.write(" ".join(map(str, metki)) + "\n")
