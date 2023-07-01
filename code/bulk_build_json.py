"""
Written by: DiamondDev
License: Public Domain

This is a probably mediocre python script that builds a list of forenames, middle names and surnames 
from the datasets and compiles them to a easy-to-use JSON file. (Builds to ./out/generated_names.json)
"""

import named_list as nl
import random as r

def getIndex(list):
    return r.randint(0, len(list))

def buildList(filepath, count):
    with open(filepath) as f: # not the best code but oh well
        names = []

        lines = []
        for line in f:
            lines.append(line)

        i = count
        while i > 0:
            x = getIndex(lines)
            if (lines[x] not in names):
                names.append(lines[x])
                i -= 1
                print(f"[filepath={filepath}] Obtained {count-i}/{count}")
            
    string = ""
    i = len(names)
    for name in names:
        n = name.split('\n')[0]
        comma = ""
        if (i > 1): comma = ","
        string += f"\t\"{n}\"" + comma + "\n\t"
        i -= 1
    return string




outpath = "./out/generated_names.json"

forenames = ""
mnames = ""
surnames = ""

## main

foreCount = int(input("Enter count of forenames to generate: ")) # im not input validating this, cant be bothered
mCount = int(input("Enter count of middle-names to generate: "))
surCount = int(input("Enter count of surnames to generate: "))

forenames = buildList(nl.forePath, foreCount)
mnames = buildList(nl.mPath, mCount)
surnames = buildList(nl.surPath, surCount)


string = "{\n\t" + f"\"forenames\": [\n\t{forenames}],\n\t\"middlenames\": [\n\t{mnames}],\n\t\"surnames\": [\n\t{surnames}]" + "\n}"

nl.prepFile(outpath)

print("\n\n")

with open(outpath, 'w') as f:
    f.write(string)

print(f"Written to {outpath}!")