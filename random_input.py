"""
Random Input Program
"""
import random
import time
import datetime

if __name__ == "__main__":
  max_v = 100
  n = 100

  print("start time:{}".format(datetime.datetime.now()))
  time1 = time.perf_counter()

  #重複ありの整数データ
  input_data_v1 = [ random.randint(0,max_v) for i in range(n) ]
  #重複なしの整数データ
  input_data_v2 = random.sample(range(max_v),n)

  time2 = time.perf_counter()
  print("elapsed time: {} [ms]".format(time2-time1))