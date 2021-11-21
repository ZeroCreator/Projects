def can_exit(lst):
    def step(x, y):
        if 0<=x<len(lst[0]) and 0<=y<len(lst) and lst[y][x] == 0:
            lst[y][x] = 2
            for dx, dy in ((0,-1), (0,1), (-1,0), (1,0)):
                step(x+dx, y+dy)
    step(0, 0)
    return lst[-1][-1] == 2