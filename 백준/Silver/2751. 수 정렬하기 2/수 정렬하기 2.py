import random
import sys
from typing import List

# 입력 받기
N = int(sys.stdin.readline())
nums = []
for _ in range(N):
  nums.append(int(sys.stdin.readline().strip()))

# 병합 정렬
def merge_sort(list: List[int]) -> List[int]:
  if len(list) <= 1:
    return list

  pivot = len(list) // 2

  left = merge_sort(list[:pivot])
  right = merge_sort(list[pivot:])

  i = 0
  j = 0
  sorted_nums = []
  
  while i < len(left) and j < len(right):
    if left[i] > right[j]:
      sorted_nums.append(right[j])
      j += 1
    else:
      sorted_nums.append(left[i])
      i += 1

  while i < len(left):
    sorted_nums.append(left[i])
    i += 1
  
  while j < len(right):
    sorted_nums.append(right[j])
    j += 1

  return sorted_nums


sorted_nums = merge_sort(nums)
for num in sorted_nums:
  print(num)