"""Synonyms program"""
def add(dictionary, args):
    """Adding synonyms"""
    if args[1] in dictionary.keys():
        if args[2] not in dictionary[args[1]]:
            dictionary[args[1]].append(args[2])
        if args[2] in dictionary.keys():
            if args[1] not in dictionary[args[2]]:
                dictionary[args[2]].append(args[1])
        else:
            dictionary[args[2]] = [args[1]]
    elif args[2] in dictionary.keys():
        if args[1] not in dictionary[args[2]]:
            dictionary[args[2]].append(args[1])
        if args[1] in dictionary.keys():
            if args[2] not in dictionary[args[1]]:
                dictionary[args[1]].append(args[2])
        else:
            dictionary[args[1]] = [args[2]]
    else:
        dictionary[args[1]] = [args[2]]
        dictionary[args[2]] = [args[1]]
    return dictionary


def count(dictionary, args):
    """Counting synonym"""
    if args[1] in dictionary.keys():
        return len(dictionary[args[1]])
    return 0


def check(dictionary, args):
    """Checking synonyms"""
    if args[1] in dictionary.keys() and args[2] in dictionary[args[1]]:
        return "YES"
    return "NO"


MYDICT = dict()
for i in range(0, int(input("Кол-во запросов: "))):
    ARGS = [arg.lower() for arg in (input("> ")).split()]
    if ARGS[0] == "add":
        add(MYDICT, ARGS)
    if ARGS[0] == "count":
        print(count(MYDICT, ARGS))
    if ARGS[0] == "check":
        print(check(MYDICT, ARGS))
