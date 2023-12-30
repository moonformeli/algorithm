import ast
import sys


class Deque:
    def __init__(self, x, p):
        self.x = x
        self.p = p
        self.head = 0
        self.tail = len(x) - 1
        self.reversed = False

    def size(self):
        return self.tail - self.head + 1

    def D(self):
        if self.size() == 0:
            return "error"

        if self.reversed:
            self.tail -= 1
        else:
            self.head += 1

    def R(self):
        self.reversed = not self.reversed

    def slice(self, start, stop, step):
        res = "["

        j = 0
        for i in range(start, stop, step):
            val = str(self.x[i])
            if j == 0:
                res += val
            else:
                res += "," + val
            j += 1

        res += "]"

        return res

    def run(self):
        for c in self.p:
            if c == "R":
                r = self.R()
            elif c == "D":
                r = self.D()

            if r == "error":
                return "error"

        if self.reversed:
            return self.slice(self.tail, self.head - 1, -1)
        else:
            return self.slice(self.head, self.tail + 1, 1)


T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    x = ast.literal_eval(input())

    deque = Deque(x, p)
    print(deque.run())