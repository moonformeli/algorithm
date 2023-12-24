# d(n) = n과 n의 각 자리수를 더하는 함수
# ex: d(75) = 75 + 7 + 5 = 87
# n = d(n) 의 생성자

# 10,001 개의 인덱스를 가진 배열 만들기
# index 값이 True - self number, 값이 False - non self number
MAX = 10000
nums = [True] * (MAX + 1)

nums[1] = True


def get_summed_num(num: int) -> int:
    num_to_str = str(num)

    acc = 0
    for digit in num_to_str:
        acc += int(digit)

    return num + acc


for i, _ in enumerate(nums):
    next_num = get_summed_num(i)

    if next_num <= MAX:
        nums[next_num] = False

for i, _ in enumerate(nums):
    if nums[i]:
        print(i)
