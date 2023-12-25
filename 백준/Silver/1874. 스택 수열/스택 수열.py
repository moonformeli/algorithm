import sys

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

i = 1
head = 0
stack = []
commands = []
while head < n:
    next_num = nums[head]

    while i <= next_num:
        stack.append(i)
        i += 1
        commands.append("+")

    if stack[-1] == next_num:
        stack.pop(-1)
        commands.append("-")
    head += 1

if len(stack) != 0:
    print("NO")
else:
    for command in commands:
        print(command)
