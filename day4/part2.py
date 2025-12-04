with open("day4/input.txt") as f:
    lines = f.readlines()

grid = []
for line in lines:
    grid.append(line.strip())

def check(i, j):
    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == '@':
        return True
    
    return False

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

ans = 0
while True:
    new_grid = [['.' for i in range(len(grid[0]))] for j in range(len(grid))]
    ok = True
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            adj = 0
            if grid[i][j] == '@':
                for k in range(8):
                    adj += check(i+dx[k], j+dy[k])
            
                if adj < 4:
                    new_grid[i][j] = '.'
                    ans += 1
                    ok = False
                    continue
            
            new_grid[i][j] = grid[i][j]
    
    grid = new_grid
    if ok: break

print(ans)
            
            