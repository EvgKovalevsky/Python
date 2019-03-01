import math
from math import sqrt
A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

def Equation(a, b, c):
	if (a == 0):
		print("x1 = %f"%(-c / b))
	else:
		D = b**2 - 4*a*c
		if(D > 0):
			print("x1 = %.1f      x2 = %.1f"%( (-b + sqrt(D)) / (2 * a), (-b - sqrt(D)) / (2 * a)))
		elif (D == 0):
			print("x1 = %.1f"%(-b / (2 * a)))
		else:
			print("Корней нет")

Equation(A, B, C)

#Открытые тесты:

#Equation(2, 5, 2)
#Equation(2, 4, 2)
#Equation(2, 1, 2)
#Equation(0, 4, 10)