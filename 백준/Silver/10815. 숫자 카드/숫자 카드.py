import sys

N = int(sys.stdin.readline())
nums = sys.stdin.readline().split()

M = int(sys.stdin.readline())
cards = sys.stdin.readline().split()

dict = {}
for num in nums:
    dict[num] = 1

res = []
for card in cards:
    if card in dict:
        res.append("1")
    else:
        res.append("0")

print(" ".join(res))
