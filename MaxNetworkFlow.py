def bfs(C, F, s, t):
    queue = [s]
    paths = {s: []}
    if s == t:
        return paths[s]
    while queue:
        u = queue.pop(0)
        for v in range(len(C)):
            if (C[u][v] - F[u][v] > 0) and v not in paths:
                paths[v] = paths[u] + [(u,v)]
                if v==t:
                    return paths[v]
                queue.append(v)
    return None

def solution(entrances, exits, path):
    max = float("inf")
    n = len(path)
    s = n
    t = n+1
    for row in range(n):
        path[row].append(0)
        path[row].append(max if row in exits else 0)

    n += 2
    path.append([(max if x in entrances else 0) for x in range(n)])
    path.append([0]*n)

    F = [[0]*n for i in range(n)]

    paths = bfs(path, F, s, t)
    while paths != None:
        flow = min(path[u][v] - F[u][v] for u,v in paths)
        for u,v in paths:
            F[u][v] += flow
            F[v][u] -= flow
        paths = bfs(path, F, s, t)
    return sum(F[s][i] for i in range(n))