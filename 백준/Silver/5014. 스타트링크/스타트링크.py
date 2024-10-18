import sys
from enum import Enum
from collections import deque

F, S, G, U, D = map(int, input().split())

MIN = 1
MAX = F

queue = deque()
visited = set()


def check_floor(floor):
    if floor < MIN:
        return False

    if floor > MAX:
        return False

    return True


def go_up(floor):
    next_floor = floor + U

    if not check_floor(next_floor):
        return

    if not next_floor in visited:
        queue.append(next_floor)
        visited.add(next_floor)


def go_down(floor):
    next_floor = floor - D

    if not check_floor(next_floor):
        return

    if not next_floor in visited:
        queue.append(next_floor)
        visited.add(next_floor)


def elevator():
    size = len(queue)

    for _ in range(size):
        current_floor = queue.popleft()

        if current_floor == G:
            return True

        go_up(current_floor)
        go_down(current_floor)

    return False


def main():
    count = 0

    queue.append(S)
    visited.add(S)

    while len(queue):
        if elevator():
            return count

        count += 1

    return "use the stairs"


print(main())
