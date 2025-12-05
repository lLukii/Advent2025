with open("day5/input.txt") as f:
    lines = f.readlines()

seg = []
for line in lines:
    a, b = list(map(int, line.split('-')))
    seg.append([a, 0]) # 0 start
    seg.append([b, 1]) # 1 end

seg.sort()
ans, num_start = 0, 0
disjoint = 1
for i in range(len(seg)-1):
    num_start += 1 if seg[i][1] == 0 else -1
    if seg[i+1][1] == 0 and seg[i][1] == 1 and num_start == 0: 
        disjoint += 1
        continue 

    ans += seg[i+1][0] - seg[i][0]

print(ans + disjoint)

