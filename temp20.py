import sympy as sy
from sympy import *
x = symbols('x')
a = 2*x+1
b = x-1
print(factor(a/b))