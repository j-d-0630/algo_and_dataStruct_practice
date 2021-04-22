"""
Connected Component
連結成分
"""

import alds1_3_A_basic_dataStruct as originalDataStruct

def dfs_path_check(vlist,start,end):

  color = [0]*len(vlist)

  s = originalDataStruct.stack()
  s.push(start)
  while not(s.is_empty()):
    u = s.pop()
    color[u] = 1
    for n in vlist[u]:
      if color[n] == 0:
        s.push(n)
      if n == end:
        return True
    
  return False

if __name__ == "__main__":

  input_data = []

  input_data.append("10 9")
  input_data.append("0 1")
  input_data.append("0 2")
  input_data.append("3 4")
  input_data.append("5 7")
  input_data.append("5 6")
  input_data.append("6 7")
  input_data.append("6 8")
  input_data.append("7 8")
  input_data.append("8 9")
  input_data.append("3")
  input_data.append("0 1")
  input_data.append("5 9")
  input_data.append("1 3")

  N,E = map(int,input_data.pop(0).split())

  vList = [ [] for i in range(N) ]

  for i in range(E):
    u,v = map(int,input_data.pop(0).split())
    vList[u].append(v)
  
  Q = int(input_data.pop(0))
  for i in range(Q):
    start,end = map(int,input_data.pop(0).split())

    ans = "yes" if dfs_path_check(vList,start,end) else "no"
    print(ans)