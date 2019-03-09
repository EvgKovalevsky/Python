def Add(sl, args):
	if args[1] in sl.keys():
		if args[2] not in sl[args[1]]:
			sl[args[1]].append(args[2])
		if args[2] in sl.keys():
			if args[1] not in sl[args[2]]:
				sl[args[2]].append(args[1])
		else:
			sl[args[2]]=[args[1]]
	elif args[2] in sl.keys():
		if args[1] not in sl[args[2]]:
			sl[args[2]].append(args[1])
		if args[1] in sl.keys():
			if args[2] not in sl[args[1]]:
				sl[args[1]].append(args[2])
		else:
			sl[args[1]]=[args[2]]
	else:
		sl[args[1]]=[args[2]]
		sl[args[2]]=[args[1]]
	return sl

def Count(sl, args):
	if args[1] in sl.keys():
		return len(sl[args[1]])
	return 0

def Check(sp, args):
	if args[1] in sl.keys() and args[2] in sl[args[1]]:
		return "YES"
	return "NO"

sl = {}

for i in range(0, int(input("Кол-во запросов: "))):
	args = (input("> ")).split()
	args = [arg.lower() for arg in args]
	if args[0] == "add":
		Add(sl, args)
	if args[0] == "count":
		print(Count(sl, args))
	if args[0] == "check":
		print(Check(sl, args))
