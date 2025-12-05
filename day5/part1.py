with open("day5/input.txt") as f:
    lines = f.readlines()

seg, ingredients = [], []
newline = False
for line in lines:
    if line == '\n': newline = True
    elif not newline:
        a, b = list(map(int, line.split('-')))
        seg.append([a, b])
    else:
        ingredients.append(int(line))

ans = 0
for ing in ingredients: 
    for s in seg:
        if s[0] <= ing <= s[1]: 
            ans += 1
            break

print(ans)