def harry(po):
    n, m = len(po), len(po[0])
    if n == 0 or m == 0:
        return -1
    if n == 1 and m == 1:
        return po[0][0]
    for c in range(1, m):
        po[0][c] += po[0][c-1]
    for r in range(1, n):
        po[r][0] += po[r-1][0]
    for r in range(1, n):
        for c in range(1, m):
            po[r][c] += max(po[r-1][c], po[r][c-1])
    return po[-1][-1]