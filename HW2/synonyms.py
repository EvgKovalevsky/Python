print("Команды:")
print("ADD arg1 arg2  - добавление слова синонима.")
print("COUNT arg1     - число синонимов у слова.")
print("CHECK arg1     - проверка на синонимы")
print("EXIT           - выход из программы")


def _input():
	s = input("> ")
	args = s.split()
	for arg in args:
		arg.lower()
	if (args[0] == "add" and len(args) == 3):
		return args
	elif (args[0] == "count" and len(args) == 2):
		return args
	elif (args[0] == "check" and len(args) == 3):
		return args
	elif (args[0] == "exit" and len(args) == 1):
		return args
	else:
		print("Браток, тут что-то не так. Повтори ввод")
		return _input()

def Add(sp, args):
	if (args[1] == args[2]):
		return sp
	for spack in sp:
		if(args[1] in spack and args[2] in spack):
			return sp
		elif(args[1] in spack and args[2] not in spack):
			spack.append(args[2])
			return sp
		elif(args[2] in spack and args[1] not in spack):
			spack.append(args[1])
			return sp
	sp.append([args[1], args[2]])
	return sp

def Count(sp, args):
	for spack in sp:
		for word in spack:
			if(word == args[1]):
				return len(spack) - 1
	return 0

def Check(sp, args):
	if (args[1] == args[2]):
		return ""
	for spack in sp:
		if(args[1] in spack and args[2] in spack):
			return "YES"
	return "NO"

sp = []
while True:
	args = _input();
	if (args[0] == "add"):
		sp = Add(sp, args)
		print(sp)
	elif (args[0] == "count"):
		print(Count(sp, args))
	elif (args[0] == "check"):
		print(Check(sp, args))
	elif (args[0] == "exit"):
		break
