with open("day2/input.txt") as f: 
    lines = f.readlines()

ranges = lines[0].split(",")
ans = 0
for cur_range in ranges:
    l, r = cur_range.split('-')
    l, r = int(l), int(r)
    for num in range(l, r+1):
        s = str(num)
        if len(s) % 2 == 1: continue
        if s[:len(s)//2] == s[len(s)//2:]: ans += num

print(ans)
        

            