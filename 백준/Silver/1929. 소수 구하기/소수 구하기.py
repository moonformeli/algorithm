# 에라토스테네스의 체 이용

m, n = map(int, input().split())

MAX = n
arr = [True] * (MAX + 1)

# 1은 소수가 아님
arr[1] = False

for i in range(2, len(arr) + 1):
    k = 2

    while i * k <= MAX:
        arr[i * k] = False
        k += 1

for i in range(m, n + 1):
    if arr[i]:
        print(i)
