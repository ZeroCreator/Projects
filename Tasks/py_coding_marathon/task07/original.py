animals = ["dog", "cat", "bat", "cock", "cow", "pig",
           "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
           "frog", "hen", "mole", "duck", "goat"]


def count_animals(txt):
    counts = []
    def f(txt, c):
        for i in animals:
            s = txt
            for x in i:
                s = s.replace(x, "", 1)
            if len(s) + len(i) == len(txt):
                f(s, c + 1)
        counts.append(c)
    f(txt, 0)
    return max(counts)

if __name__ == '__main__':
    print(count_animals("cockdogwdufrbir"))