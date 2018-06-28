#-*- coding: utf-8 -*-
import numpy as np
import itertools
import csv

#1行目は不要なのでskiprowsで読み飛ばし、配列に格納
data = np.loadtxt("input_0.csv",delimiter=",",skiprows=1)


#print(data)

cont_dist=0
dist=float('inf') #最短距離、仮に無限とおいておく
order=(0,1,2,3,4) #ここを0~n-1にすればn点に対応
result_order=[] 
result=[] #最終的にファイルに書き込む内容

#(点の順列を全て挙げ,その順列が示す順番通りに辿り、距離を求める)
for hoge in itertools.permutations(order):
    cont_dist=0
    for i in range(4):
        k=np.linalg.norm(data[hoge[i]]-data[hoge[i+1]])
        cont_dist=cont_dist+k
        #print(cont_dist)
    l=np.linalg.norm(data[hoge[4]]-data[hoge[0]])
    cont_dist=cont_dist+l
    #print(cont_dist)
    if cont_dist < dist:
        #print('foo') #test
        dist=cont_dist
        result_order[0:5]=hoge
        #print(result_order)

print(dist)
#print(result_order)


for j in range(5):
    m=result_order[j]
    result.append(data[m])

#print(result)

#ファイルに書き込み
with open('output_0.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')  
    writer.writerows(result) 
    
