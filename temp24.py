def TSum(*t) -> float:
    v = 00.00
    if len(t) == 1:
        return t[0]
    for i in t:
        v = round(v+i,2)
        if v%1 >= 0.60:
            v -= 0.60
            v += 1
    return round(v,2)


def mine():
    print(TSum(4.03) == 4.03)
    print(TSum(02.05,01.58) == 4.03)
    print(TSum(02.05,00.58,01.00) == 4.03)

mine()