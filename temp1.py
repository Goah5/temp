from random import *
import time


def txpo1(n: int):
	p = []
	while n != 1:
		p.append(n)
		if n % 2 == 0:
			n = n // 2
		else:
			n = (n * 3) + 1
	p.append(1)  # ± 1
	return p

def txpo2(num):
	class FoundCyclicalPattern(Exception):
		pass
	results = []
	while num != 1:
		if num in results:
			raise FoundCyclicalPattern()
		results.append(num)
		if num % 2:
			num = 3*num+1
		else:
			num = num//2
	results.append(1)
	return results

def txpo3(x):
	if x > 1:
		return (x,) + txpo3((3 * x + 1) if x % 2 else x//2)
	return (1,)


a = 10**(3*500)

FList = [txpo1, txpo2, txpo3]
for n, f in enumerate(FList, start=1):
	try:
		start = time.time()
		t = f(a)
		end = time.time()
		print(n, "	", end - start)
	except:
		print(n, "   ", -n)
