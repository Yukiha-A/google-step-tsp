#####たくさんの点を８つずつに分けてその中で総当たりする方法###
import csv
import itertools
import math
#２点間の距離を求める関数dest
def dest(list1, list2):
    l = list(map(lambda x,y:(x-y)**2, list1, list2))
    s = math.sqrt(sum(l))
    return s

def arrangement(all_points, start_point, end_point):#all_points:８つの点のインデックスのリスト/start_point:始点/end_point:終点
    with open('input_6.csv','r') as f:
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
        #点のリストから始点と終点を除く
        all_points.remove(start_point)
        all_points.remove(end_point)
        #csvファイルの中のインデックスから座標に変換
        chart_all_points = []
        for j in all_points:
            chart_all_points.append(floatpoint[j - 1])
        #全ての並べ方をallに列挙
        all = list(itertools.permutations(chart_all_points))
        d = []
        for a in all:
            destination = dest(floatpoint[start_point - 1], a[0]) + dest(a[0], a[1]) + dest(a[1], a[2]) + dest(a[2], a[3]) +dest(a[3],a[4]) + dest(a[4],a[5]) + dest(a[5], floatpoint[end_point - 1])
            d.append(destination)
        print(min(d))