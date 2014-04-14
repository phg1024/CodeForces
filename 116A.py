__author__ = 'Peihong'

if __name__ == '__main__':
    n = int(raw_input())
    count = 0
    capacity = 0
    for i in range(n):
        a, b = map(int, raw_input().split())
        count = count - a + b
        capacity = max(capacity, count)
    print capacity