from enum import Enum
import sys


class Direction(Enum):
    LEFT = ("L",)
    RIGHT = ("D",)
    UP = ("U",)
    DOWN = "DD"


class Cell(Enum):
    NOTHING = (1,)
    APPLE = (2,)
    SNAKE = 3


board = []
snake_queue = [[0, 0]]
directions = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

# 게임 보드 생성
for _ in range(N):
    bboard = []
    for _ in range(N):
        bboard.append(Cell.NOTHING)
    board.append(bboard)
board[0][0] = Cell.SNAKE

for _ in range(K):
    A = sys.stdin.readline().split()
    board[int(A[0]) - 1][int(A[1]) - 1] = Cell.APPLE

L = int(sys.stdin.readline())
commands = []
for _ in range(L):
    A = input().split()
    commands.append([int(A[0]), A[1]])


def check_wall(i: int, j: int):
    if i >= N or j >= N or i < 0 or j < 0:
        return True


def check_snake_body(i: int, j: int):
    if len(snake_queue) == 1:
        return False

    for q in snake_queue:
        if q[0] != snake_queue[-1][0] or q[1] != snake_queue[-1][0]:
            if i == q[0] and j == q[1]:
                return True
    return False


def check_apple(i: int, j: int):
    return board[i][j] == Cell.APPLE


def check_turn(time: int):
    for c in commands:
        if time > c[0]:
            continue
        if time == c[0]:
            return True
    return False


def turn(time: int):
    global direction
    global direction_i

    for c in commands:
        if time == c[0]:
            if c[1] == "L":
                if direction_i == 0:
                    direction_i = 3
                else:
                    direction_i -= 1
            elif c[1] == "D":
                direction_i = (direction_i + 1) % 4

    direction = directions[direction_i]


def move(i: int, j: int):
    board[i][j] = Cell.SNAKE


direction = Direction.RIGHT
direction_i = 1
t = 1
while True:
    i = snake_queue[-1][0]
    j = snake_queue[-1][1]

    if direction == Direction.LEFT:
        j -= 1
    elif direction == Direction.RIGHT:
        j += 1
    elif direction == Direction.UP:
        i -= 1
    elif direction == Direction.DOWN:
        i += 1

    if check_wall(i, j):
        break

    if check_snake_body(i, j):
        break

    snake_queue.append([i, j])
    if check_apple(i, j) == False:
        q = snake_queue.pop(0)
        board[q[0]][q[1]] = Cell.NOTHING

    move(i, j)

    if check_turn(t):
        turn(t)

    if t == 9:
        aa = 10
    t += 1


print(t)
