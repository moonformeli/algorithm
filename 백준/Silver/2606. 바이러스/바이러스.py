import sys
from collections import deque


class Computer:
    def __init__(self, node):
        self.node = node
        self.visited = False
        self.connected_computers = []

    def connect_to_computer(self, computer):
        self.connected_computers.append(computer)


# 컴퓨터의 수
N = int(sys.stdin.readline().strip())

# 연결 수
M = int(sys.stdin.readline().strip())

# 간선 정보
computers = [Computer(i) for i in range(N + 1)]
for i in range(M):
    C, V = map(int, sys.stdin.readline().split())

    computers[C].connect_to_computer(V)
    computers[V].connect_to_computer(C)


def get_infected_computers_count():
    count = 0
    queue = deque()

    computers[1].visited = True
    queue.append(computers[1])

    while len(queue):
        computer: Computer = queue.popleft()

        for i in computer.connected_computers:
            neighbor_computer = computers[i]
            if not neighbor_computer.visited:
                count += 1
                neighbor_computer.visited = True
                queue.append(neighbor_computer)

    return count


print(get_infected_computers_count())
