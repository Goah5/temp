#n, k, x = list(map(int, input().split()))
#m = list(map(int, input().split()))
n, k, x = list(map(int, "6 3 3".split()))
m = list(map(int, "7 10 9 13 14 15".split()))


def f(n, k, x, m):
    print(ff([0]))


def ff(l):
    global n, k, x, m
    toret = []

    for i in l:
        if abs(m[i] - m[i-1]) <= x:
            toret += [ff(m[i])]
    return toret


print(f(n, k, x, m))
