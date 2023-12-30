import sys


class Deque:
    def __init__(self):
        self.reset()

    def reset(self):
        self.q = []
        self.head = 0
        self.tail = 0

    def push_back(self, n: int):
        self.q.insert(self.tail + 1, n)

        if self.tail < len(self.q) - 1:
            self.tail += 1

    def push_front(self, n: int):
        self.q.insert(self.head, n)

        if self.tail < len(self.q) - 1:
            self.tail += 1

    def pop_front(self):
        if self.len() <= 0:
            print(-1)
            return

        print(self.q[self.head])

        self.head += 1
        if self.len() <= 0:
            self.reset()

    def pop_back(self):
        if self.len() <= 0:
            print(-1)
            return

        print(self.q[self.tail])

        self.tail -= 1
        if self.len() <= 0:
            self.reset()

    def len(self):
        if len(self.q) == 0:
            return 0
        return self.tail - self.head + 1

    def size(self):
        print(self.len())

    def empty(self):
        if self.len() == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if self.len() == 0:
            print(-1)
        else:
            print(self.q[self.head])

    def back(self):
        if self.len() == 0:
            print(-1)
        else:
            print(self.q[self.tail])


n = int(sys.stdin.readline())

cs = []
for _ in range(n):
    c = sys.stdin.readline().split()
    cs.append(c)

deque = Deque()
for c in cs:
    if c[0] == "push_back":
        deque.push_back(int(c[1]))
    elif c[0] == "push_front":
        deque.push_front(int(c[1]))
    elif c[0] == "pop_front":
        deque.pop_front()
    elif c[0] == "pop_back":
        deque.pop_back()
    elif c[0] == "size":
        deque.size()
    elif c[0] == "empty":
        deque.empty()
    elif c[0] == "front":
        deque.front()
    elif c[0] == "back":
        deque.back()
