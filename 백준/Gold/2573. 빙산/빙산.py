import sys
from enum import Enum
from collections import deque


N, M = map(int, input().split())

queue = deque()
ices = [[-1 for _ in range(M + 2)] for _ in range(N + 2)]
visited = [[0 for _ in range(M + 2)] for _ in range(N + 2)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 입력 받기
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        ices[i + 1][j + 1] = line[j]


# 초기화 함수
def reset():
    for i in range(N):
        for j in range(M):
            visited[i + 1][j + 1] = 0


# 얼어있는 칸이 있는지 확인
def check_frozen_cell():
    for i in range(N):
        for j in range(M):
            if ices[i + 1][j + 1] > 0:
                return True

    return False


# 아직 녹지 않은 빙산을 확인하는 함수
def check_ices(i, j):
    queue.clear()
    queue.append((i, j))
    visited[i][j] = 1

    while len(queue):
        x, y = queue.popleft()

        for l in range(4):
            px = x + dx[l]
            py = y + dy[l]

            if ices[px][py] > 0 and not visited[px][py]:
                visited[px][py] = 1
                queue.append((px, py))


# 빙하가 녹는 함수
def melting_ice():
    queue.clear()

    # 녹아야 할 빙하를 조사하기
    for i in range(N):
        for j in range(M):
            # 0보다 큰 경우, 4방향을 조사하면서 주변에 물이 얼마나 있는지 확인하고 큐에 넣는다.
            if ices[i + 1][j + 1] > 0:
                water_cell = 0
                for k in range(4):
                    x = i + 1 + dx[k]
                    y = j + 1 + dy[k]

                    if ices[x][y] == 0:
                        water_cell += 1

                if water_cell > 0:
                    queue.append((i + 1, j + 1, water_cell))

    # 빙하를 녹이는 작업
    while len(queue):
        i, j, water_cell = queue.popleft()

        if ices[i][j] < water_cell:
            ices[i][j] = 0
        else:
            ices[i][j] -= water_cell


def print_ices(year):
    print()
    print(f"{year}년차 얼음 현황")
    for i in range(N):
        row = []
        for j in range(M):
            row.append(ices[i + 1][j + 1])
        print(" ".join(map(str, row)))
    print()


def main():
    year = 0

    while True:
        year += 1

        melting_ice()

        if not check_frozen_cell():
            return 0

        count = 0
        for i in range(N):
            for j in range(M):
                if ices[i + 1][j + 1] > 0 and not visited[i + 1][j + 1]:
                    count += 1
                    check_ices(i + 1, j + 1)

        if count >= 2:
            return year

        reset()


print(main())
