# Деление в столбик (Нет)
a, b = list(map(int,input().split()))
l = []
i = 0
av = None
while a==av:
	av = a
	for i in range(1,a)[::-1]:
		if (a <=(b*i)):
			pass
		l.append(b*i)
		print(f"{a} // {b*i} = {(a / (b*i))}")
		a = a-b*i
		break

		
print(l)

