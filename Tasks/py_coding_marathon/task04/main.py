def is_pandigital(num):
    if sorted(set(str(num))) == list('0123456789'):
        return True
    return False


if __name__ == '__main__':
    print(is_pandigital(98140723568910))
    print(is_pandigital (90864523148909))
    print(is_pandigital (112233445566778899))
