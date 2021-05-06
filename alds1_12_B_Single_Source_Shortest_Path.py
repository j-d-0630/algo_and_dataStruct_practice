"""
Single Source Shortest Path
単一始点最短経路
"""

input_data = []
input_data.append("5")
input_data.append("0 3 2 3 3 1 1 2")
input_data.append("1 2 0 2 3 4")
input_data.append("2 3 0 3 3 1 4 1")
input_data.append("3 4 2 1 0 1 1 4 4 3")
input_data.append("4 2 2 1 3 3")

N = int(input_data.pop(0))
INF = 1000 #INFは経路が繋がっていない状態を示す
M = [ [INF]*N for i in range(N) ]
adjList = [ list(map(int,input_data.pop(0).split())) for i in range(N) ]

#各Nodeと各Nodeの繋がりの関係のリストを作成
for i in range(N):
  adjN = adjList[i][1]
  for j in range(adjN):
    adjNode = adjList[i][j*2+2]
    M[i][adjNode] = adjList[i][j*2+3]

def dikstra(start:int,M:list):
  N = len(M)
  p = [None]*N #親のNode_IDリスト
  d = [INF]*N #distanceリスト
  color = [0]*N # 0:undiscoverd ,1:dicovered

  d[start] = 0

  while True:
    mindis = INF
    for i in range(N):
      #未探索かつ最短経路のNodeから探索
      if color[i] != 1 and d[i] < mindis:
         mindis = d[i]
         u = i
    #全てのNodeが探索済ならばwhileを抜ける
    if mindis == INF:
      break
    
    color[u] = 1
        
    for v in range(N):
      if M[u][v] != INF and d[v] > d[u]+ M[u][v]:
        d[v] = d[u] + M[u][v]
        p[v] = u

  return p,d

p,d = dikstra(0, M)
print("親Node：",p)
print("最短経路：",d)
