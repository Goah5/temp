def f(a):
    for i in list(a):
        a.append(i+1)
        a.append(i-1)
    return a


def ff(a):
    t = {}
    for i in a:
        try:
            t[i] += 1

        except:
            t[i] = 1
    return (max(t.values()))



print(a := f(list(map(int, list(input())))), (ff(a)))
