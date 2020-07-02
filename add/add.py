def add(*args):
    if not const_lens(args) or not const_lens([item for sublist in args for item in sublist]):
        raise ValueError('all lists must be the same length')
    rows = len(args[0])
    cols = len(args[0][0])
    buf = [[0] * cols for _ in range(rows)]
    for arg in args:
        for i in range(rows):
            for j in range(cols):
                buf[i][j] += arg[i][j]
    return buf

def const_lens(lists):
    return all([len(list) == len(lists[0]) for list in lists])


if __name__ == '__main__':
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[-1, -2, -3], [-4, -5, -6]]
    print(add(m1, m2))
