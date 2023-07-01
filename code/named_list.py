"""
Written by: DiamondDev
License: Public Domain

Library Code used for named-list, merging operations, and more.
"""

import os
import urllib.request

forePath = "./names/forenames.txt"
mPath = "./names/middlenames.txt"
surPath = "./names/surnames.txt"

def prepFile(path : str) -> None:
    if (os.path.exists(path)):
        return
    else:
        dirs = path.split("/")
        try:
            os.makedirs(dirs[len(dirs)-2])
        except (OSError): print("Directories already exist, skipping..")
                
        open(path, "x")

def buildExistingListAsPythonList(path : str) -> list:
    pylist = []
    with open(path) as f:
        for line in f:
            pylist.append(line)
    return pylist

def checkListContains(path : str, name : str) -> bool:
    return (name in buildExistingListAsPythonList(path))

def createMergedList(path, toMerge):
    pylist = buildExistingListAsPythonList(path)
    for name in toMerge:
        if (not checkListContains(path, name)):
            pylist.append(name)
    return pylist

def buildTxtList(list : list, outFilename : str) -> None:
    path = f"./out/{outFilename}"
    prepFile(path)

    stringlist = ""

    for name in list:
            n = str(name).split('\n')[0]
            stringlist += f"{n}\n"

    with open(path, 'w') as f:
        f.write(stringlist)

def getRemoteTextFileLines(url : str) -> list:
    return list(urllib.request.urlopen(url))

def removeDuplicates(l: list) -> list:
    return list(dict.fromkeys(l))

    