import csv
import itertools
import math
#２点間の距離を求める関数dest
def dest(list1, list2):
    l = list(map(lambda x,y:(x-y)**2, list1, list2))
    s = math.sqrt(sum(l))
    return s

with open('input_0.csv','r') as f:
    dataReader = csv.reader(f)
    point = []
    #csvファイルから点の座標を取り出しリストpointに入れる
    for row in dataReader:
        point.append(row)
    del point[0]
    floatpoint = []
    for p in point:
        floatp = list(map(float, p))
        floatpoint.append(floatp)
    #全ての並べ方をallに列挙
    all = list(itertools.permutations(floatpoint[0:5]))
    d = []
    for a in all:
        destination = dest(a[0], a[1]) + dest(a[1], a[2]) + dest(a[2], a[3]) +dest(a[3],a[4]) + dest(a[4],a[0])
        d.append(destination)
    print(min(d))