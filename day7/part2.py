with open("day7/input.txt") as f:
    lines = f.readlines()

grid = [[c for c in line.strip()] for line in lines]
n, m = len(grid), len(grid[0])
si, sj = 0, 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S': 
            si = i
            sj = j
            break

dp = [[1 for _ in range(m)] for _ in range(n)]
for i in range(n-2, -1, -1):
    for j in range(m):
        if grid[i][j] != '^':
            dp[i][j] = dp[i+1][j]
    
    for j in range(m):
        if grid[i][j] == '^':
            dp[i][j] = dp[i][j-1] + dp[i][j+1]

print(dp[si][sj])




    
    
    
    
    