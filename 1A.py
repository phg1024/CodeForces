__author__ = 'Peihong'
import math

if __name__ == '__main__':
    n, m, a = map(int, raw_input().split())
    print int(math.ceil(n/float(a))*math.ceil(m/float(a)))