def function(N,input_data):
  rslt = []
  for i in range(N):
    adj_num = input_data[i][1]
    tmp = [0]*N
    for j in range(adj_num):
      tmp[input_data[i][2+j]-1] = 1
    
    rslt.append(tmp)
  
  return rslt


N = int(input())
input_data = [list(map(int,input().split())) for i in range(N)]

ans = function(N,input_data)
print(ans)