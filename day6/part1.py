with open("day6/input.txt") as f:
    lines = f.readlines()

nums = []
for line in lines[:-1]:
    row = []
    parsed = line.split(" ")
    for item in parsed: 
        if item != '' and item != '\n': row.append(int(item))
    
    nums.append(row)
    

operations = []
for c in lines[-1].split(" "):
    if c != '' and c != '\n': 
        operations.append(c)

ans = 0
for i in range(len(nums[0])):
    result = 0 if operations[i] == '+' else 1
    for j in range(len(nums)):
        if operations[i] == '+':
            result += nums[j][i]

        else: result *= nums[j][i]

    ans += result

print(ans)        