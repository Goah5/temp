import itertools

def f(a):
    return a

n = int(input("n = "))
bl = tuple(input())
a = tuple(input())
b = f(bl)
for i in itertools.permutations(a,len(a)):
    for j in itertools.permutations(b,len(b)):
        j = j + ("+0",)
        if eval(f'n=='+''.join([i[k]+j[k] for k in range(len(a))])):
            print(f'n=='+''.join([i[k]+j[k] for k in range(len(a))]))
    b = f(bl)