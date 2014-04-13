__author__ = 'Peihong'

if __name__ == '__main__':
    word = raw_input()
    y = []
    d = ['a', 'e', 'i', 'o', 'u', 'y']
    word = word.lower()
    for x in word:
        if x in d:
            continue
        else:
            y.append('.')
            y.append(x)
    print ''.join(y)