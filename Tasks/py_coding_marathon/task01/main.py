def hamming_distance(a, b):
    first_str = list(a)
    second_str = list(b)
    count = 0

    for i in range(len(first_str)):
        if first_str[i] != second_str[i]:
            count += 1

    return count

if __name__ == '__main__':
    print(hamming_distance("abcde", "bcdef"))
    print(hamming_distance("abcde", "abcde"))
    print(hamming_distance("strong", "strung"))
    print(hamming_distance("ABBA", "abba"))

