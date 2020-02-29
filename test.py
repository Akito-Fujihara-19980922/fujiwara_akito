"""
このファイルに解答コードを書いてください
"""
#ここに整数を入力してください

import numpy as np
f = open('input.txt')
data1 = f.read()  
f.close()
data = data1.split('\n') 
data = np.array(data)
data_list = []
for i in range(len(data)):
    add = data[i].split(":")
    data_list.append(add)
m = int(data_list[-2][0])
data_list = data_list[:-2]
for i in range(len(data_list)):
    data_list[i][0] = int(data_list[i][0])
data_list = sorted(data_list)

x = 0
for i in range(len(data_list)):
    if m % data_list[i][0] == 0:
        x += 1
        print(data_list[i][1])
if x == 0: 
    print(m)