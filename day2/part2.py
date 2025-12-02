with open("day2/input.txt") as f: 
    lines = f.readlines()

ranges = lines[0].split(",")
ans = 0
for cur_range in ranges:
    l, r = cur_range.split('-')
    l, r = int(l), int(r)
    for num in range(l, r+1):
        s = str(num)
        invalid = False
        for idx in range(1, len(s) // 2 + 1):
            ok = True
            prefix = s[:idx]
            for i in range(0, len(s), idx):
                if s[i:i+idx] != prefix:
                    ok = False
                    break
            
            if ok:
                invalid = True
                break
        
        ans += num if invalid else 0


print(ans)
        

            