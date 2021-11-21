def mineral_formation(input):
    if 1 in input[0] and 1 in input[-1]:
        return 'both'
    if 1 in input[0] :
        return 'stalactites'
    if 1 in input[-1]:
        return 'stalagmites'