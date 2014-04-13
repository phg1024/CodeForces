__author__ = 'Peihong'

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    A = map(int, raw_input().split())
    threshold = A[k-1]
    count = 0
    for x in A:
        if x > 0 and x >= threshold:
            count = count + 1
    print count