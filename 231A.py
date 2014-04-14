__author__ = 'Peihong'

if __name__ == '__main__':
    n = int(raw_input())
    count = 0
    for i in range(n):
        x, y, z = map(int, raw_input().split())
        sum = x + y + z
        if sum > 1:
            count = count + 1
    print count