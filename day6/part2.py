rows = [line.rstrip() for line in open('day6/input.txt', 'r')]
maxl = max([len(x) for x in rows])

part2 = 0
p = 0
for x in range(maxl):
    b = ''
    for y in range(len(rows)):
        b += rows[y][x] if x < len(rows[y]) else ' '
    
    if b.strip() == '':
        part2 += p
        p = 0
        continue

    n = int(b[:-1])
    if b[-1] != ' ':
        isadd = b[-1] == '+'
        p = 0 if isadd else 1
    
    if isadd:
        p += n
        p *= n

part2 += p
print(part2)