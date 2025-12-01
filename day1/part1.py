with open("day1/input.txt") as f:
    lines = f.readlines()

dial, ans = 50, 0
for line in lines:
    direction = 1 if line[0] == 'R' else -1
    amt = int(line[1:])
    dial = (dial + direction * amt) % 100
    ans += dial == 0

print(ans)