import random as r

def getIndex(list):
    return r.randint(0, len(list))

def buildList(filepath, count):
    with open(filepath) as f: # not the best code but oh well
        names = []

        lines = []
        for line in f:
            lines.append(line)

        for x in range(count):
            names.append(lines[getIndex(lines)])
            
    string = ""
    for name in names:
        n = name.split('\n')[0]
        string += f"\t\"{n}\"," + "\n\t"
    return string


forePath = "./names/forenames.txt"
mPath = "./names/middle-names.txt"
surPath = "./names/surnames.txt"

forenames = ""
mnames = ""
surnames = ""

foreCount = int(input("Enter count of forenames to generate: ")) # im not input validating this, cant be bothered
mCount = int(input("Enter count of middle-names to generate: "))
surCount = int(input("Enter count of surnames to generate: "))

forenames = buildList(forePath, foreCount)
mnames = buildList(mPath, mCount)
surnames = buildList(surPath, surCount)



string = "{\n\t" + f"\"forenames\": [\n\t{forenames}],\n\t\"middlenames\": [\n\t{mnames}],\n\t\"surnames\": [\n\t{surnames}]" + "\n}"

print("\n\n")
print(string)
    