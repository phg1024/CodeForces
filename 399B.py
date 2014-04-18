# Author: peihong

def solve(n, pairs):
    # TBA

if __name__ == '__main__':
    n, m = map(int, raw_input().split())

    pairs = []
    for i in range(n):
        r, c = map(int, raw_input().split())
        pairs.append((r, c))

    t = solve(n, pairs)
    print t
