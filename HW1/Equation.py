import math
from math import sqrt
A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

def Equation(a, b, c):
	if (a == 0 and b == 0):
		return ""
	elif (a == 0):
		return (-c / b)
	else:
		D = b**2 - 4*a*c
		if(D > 0):
			return "%.2f %.2f"%((-b + sqrt(D)) / (2 * a), (-b - sqrt(D)) / (2 * a))
		elif (D == 0):
			return (-b / (2 * a))
		else:
			return ""

print(Equation(A, B, C))

#Открытые тесты:

#Equation(2, 5, 2)
#Equation(2, 4, 2)
#Equation(2, 1, 2)
#Equation(0, 4, 10)