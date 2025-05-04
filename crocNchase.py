from collections import deque

def is_enclosed(lake, x, y):
    if lake[x][y] == 1:
        return False  
    
    n = len(lake)
    visited = set()
    q = deque([(x, y)])
    visited.add((x, y))
    
    while q:
        i, j = q.popleft()
        
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            if lake[i][j] == 0:
                return False
        
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if (ni, nj) not in visited and lake[ni][nj] == 0:
                    visited.add((ni, nj))
                    q.append((ni, nj))
    
    return True

def shortestboundary(lake, x, y):
    if lake[x][y] == 1:
        return 0  
    
    n = len(lake)
    visited = set()
    q = deque([(x, y, 0)])  
    visited.add((x, y))
    
    while q:
        i, j, steps = q.popleft()
        
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if lake[ni][nj] == 1:
                    return steps + 1
                if (ni, nj) not in visited and lake[ni][nj] == 0:
                    visited.add((ni, nj))
                    q.append((ni, nj, steps + 1))
    
    return -1  

def crocodile_prey(lake, x, y):
    if not is_enclosed(lake, x, y):
        return -1
    
    return shortestboundary(lake, x, y)

lake1 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
print(crocodile_prey(lake1, 3, 3))  

lake2 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
print(crocodile_prey(lake2, 0, 0))  