with open("input.txt") as f:
    lines = f.readlines()
    
ans = 0
for line in lines:
    max_num = 0
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            max_num = max(max_num, int(line[i]+line[j]))
    
    ans += max_num
    
print(ans)