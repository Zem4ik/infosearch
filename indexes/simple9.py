_payload = [(1, 28), (2, 14), (3, 9), (4, 7), (5, 5), (7, 4), (9, 3), (14, 2), (28, 1)]


def cnt_bits(x):
    i = 0
    while (x >> i) > 0:
        i += 1
    return i


def simple9_encode_lst(lst):
    res = []
    i = 0
    while i < len(lst):
        j = i
        m = cnt_bits(lst[j])
        while j < len(lst) and (j - i + 1) * m <= 28:
            j += 1
            if j < len(lst):
                m = max(m, cnt_bits(lst[j]))
        num = simple9_encode(lst[i:j])
        res.append(num)
        i = j
    return res


def simple9_encode(x):
    n = len(x)
    x.reverse()
    res = 0
    res += (n << 28)
    m = 28 // n
    for i in range(n):
        res += (x[i] << (i * m + 28 % n))
    return res


def simple9_decode_lst(x):
    res = []
    for num in x:
        res += simple9_decode(num)
    return res


def simple9_decode(x):
    res = []
    n = x >> 28
    m = 28 // n
    for i in range(n):
        ll = (28 - i * m)
        cur = (x & ((1 << ll) - 1)) >> (ll - m)
        res.append(cur)
    return res


def x_to_str(x):
    s = ''
    for i in range(32):
        if (x & (1 << i)) > 0:
            s += '1'
        else:
            s += '0'
        i += 1
    return s[::-1]
