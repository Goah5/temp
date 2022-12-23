def f(t, s):
    c = 0
    for i in range(len(t)):
        if t[i:i+len(s)] == s:
            c += 1
    return c


r = input()
n = len(r)
a = []
for i in range(n):
    for j in range(i, n+1):
        if f(r, r[i:j]) > 1:
            a.append(len(r[i:j]))

print(max(a))
