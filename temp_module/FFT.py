# import pip._vendor.msgpack.fallback
# from pip._vendor.msgpack.fallback import xrange


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

    for c, i in zip(T, range(len(T) - len(P) + 1)):
        found = True
        for c_p, c_t in zip(P, T[i:]):
            if c_p != c_t:
                found = False
                break
        if found:
            res_indexes.append(i)

    return res_indexes


def rabin_karp_match(T, P, q=101, d=256):
    """
    find Sub-shows of P inside T

    @param:
        @T: long string to search P inside
        @P: short string to search inside T
        @q: Prime number
        @d: Counting base by default is 256 -> the range of ascii table

    :return: list of indexes where P found in T, index of the first char mach

    :complexity: where n,m,k = len(T),len(P),Sub-shows number
        worst-case: O(n*m)
        Average-case: O(m+n)
    """
    n, m = len(T), len(P)
    h, p, t = (d ** (m - 1)) % q, 0, 0  #
    h = 1
    for i in range(m - 1):
        h = (d * h) % q
    for c1, c2, i in zip(T, P, range(m)):
        t = (t * d + ord(c1)) % q
        p = (p * d + ord(c2)) % q

    res_indexes = []
    for i in range(n - m + 1):  # c_prev, c_next,  zip(T[0:n - m + 1], T[m:], range(n - m + 1))
        if t == p:
            found = True
            for c1, c2 in zip(P, T[i:m + i]):
                if c1 != c2:
                    found = False
                    break
            if found:
                res_indexes.append(i)

        if i < n - m:
            # print(f'i={i}, t={t}, p={p},c_prev={i, T[i]}, c_next={m + i, T[m + i]}, macth={res_indexes}')
            t = (d * (t - h * ord(T[i])) + ord(T[m + i])) % q
            t = t if t >= 0 else t + q

        # else:
        #     print(f'i={i}, t={t}, p={p},c_prev={i, T[i]}, c_next={None}, macth={res_indexes}')
    return res_indexes


#
# def str_to_int(s):
#     pass
#
#
# def int_to_base(n, N):
#     """ Return base N representation for int n. """
#     base_n_digits = None  # digits + ascii_lowercase + ascii_uppercase
#     result = ""
#     if n < 0:
#         sign = "-"
#         n = -n
#     else:
#         sign = ""
#     while n > 0:
#         q, r = divmod(n, N)
#         result += base_n_digits[r]
#         n = q
#     if result == "":
#         result = "0"
#     return sign + "".join(reversed(result))


if __name__ == '__main__':
    import gmpy

    T, P = 'abakhgiuaba990abre abrabababa', 'aba'
    print(naive_match(T, P))
    print(rabin_karp_match(T, P, q=10))

    # print(6 % 2)
    # print(Decimal('4.9') % Decimal('4'))
    # print(30 % 7)
    # print(-30 % 7)
    # print(str(([ord(c) for c in '100'])))
    # print(int(str(ord(c) for c in '100'), 19))
    # print(int(100,2))
    # print(gmpy.digits(9, 2))
    # print(ord('z') - ord(chr(ord('a')-1)))
    # print('0123'[2:])
