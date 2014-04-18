# Author: peihong

if __name__ == '__main__':
    n = int(raw_input())
    state = raw_input()
    count = 0
    for i in range(n):
        if state[i] == 'B':
            count = count + 2**i
    print count
