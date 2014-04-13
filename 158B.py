__author__ = 'Peihong'
import math

if __name__ == '__main__':
    ngroups = int(raw_input())
    A = map(int, raw_input().split())
    counts = [0, 0, 0, 0, 0]
    for x in A:
        counts[x] = counts[x] + 1

    ntaxi = counts[4] + counts[3] + counts[2]/2
    counts[1] = counts[1] - counts[3]
    counts[2] = counts[2] % 2
    if counts[2] == 1:
        ntaxi = ntaxi + 1
        counts[1] = counts[1] - 2
    if counts[1] > 0:
        ntaxi = ntaxi + int(math.ceil(counts[1]/4.0))
    print ntaxi