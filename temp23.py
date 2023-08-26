
a, b, c = map(int, input().split())


def check(a, b, c):
    a, b, c = sorted([a,b,c])
    if a == b == c:
        return ('3eqSide')
    elif a**2 + b**2 == c**2:
        return ('2/')
    elif a == b or b == c or c == a:
        return ('2eqSides')
    else:
        return ('noEqSides')


print(check(a, b, c))
