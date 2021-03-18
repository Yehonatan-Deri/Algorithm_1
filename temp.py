from typing import NewType
import numpy as np


def rabin_karp_match(T, P, q=101, d=256):
    """
    find Sub-shows of P inside T

    @param:
        @T: long string to search P inside
        @P: short string to search inside T
        @q: Prime number
        @d: Counting base by default is 256 -> the range of ascii table

    :return: list of indexes where P found in T, index of the first char mach

    :complexity: where n,m,t,(n/q) = len(T),len(P),Sub-shows number,shows where tha hash was equal but not the Sub-show
        Average-case: O(n + m*t + m*(n/q))
    """
    n, m = len(T), len(P)
    h, p, t = (d ** (m - 1)) % q, 0, 0  #
    h = 1

    t0, p0 = [], []
    for i in range(m - 1):
        h = (d * h) % q
    for c1, c2, i in zip(T, P, range(m)):
        t = (t * d + (ord(c1) - ord('a'))) % q
        p = (p * d + (ord(c2) - ord('a'))) % q
        t0.append(t)
        p0.append(p)

    res_indexes, arr_t, hits = [], [t], []
    for i in range(n - m + 1):
        if t == p:
            hits.append(i)
            found = True
            for c1, c2 in zip(P, T[i:m + i]):
                if c1 != c2:
                    found = False
                    break
            if found:
                res_indexes.append(i)

        if i < n - m:  # t=(d*(t-h*T[i])+T[m+i]) mod q
            t = (d * (t - h * (ord(T[i]) - ord('a'))) + (ord(T[m + i]) - ord('a'))) % q
            t = t if t >= 0 else t + q
            arr_t.append(t)

    print(f'h={h}, t0_init={t0}, p_init={p0}')
    print(f'arr_t={arr_t}')
    print(f'hits={hits}, number of hits={len(hits)}')
    print(f'math: {res_indexes},')
    return res_indexes


def naive_match(T, P):
    """
    find Sub-shows of P inside T

    @param:
        @T: long string to search P inside
        @P: short string to search inside T

    :return: list of indexes where P found in T, index of the first char mach

    :efficiency: where n,m = len(T),len(P)
        worst-case: O(n*m)
        Average-case: O(n) (=for a random P)
    """
    res_indexes = []
    m, c_p = len(P), P[0]

    i = 0
    # for c, i in zip(T, range(len(T) - len(P) + 1)):
    while i < len(T) - len(P) + 1:
        if T[i] == c_p:
            j = 1
            i += 1
            for c_t in T[i:]:
                if c_p != c_t:
                    # i += 1
                    break
                else:
                    if j >= m - 1:
                        res_indexes.append(i - m + 1)
                i, j = i + 1, j + 1
            # else:
        i += 1

    return res_indexes


def eval_(A, x_0):
    res, x = 0, 1
    for a in A:
        res += a * x
        x *= x_0
    return res


def mult_(A, B):
    # C=
    pass


print(eval_([1, -2, 2], 2))
print(mult_([2, -1, 0, 2], [1, 0, -2, 1]))
s = np.array([[-1, 1], [0, 2], [1, 1]])
print(s)
