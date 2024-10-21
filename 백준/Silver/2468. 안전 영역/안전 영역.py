import sys
from enum import Enum
from collections import deque


class Area(Enum):
    WET = -1
    DRIED = 0
    WALL = 1


N = int(input().strip())

area = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
mark = [[Area.WALL for _ in range(N + 2)] for _ in range(N + 2)]

visited = set()

for i in range(N):
    line = list(map(int, input().split()))

    for j in range(N):
        mark[i + 1][j + 1] = Area.DRIED
        area[i + 1][j + 1] = line[j]


def reset():
    visited.clear()

    for i in range(N):
        for j in range(N):
            mark[i + 1][j + 1] = Area.DRIED


# 물에 잠기지 않은 영역을 표시하는 함수
def mark_dried_area(i, j):
    queue = deque()
    queue.append((i, j))
    visited.add((i, j))

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    while len(queue):
        a, b = queue.popleft()

        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b

            if mark[x][y] == Area.DRIED and not (x, y) in visited:
                visited.add((x, y))
                queue.append((x, y))


# 물에 잠기지 않은 영역의 개수를 구하는 함수
def get_dried_area_count():
    count = 0

    for i in range(N):
        for j in range(N):
            if mark[i + 1][j + 1] == Area.DRIED and not (i + 1, j + 1) in visited:
                mark_dried_area(i + 1, j + 1)
                count += 1

    return count


# 물에 잠기게하는 함수
def wet_area(height):
    for i in range(N):
        for j in range(N):
            if area[i + 1][j + 1] <= height and mark[i + 1][j + 1] == Area.DRIED:
                mark[i + 1][j + 1] = Area.WET


# 2차원 형태로 mark 배열을 보기 좋게 출력하는 함수
def print_mark():
    for i in range(N + 2):
        row = []
        for j in range(N + 2):
            row.append(mark[i][j].value)  # Enum의 값을 숫자로 변환하여 출력
        print(" ".join(map(str, row)))
    print()  # 줄바꿈


def main():
    height = -1
    max_count = 0

    while True:
        height += 1

        wet_area(height)
        count = get_dried_area_count()

        if count == 0:
            break

        if count >= max_count:
            max_count = count

        reset()

    return max_count


print(main())
