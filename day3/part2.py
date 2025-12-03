with open("input.txt") as f:
    lines = f.readlines()
    
ans = 0
for line in lines:
    line = line[:-1]
    dp = [[0 for _ in range(13)] for j in range(len(line))]
    dp[0][1] = int(line[0])
    for i in range(1, len(line)):
        for j in range(1, min(13, i+2)):
            dp[i][j] = max(dp[i-1][j], 10 * dp[i-1][j-1] + int(line[i]))

    ans += dp[-1][12]

print(dp[-1][12])
print(ans)
            
