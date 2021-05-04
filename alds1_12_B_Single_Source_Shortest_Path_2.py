"""
Single Source Shortest Path 2
単一始点最短経路（ダイクストラをヒープで高速化）
"""
import heapq

input_data = []
input_data.append("5")
input_data.append("0 3 2 3 3 1 1 2")
input_data.append("1 2 0 2 3 4")
input_data.append("2 3 0 3 3 1 4 1")
input_data.append("3 4 2 1 0 1 1 4 4 3")
input_data.append("4 2 2 1 3 3")

N = int(input_data.pop(0))
INF = 1000 #INFは繋がっていない状態を示す
M = [ [INF]*N for i in range(N) ]
adjList = [ list(map(int,input_data.pop(0).split())) for i in range(N) ]

#各Nodeと各Nodeの繋がりの関係リストを作成
for i in range(N):
  adjN = adjList[i][1]
  for j in range(adjN):
    adjNode = adjList[i][j*2+2]
    M[i][adjNode] = adjList[i][j*2+3]

def dijkstra(start:int,adjList:list):
  N = len(M)
  p = [None]*N #親のNode_IDリスト
  d = [INF]*N #disatanceリスト
  color = [0]*N # 0:undiscovered 1:discovered 2:decided

  d[start] = 0

  h = [(0,0)] #(distance,Node_ID)
  heapq.heapify(h)

  while len(h) > 0:
    min_d,u = heapq.heappop(h)
    color[u] = 2

    for i,v in enumerate(adjList[u]):
      if i%2 == 0:
        if color[v] == 2:
          continue
        if d[v] > d[u] + adjList[u][i+1]:
          d[v] = d[u] + adjList[u][i+1]
          p[v] = u
          color[v] = 1
          heapq.heappush(h,(d[v],v))

  return p,d


p,d = dijkstra(0,adjList)

for i in range(N):
  print(str(i)+"の最短経路長は"+str(d[i]))

for i in range(N):
  print(str(i)+"の親Nodeは"+str(p[i]))