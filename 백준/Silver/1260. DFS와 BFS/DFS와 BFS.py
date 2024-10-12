import sys

answer_dfs = []
answer_bfs = []

class Node:
  def __init__(self, u):
    self.u = u
    self.visited = False
    self.edges = []

  def addEdge(self, edge):
    self.edges.append(edge)

  def getEdges(self):
    return self.edges

  def is_visited(self):
    return self.visited
  
  def visit(self):
    self.visited = True

  def clearVisit(self):
    self.visited = False
  
def dfs(start_node: int):
  global answer_dfs
  node = nodes[start_node]

  # 노드를 이미 방문했으면 종료
  if node.is_visited():
    return
  
  answer_dfs.append(start_node)
  node.visit()

  edges = sorted(node.getEdges())

  for edge in edges:
    dfs(edge)

def bfs(start_node: int):
  global answer_bfs
  edges = [start_node]

  while len(edges) > 0:
    edge = edges.pop(0)
    node = nodes[edge]
    
    if node.is_visited():
      continue

    node.visit()
    answer_bfs.append(edge)
    edges.extend(sorted(node.getEdges()))

# 입력 받기
N, M, V = map(int, sys.stdin.readline().split())

nodes = [Node(i) for i in range(N + 1)]

for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())

  nodes[u].addEdge(v)
  nodes[v].addEdge(u)

dfs(V)

# 노드 클리어
for node in nodes:
  node.clearVisit()

bfs(V)

print(' '.join(map(str, answer_dfs)))
print(' '.join(map(str, answer_bfs)))