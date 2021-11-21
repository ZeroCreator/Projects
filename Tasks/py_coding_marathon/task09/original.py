def translator(txt):
    word = 'двуликий'
    res = []
    for char in bytearray(txt, 'utf-8'):
        b = '{:0>8b}'.format(char)
        new = ''.join(word[i].upper() if b[i] == '1' else word[i] for i in range(8))
        res.append(new)
    return ' '.join(res)

