import itertools #permutations
s = input()
t = [int(''.join(i)) for i in itertools.permutations(s)]

for i in t:
    if i%8 == 0:
        print(i)