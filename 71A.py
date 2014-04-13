__author__ = 'Peihong'

if __name__ == '__main__':
    nwords = int(raw_input())
    for i in range(nwords):
        word = raw_input()
        if len(word) <= 10:
            print word
        else:
            print '%c%d%c' % (word[0], len(word)-2, word[-1])