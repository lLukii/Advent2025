with open("day7/input.txt") as f:
    lines = f.readlines()

grid = [[c for c in line.strip()] for line in lines]
n, m = len(grid), len(grid[0])

ans = 0
for i in range(1, n):
    for j in range(m):
        if grid[i-1][j] == 'S':
            if grid[i][j] == '^':
                corners = 0
                if j > 0:
                    tmp = grid[i][j-1] 
                    grid[i][j-1] = 'S'
                    corners += tmp == 'S'

                if j < m - 1: 
                    tmp = grid[i][j+1]
                    grid[i][j+1] = 'S'
                    corners += tmp == 'S'
                
                ans += corners < 2
                
            else: 
                grid[i][j] = 'S'

print(ans)
        
            
        
        