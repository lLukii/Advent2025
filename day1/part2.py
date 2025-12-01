with open("day1/input.txt") as f:
    lines = f.readlines()

dial, ans = 50, 0
for line in lines:
    direction = 1 if line[0] == 'R' else -1
    amt = int(line[1:])
    wrap = 0
    for _ in range(amt):
        dial += direction
        if dial == -1: dial = 99
        elif dial == 100: dial = 0

        if dial == 0: wrap += 1
    
    ans += wrap

print(ans)