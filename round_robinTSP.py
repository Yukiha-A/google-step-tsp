#総当りでとく
import sys
import math
import random
import itertools  
from common import read_input, print_tour

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
            
    array_N = [0 for i in range(N)]
    for i in range(N):
        array_N[i] = i

    best_dist = 10000
    tour_perm = itertools.permutations(array_N)
    #permは順列の一つ
    for perm in tour_perm:
        tour_dist = 0
        for i in range(len(perm)-1):
            tour_dist += dist[perm[i]][perm[i+1]]
        tour_dist += dist[perm[0]][perm[N-1]]
        if best_dist > tour_dist:
            best_dist =  tour_dist
            best_tour_list = perm      
    return best_tour_list

if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
