import sys
from enum import Enum
from collections import deque

queue = deque()
# 편의점 큐
graph = []
locations = []
visited = deque()

result = []

MIN = -32768
MAX = 32767


def get_distance(locA, locB):
    (x1, y1) = locA
    (x2, y2) = locB

    return abs(x1 - x2) + abs(y1 - y2)


# 모든 요소간의 거리를 재서 graph에 추가
def make_graph(N):
    global graph
    graph = [[] for _ in range(N + 2)]

    for i in range(N + 2):
        for j in range(N + 2):
            if i == j:
                continue

            if get_distance(locations[i], locations[j]) <= 1000:
                graph[i].append(j)
                graph[j].append(i)


def reset():
    global locations, graph, visited, queue
    locations = []
    graph = []
    visited.clear()
    queue.clear()


def main():
    queue.append(0)
    visited.append(locations[0])

    while len(queue):
        i = queue.popleft()

        if locations[i] == locations[-1]:
            return "happy"

        for j in graph[i]:
            if not locations[j] in visited:
                visited.append(locations[j])
                queue.append(j)

    return "sad"


T = int(input().strip())

for _ in range(T):
    # 편의점의 개수
    N = int(input().strip())

    # 상근이네 집
    Hx, Hy = map(int, input().split())
    locations.append((Hx, Hy))

    for _ in range(N):
        # 편의점
        Cx, Cy = map(int, input().split())

        locations.append((Cx, Cy))

    # 페스티벌 위치
    Fx, Fy = map(int, input().split())
    locations.append((Fx, Fy))

    make_graph(N)
    result.append(main())
    reset()

for res in result:
    print(res)
