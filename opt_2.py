import sys
import math
from common import print_tour, read_input
from solver_greedy import solve as solve_greedy
from solver_greedy import distance

def tour_dist(tour,array,N):
    dist = 0
    
    dist = sum(array[tour[i]][tour[i+1]] for i in range(N-1))
    dist += array[tour[0]][tour[N-1]]
    print('BEST DISTANCE IS',dist)

def opt_2(tour,array,N):
    while True:
        count = 0
        for i1 in range(N-2):
            i2 = i1 + 1
            for j1 in range(i1+2,N):
                if j1 == N - 1:
                    j2 = 0
                else:
                    j2 = j1 + 1
                if i1 != 0 or j2 != 0:
                    dist1 = array[tour[i1]][tour[i2]]
                    dist2 = array[tour[j1]][tour[j2]]
                    dist3 = array[tour[i1]][tour[j1]]
                    dist4 = array[tour[i2]][tour[j2]]
                    if dist1 + dist2 > dist3 + dist4:
                        tour[i2:j1+1] = reversed(tour[i2:j1+1])
                        count += 1
        if count == 0:
            break
    return tour

def or_opt(tour,array,N):
    while True:
        count = 0
        for i1 in range(N):
            i0 = i1 - 1
            i2 = i1 + 1
            #編集中 
    
def solve(cities):
    N = len(cities)
    dist_array = [[0] * N for i in range(N)]
    for i in  range(N):
        for j in range(i, N):
            dist_array[i][j] = dist_array[j][i] = distance(cities[i],cities[j])
    tour = solve_greedy(cities)
    tour_dist(tour,dist_array,N)
    tour2 = opt_2(tour,dist_array,N)
    tour_dist(tour2,dist_array,N)
    #tour3 = or_opt(tour,dist_array,N)

    return tour2



if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    #print_tour(tour)
