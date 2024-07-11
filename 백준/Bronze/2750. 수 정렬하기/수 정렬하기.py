import sys

# 입력 받기
N = int(sys.stdin.readline())
nums = []
for _ in range(N):
  nums.append(int(sys.stdin.readline().strip()))

# 버블 정렬
for i in range(len(nums)):
  for j in range(len(nums) - i - 1):
    if nums[j] > nums[j + 1]:
      tmp = nums[j + 1]
      nums[j + 1] = nums[j]
      nums[j] = tmp

for num in nums:
  print(num)