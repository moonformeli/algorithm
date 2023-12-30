import sys

N = int(sys.stdin.readline())

heap = [sys.maxsize]


def swap(l: int, r: int):
    tmp = heap[l]
    heap[l] = heap[r]
    heap[r] = tmp


def heap_max(h: int, l: int, r: int):
    max_value = 0
    q = 1

    if h < len(heap) and heap[h] > max_value:
        max_value = heap[h]
        q = h
    if l < len(heap) and heap[l] > max_value:
        max_value = heap[l]
        q = l
    if r < len(heap) and heap[r] > max_value:
        max_value = heap[r]
        q = r

    return q


def heap_pop():
    if len(heap) == 1:
        return 0

    swap(1, -1)
    res = heap.pop(-1)

    h = 1
    l = h * 2
    r = l + 1
    while heap_max(h, l, r) != h:
        m = heap_max(h, l, r)
        swap(m, h)
        h = m
        l = h * 2
        r = l + 1

    return res


def heapify(n: int):
    heap.append(n)

    h = len(heap) - 1
    p = h // 2
    while h > 0 and p > 0 and h != p and heap[h] > heap[p]:
        swap(p, h)
        h = p
        p = h // 2


xs = []
for _ in range(N):
    xs.append(int(sys.stdin.readline()))

for x in xs:
    if x == 0:
        print(heap_pop())
    else:
        heapify(x)
