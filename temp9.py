from itertools import product
c = int(input())
l = list(map(int, input().split()))


operands = l
# change '//' to '/' for floating point division
operators = ['+', '-']
for opers in product(operators, repeat=len(operands)-1):
    formula = [str(operands[0])]
    for op, operand in zip(opers, operands[1:]):
        formula.extend([op, str(operand)])
    formula = ' '.join(formula)
    if int(eval(formula)) == c:
        print('{} = {}'.format(formula, eval(formula)))
    