if __name__ == "__main__":
  '''
  数値を標準入力で連続で受け取るメインプログラム
  '''
  print("start input data. if you completed  input, you type \"end\.")
  
  input_data = []
  while(1):
    tmp = input()
    if tmp == "end":
      break
    else:
      input_data.append(int(tmp))
  
  output = input_data

  print(output)