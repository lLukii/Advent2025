with open("day8/input.txt") as f:
    lines = f.readlines()

points = [line.strip().split(",") for line in lines]
n = len(points)
comp_size = 0

connections = []
adj = [[] for _ in range(n)]
vis = [False for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        x1, y1, z1 = list(map(int, points[i]))
        x2, y2, z2 = list(map(int, points[j]))
        dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
        connections.append([dist, i, j])

def dfs(cur):
    vis[cur] = True
    for v in adj[cur]:
        if not vis[v]: 
            dfs(v)

connections.sort()
idx = 0
for connection in connections:
    vis = [False for _ in range(n)]
    adj[connection[1]].append(connection[2])
    adj[connection[2]].append(connection[1]) 
    num_comp = 0
    for i in range(n):
        if not vis[i]:
            num_comp += 1
            dfs(i)

    if num_comp == 1: 
        print(int(points[connection[1]][0]) * int(points[connection[2]][0]))
        break
