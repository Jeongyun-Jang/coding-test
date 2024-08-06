node = ['m','a','k','i','t','c']

g = [[0,1,1,0,0,0],
     [1,0,1,1,0,0],
     [0,1,1,0,1,1],
     [0,0,0,1,0,0],
     [0,0,0,1,0,0],
     ]

# bfs

q = []
visit = []

q.append(node[0])
visit.append(node[0])

while q:
  x = q.pop(0)
  print(x, end=' ')
  idx = node.index(x)
  for i in range(len(g[idx])):
    if g[idx][i] == 1:
      if node[i] not in visit:  # 방문 리스트에 노드가 있는지 확인
        q.append(node[i])
        visit.append(node[i])
