from random import randint


def roll(inp):
    # NdX±C

    # inp = input().lower()
    # inp = "d20"

    n, c, = 1, 0
    d_index, zc_index = inp.find("d"), -1

    for i in ("+", "-"):
        if i in inp:
            zc_index = inp.find(i)
            c = int(inp[zc_index:])

    n = int(inp[:d_index]) if d_index != 0 else 1
    x = int(inp[d_index+1:zc_index] if zc_index != -1 else inp[d_index+1:])
    if (d_index, zc_index) == (0,0):
        x = int(inp)
        c = 0
        n = 1

    print(n, x, c)
    print(d_index, zc_index)

    return [randint(1, x)+c for _ in range(n)]


if __name__ == "__main__":
    inp = 0
    while not inp == "":
        inp = input().lower()
        print(*roll(inp))

    for i in ("d12", "4d5+2", "d7-2", "2 d10"):
        print(i, "\n", *roll(i))
