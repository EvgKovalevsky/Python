"""docstring"""
import bz2
import os
import json
import re

def unpack_archives(tmppath):
    """Find and unpack archives"""
    names = []
    for name in os.listdir():
        if name[0:2] == "RC":
            names.append(name)
    if not os.path.exists(tmppath):
        os.makedirs(tmppath)
    for name in names:
        with open(tmppath + "/" + name[0:-3], 'wb') as new_file, bz2.BZ2File(name, 'rb') as file:
            for data in file:
                new_file.write(data)

def parse_archives(tmppath):
    """Parse archives"""
    word_dict = {}
    for name in os.listdir(tmppath):
        for line in open(tmppath + "/" + name, "r"):
            data = json.loads(line)
            if data["body"] != "[deleted]":
                for word in re.findall(r"[\w']+", data["body"]):
                    if len(word) >= 4 and word not in word_dict.keys():
                        word_dict[word] = 1
                    elif len(word) >= 4:
                        word_dict[word] += 1
        print(name + " parsed")
    return word_dict

def set_output(dictionary, path):
    """Writing output Json-file"""
    sorted_list = [
        (i, dictionary[i]) for i in sorted(dictionary.keys(), key=dictionary.get, reverse=True)]
    dictionary.clear()
    for i in range(0, 20):
        dictionary[sorted_list[i][0]] = sorted_list[i][1]
    with open(path, 'w') as outfile:
        return json.dump(dictionary, outfile, sort_keys=False, indent=4)

JSON_FOLDER = "JsonFolder"
JSON_OUTPUT = "JsonOutput"

unpack_archives(JSON_FOLDER)
set_output(parse_archives(JSON_FOLDER), JSON_OUTPUT)
