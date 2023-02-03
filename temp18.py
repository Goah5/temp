cell=[];num=int(input())
for i in range(num*10):
    if str(i**2)[-2:] == "25":cell.append(i**2)
print(cell[num-1])