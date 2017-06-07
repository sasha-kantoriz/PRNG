#!usr/bin/python
import sys
from random import randint


lags1, lags2 = (55, 24), (52, 19)
_modulus = 31


def lagfib(n, lags, firstterms=None):
    maxlag = max(lags)
    if firstterms is None:
        firstterms = [randint(0, 2 ** _modulus) for x in range(0, maxlag + 1)]
    if n <= maxlag:
        return firstterms[n]
    else:
        # Compute recursively Xn
        return (lagfib(n - lags[0], lags, firstterms) + lagfib(n - lags[1], lags, firstterms)) % (2 ** _modulus)


def fish(size):
    result = []
    for i in range(size):
        a, b = bin(lagfib(n=i, lags=lags1))[-1], bin(lagfib(n=i, lags=lags2))[-1]
        while b == '0':
            a, b = bin(lagfib(n=i, lags=lags1))[-1], bin(lagfib(n=i, lags=lags2))[-1]
        result.append(str(int(a) ^ int(b)))
    return result


def mush(size):
    result = []
    for i in range(size):
        a, b = bin(lagfib(n=i, lags=lags1))[-1], bin(lagfib(n=i, lags=lags2))[-1]
        if a == '1':
            b = bin(lagfib(n=i, lags=lags2))[-1]
        if b == '1':
            a = bin(lagfib(n=i, lags=lags1))[-1]
        result.append(str(int(a) ^ int(b)))
    return result


def fish_to_file(file_name, size):
    with open(file_name, 'w') as f:
        f.write(''.join(fish(size)))


def mush_to_file(file_name, size):
    with open(file_name, 'w') as f:
        f.write(''.join(mush(size)))


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print "Usage: {} METHOD SIZE OUTPUT".format(sys.argv[0])
        exit()

    method, size, output_file = sys.argv[1:]
    size, method = int(size), method.lower()

    if 'fish' in method:
        fish_to_file(output_file, size)
    elif 'mush' in method:
        mush_to_file(output_file, size)
