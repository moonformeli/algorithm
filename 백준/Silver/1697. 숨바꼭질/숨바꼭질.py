import sys
from enum import Enum
from collections import deque

N, K = map(int, input().split())

MIN = 0
MAX = 100000

queue = deque()
steps = set()


def walk(n):
    c1 = n - 1
    c2 = n + 1

    if c1 >= MIN and c1 <= MAX and not c1 in steps:
        queue.append(c1)
        steps.add(c1)

    if c2 >= MIN and c2 <= MAX and not c2 in steps:
        queue.append(c2)
        steps.add(c2)


def run(n):
    c1 = n * 2

    if c1 >= MIN and c1 <= MAX and not c1 in steps:
        queue.append(c1)
        steps.add(c1)


def move():
    size = len(queue)

    for _ in range(size):
        n = queue.popleft()

        if n == K:
            return True

        walk(n)
        run(n)

    return False


def main():
    time = 0
    queue.append(N)
    steps.add(N)

    while len(queue):
        if move():
            break

        time += 1

    return time


print(main())
