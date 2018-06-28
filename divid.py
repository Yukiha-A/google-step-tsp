import numpy as np
import itertools
import csv

#1行目は不要なのでskiprowsで読み飛ばし、配列に格納
data = np.loadtxt("input_6.csv",delimiter=",",skiprows=1)



def division(data):
	assert len(data) == 2048
	y_sorted_data=sorted(data,key=(lambda p: p[1]))
	#print(y_sorted_data[1])
	y_devided_data=[]
	assert 1 == 1

	for i in range(0,2048,128):
		y_devided_data.append(y_sorted_data[i:i+128])
	assert len(y_devided_data[0]) == 128
	assert len(y_devided_data) == 16
	#print(y_devided_data[1])
	for k in range(16):
		y_devided_data[k].sort(key=(lambda p: p[0]))
	assert len(y_devided_data[0]) == 128
	assert len(y_devided_data) == 16
	#print("y_devided_data")
	#print(y_devided_data[1])
	devided_data=[]
	for j in range(16):
		hoge=[]
		assert len(y_devided_data[j]) == 128
		for l in range(0,128,8):
			hoge.append(y_devided_data[j][l:l+8])
		assert len(hoge)== 16
		devided_data.append(hoge)
	print("devided_data")
	print(devided_data[0])
	print("len",len(devided_data))
	print("len of devided_data[0]",len(devided_data[0]))
	print("len of devided_data[0][0]",len(devided_data[0][0]))
	return (devided_data)

devided_data=division(data)

#print(devided_data)
