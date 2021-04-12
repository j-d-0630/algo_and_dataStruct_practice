"""
Basic Sorting Problem
"""
import copy

def sort_selection(input_data):
  """
  選択ソート
  ソート済領域を拡張していく
  最小値（最大値）を選ぶことを繰り返す
  非安定なソート
  下記は昇順ソート
  """
  rslt = copy.deepcopy(input_data)
  for i in range(0,len(input_data)):
    min_id = i
    #rslt[i]にi番目～最後尾までの範囲のmin値を持ってくる
    for j in range(i,len(input_data)):
      if rslt[min_id] > rslt[j]:
        min_id = j
    tmp = rslt[i]
    rslt[i] = rslt[min_id]
    rslt[min_id] = tmp
  
  return rslt


def sort_bubble(input_data):
  """
  バブルソート
  隣り合う要素を入れ替えることを繰り返す
  入れ替わりが起きなくなったら終了
  安定なソート
  下記は昇順ソート
  """
  rslt = copy.deepcopy(input_data)
  flag = 1
  j = 0
  while flag:
    flag = 0
    #隣通しを比較しながらmax値を最後尾に持っていく
    for i in range(0,len(rslt)-j-1):
      if rslt[i] > rslt[i+1]:
        tmp = rslt[i+1]
        rslt[i+1] = rslt[i]
        rslt[i] = tmp
        flag = 1
    j += 1
  
  return rslt


def sort_insert(input_data):
  """
  挿入ソート
  ソート済領域を拡張していく
  拡張していく中で拡張する先頭要素を適切な場所に挿入していく
  安定なソート
  以下は昇順ソート
  """
  rslt = copy.deepcopy(input_data)
  for i in range(1,len(input_data)):
    v = rslt[i]
    j = i-1
    #vよりもrslt[i-1]が大きいときはrslt[i]をrslt[i-1]にする。これを左側へ繰り返していき大きいものがなくなったらそこにvを入れる（vを適切な場所に入れていく）
    while( (j >= 0 and rslt[j] > v) ):
      rslt[j+1] = rslt[j]
      j -= 1
    rslt[j+1] = v
  
  return rslt


if __name__ == "__main__":
  print("start input.")
  
  input_data = []
  while(1):
    tmp = input()
    if tmp == "end":
      break
    else:
      input_data.append(int(tmp))
  
  output_sel = sort_selection(input_data)
  output_bub = sort_bubble(input_data)
  output_ins = sort_insert(input_data)

  print(output_sel)
  print(output_bub)
  print(output_ind)