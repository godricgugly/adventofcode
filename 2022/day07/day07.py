from collections import defaultdict

puzzle = list(i.strip().split() for i in open("puzzle07").readlines())

directorySize = defaultdict(int)
stack = []
for row in puzzle:
    if row[0] == '$' and row[1] == 'cd' and row[2] == '..':
        stack.pop()
    if row[0] == '$' and row[1] == 'cd'and row[2] != '..':
        stack.append(row[2])
        if row[2] == '/':
            stack = []
    if row[0].isdigit():
        for i in range(len(stack) + 1):
            path = "/" + "/".join(stack[:i])
            directorySize[path] += int(row[0])

part1Sizes = []
for num in directorySize.values():
    if num <= 100000:
        part1Sizes.append(num)
print('Part 1:', sum(part1Sizes))

### Part 2

freeSpace = 70000000 - directorySize['/']
neededSpace = 30000000 - freeSpace

part2Size = directorySize['/']
for num2 in directorySize.values():
    if part2Size > num2 >= neededSpace:
        part2Size = num2
print('Part 2:', part2Size)
