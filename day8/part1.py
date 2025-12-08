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

connections.sort()
for connection in connections[:1000]:
    adj[connection[1]].append(connection[2])
    adj[connection[2]].append(connection[1])

def dfs(cur):
    global comp_size
    comp_size += 1
    vis[cur] = True
    for v in adj[cur]:
        if not vis[v]: 
            dfs(v)

sizes = []
for i in range(n):
    if not vis[i]:
        comp_size = 0
        dfs(i)
        sizes.append(comp_size)

sizes.sort(reverse=True)
print(sizes[0] * sizes[1] * sizes[2])