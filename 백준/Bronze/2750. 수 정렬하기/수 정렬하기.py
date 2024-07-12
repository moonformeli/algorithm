import sys

# 입력 받기
N = int(sys.stdin.readline())
nums = []
for _ in range(N):
  nums.append(int(sys.stdin.readline().strip()))

# 삽입 정렬
for i in range(1, len(nums)):
  if nums[i] < nums[i - 1]:
    for j in range(i, 0, -1):
      if nums[j] < nums[j - 1]:
        tmp = nums[j - 1]
        nums[j - 1] = nums[j]
        nums[j] = tmp
      else:
        break
  
for num in nums:
  print(num)