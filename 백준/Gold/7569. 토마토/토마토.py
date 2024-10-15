import sys
from enum import Enum
from collections import deque


class Tomato(Enum):
    NOTHING = -1  # 들어있지 않음
    UNRIPE = 0  # 익지 않은 토마토
    RIPE = 1  # 익은 토마토


class Visit(Enum):
    UNVISITED = 0
    VISITED = 1


# M: 가로 칸의 수
# N: 세로 칸의 수
# H: 쌓아올려지는 상자의 수
M, N, H = map(int, input().split())

# 전체 토마토 수 = 전체 칸의 수 - 아무것도 없는 칸의 수
total_tomato = H * N * M

# 토마토 입력받기
boxes = [
    [[Tomato.NOTHING for _ in range(M + 2)] for _ in range(N + 2)] for _ in range(H + 2)
]
visited = [
    [[Visit.UNVISITED for _ in range(M + 2)] for _ in range(N + 2)]
    for _ in range(H + 2)
]
for h in range(H):
    for n in range(N):
        line = list(map(int, input().split()))
        for m in range(M):
            tomato = Tomato(line[m])
            if tomato == Tomato.NOTHING:
                total_tomato -= 1

            boxes[h + 1][n + 1][m + 1] = tomato


# 디버깅용 출력
def printBoxes(day):
    print(f"----Day: {day}일 째 토마토 상자----")

    for h in range(H):
        for n in range(N):
            for m in range(M):
                print(boxes[h + 1][n + 1][m + 1].value, end=" ")
            print()


# 토마토가 익는 함수
def water(day, queue: deque, ripe_count):
    new_queue = deque()
    count = ripe_count

    dh = [1, -1, 0, 0, 0, 0]
    dn = [0, 0, 1, -1, 0, 0]
    dm = [0, 0, 0, 0, -1, 1]

    while len(queue):
        h, n, m = queue.popleft()

        for i in range(6):
            posH = h + dh[i]
            posN = n + dn[i]
            posM = m + dm[i]

            if (boxes[posH][posN][posM] == Tomato.UNRIPE) and (
                visited[posH][posN][posM] == Visit.UNVISITED
            ):
                boxes[posH][posN][posM] = Tomato.RIPE
                visited[posH][posN][posM] = Visit.VISITED
                count += 1
                new_queue.append((posH, posN, posM))

    return new_queue, count


# 익은 토마토가 들어있는 칸 찾기
def find_ripe_tomato():
    queue = deque()

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if (
                    boxes[h + 1][n + 1][m + 1] == Tomato.RIPE
                    and visited[h + 1][n + 1][m + 1] == Visit.UNVISITED
                ):
                    queue.append((h + 1, n + 1, m + 1))
                    visited[h + 1][n + 1][m + 1] = Visit.VISITED

    return queue


# 모든 토마토가 익었는지 확인
def checkTomato(ripe_count):
    return total_tomato == ripe_count


# 토마토가 익어가는 함수
def bfs():
    day = 0
    queue = deque()

    queue.extend(find_ripe_tomato())
    ripe_count = len(queue)

    # 모든 토마토가 익어있는 경우
    if len(queue) == total_tomato:
        return 0

    while len(queue):
        day += 1

        new_queue, count = water(day, queue, ripe_count)

        queue = new_queue
        ripe_count = count

        # 모든 토마토가 익었으면 종료
        if checkTomato(ripe_count):
            return day

    return -1


print(bfs())
