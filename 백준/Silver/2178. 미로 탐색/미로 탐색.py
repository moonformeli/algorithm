import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

# 빈 배열을 한 사이즈 크게 만들기
maze = [[0 for _ in range(M + 2)] for _ in range(N + 2)]
visited = [[0 for _ in range(M + 2)] for _ in range(N + 2)]

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

# 입력 받기
for i in range(N):
    line = sys.stdin.readline().strip()

    for j in range(M):
        maze[i + 1][j + 1] = int(line[j])


# 최단 경로 찾기
def find_exit(i, j):
    queue = deque()

    # x좌표, y좌표, 움직인 칸 수
    queue.append((i, j, 1))
    while len(queue):
        x, y, move = queue.popleft()

        # 목표 지점 확인
        if x == N and y == M:
            return move

        # 네 방향 검사
        for i in range(4):
            posX = x + dx[i]
            posY = y + dy[i]

            if maze[posX][posY] and not visited[posX][posY]:
                visited[posX][posY] = 1
                queue.append((posX, posY, move + 1))

    return 0


print(find_exit(1, 1))
