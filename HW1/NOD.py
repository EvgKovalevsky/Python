A = int(input("A = "))
B = int(input("B = "))

def NOD(a, b):
	while (a != 0 and b != 0):
		if (a > b):
			a = a % b
		else:
			b = b % a
	return (a + b)

print("NOD = %i"%(NOD(A, B)))

#Открытые тесты:

#NOD(25, 27)
#NOD(12, 16)
#NOD(13, 13)