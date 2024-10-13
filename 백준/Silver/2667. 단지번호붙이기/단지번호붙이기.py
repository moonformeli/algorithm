import sys
from collections import deque

N = int(sys.stdin.readline().strip())

# 빈 배열 정의. 한 사이즈 크게
maps = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
visited = [[0 for _ in range(N + 2)] for _ in range(N + 2)]

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

for i in range(N):
    line = sys.stdin.readline().strip()

    for j in range(N):
        maps[i + 1][j + 1] = int(line[j])


# 단지 찾기
def mark_apartment_complex(i, j) -> tuple[int, int]:
    global maps, visited

    complex_count = 0
    apartment_count = 0

    if visited[i][j]:
        return (complex_count, apartment_count)

    complex_count += 1
    apartment_count += 1
    visited[i][j] = 1
    queue = deque()
    queue.append((i, j))

    while len(queue):
        x, y = queue.popleft()

        # 네 방향 검사
        for i in range(4):
            pos_x = x + dx[i]
            pos_y = y + dy[i]
            if maps[pos_x][pos_y] and not visited[pos_x][pos_y]:
                apartment_count += 1
                visited[pos_x][pos_y] = 1
                queue.append((pos_x, pos_y))

    return (complex_count, apartment_count)


# 배열을 순회하면서 체크하기
complex_count = 0
apartment_counts = []

for i in range(N):
    for j in range(N):
        if not maps[i + 1][j + 1]:
            continue

        result = mark_apartment_complex(i + 1, j + 1)

        if result[0] > 0:
            complex_count += result[0]
            apartment_counts.append(result[1])

# 출력
print(complex_count)
for count in sorted(apartment_counts):
    print(count)
