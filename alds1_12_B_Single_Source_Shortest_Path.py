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

def dijkstra(start:int,M:list):
  N = len(M)
  p = [None]*N #親のNode_IDリスト
  d = [INF]*N #distanceリスト

  d[start] = 0

  while True:
    #接続先のdistanceを決めていく
    for i in range(len(M)):
      for j in range(len(M[i])):
        #スタートから接続先までの距離が暫定値d[j]よりも短い場合は値を更新する
        if d[j] > d[i] + M[i][j]:
          d[j] = d[i] + M[i][j]
          p[j] = i
    return p,d

p,d = dijkstra(0, M)
print("親Node：",p)
print("最短経路：",d)