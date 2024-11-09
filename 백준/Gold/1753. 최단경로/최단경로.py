import sys
from enum import Enum
from collections import deque
from heapq import heappush, heappop, heapify
from math import inf, isinf

V, E = map(int, input().split())

K = int(input().strip())

graphs = [[] for _ in range(V + 1)]

distance = [inf for _ in range(V + 1)]
prev = [None for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())

    graphs[u].append((v, w))


def solution():
    distance[K] = 0

    queue = [(0, K)]

    while queue:
        dist, source = heappop(queue)

        if dist > distance[source]:
            continue

        for node, next_dist in graphs[source]:
            if next_dist + distance[source] < distance[node]:
                distance[node] = next_dist + distance[source]
                heappush(queue, (distance[node], node))

    for i in range(1, len(distance)):
        if isinf(distance[i]):
            print("INF")
        else:
            print(distance[i])


solution()
