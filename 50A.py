__author__ = 'Peihong'

def solve(m, n):
    if m < n:
        return solve(n, m)
    else:
        if m <= 1 or n == 0:
            return 0
        elif n == 1:
            return m/2
        else:
            # m>1, n>1
            res1 = 1 + solve(m-1, 2) + solve(1, n-2) + solve(m-1, n-2)
            res2 = 1 + solve(m-2, 1) + solve(2, n-1) + solve(m-2, n-1)
            return max(res1, res2)

if __name__ == '__main__':
    m, n = map(int, raw_input().split())
    res = solve(m, n)
    print res
