import sys

n = int(sys.stdin.readline())

heap = []


def swap(i: int, j: int):
    tmp = heap[i]
    heap[i] = heap[j]
    heap[j] = tmp


def get_min_index(h: int, l: int, r: int):
    size = len(heap)
    smallest = sys.maxsize
    q = None

    if h < size and smallest > heap[h]:
        smallest = heap[h]
        q = h
    if l < size and smallest > heap[l]:
        smallest = heap[l]
        q = l
    if r < size and smallest > heap[r]:
        smallest = heap[r]
        q = r

    return q


def pop():
    if len(heap) == 0:
        print(0)
        return

    swap(0, -1)
    print(heap.pop(-1))

    index = 0
    while len(heap) > 0:
        min_index = get_min_index(index, index * 2, index * 2 + 1)

        if min_index != index:
            swap(min_index, index)
            index = min_index
        else:
            break


def heapify(m: int):
    heap.append(m)

    head = len(heap) - 1
    parent = head // 2

    while head != parent:
        if heap[parent] > heap[head]:
            swap(parent, head)
        head = parent
        parent = head // 2


for _ in range(n):
    m = int(sys.stdin.readline())

    if m == 0:
        pop()
    else:
        heapify(m)
