x = float(input())
y = 5/x+(2*x)
with open("output.txt", "w") as somefile:
	somefile.write(str(y))