"""
Written by: DiamondDev
License: Public Domain

Script used to merge 7 years worth of name data from dlsun/pods with named-list's dictionary.

dlsun/pods -> https://github.com/dlsun/pods
"""
import named_list as nl # import namedlist
import time

def buildLink(year):
    return f"https://raw.githubusercontent.com/dlsun/pods/master/data/names/yob{year}.txt"

def scrapeName(line): ## dlsun/pods's name files contain a little more information about each name (sex and occurences), but we only need the name
    return str(line).split(',')[0] # the structure is b'[name,sex,occurences]', so we get index 0 after splitting at commas, then truncate

def createFilename(start, end):
    return f"dlsun_scraped_names_yob{start}-yob{end}.txt"

## main
startYear = 2000
endYear = 2021

outFilename = ""

allScrapedNames = []

startTime = time.perf_counter()

for year in range(startYear, endYear+1): # Scrape names
    url = buildLink(year)
    print(f"Scraping name data from year {year} [{url}]")

    text = nl.getRemoteTextFileLines(url)
    names = []
    for line in text:
        names.append(scrapeName(line)[2:])

    for name in names: allScrapedNames.append(name)

    print(f"Scraped {len(names)} names from year {year}!")
    print()

# print scrape results
print()
print(f"Scraped {len(allScrapedNames)} total names over a course of {endYear - startYear + 1} years of name data!")

# Remove duplicate names
trimmedScrapedNames = nl.removeDuplicates(allScrapedNames)
print()
print(f"Removed {len(allScrapedNames) - len(trimmedScrapedNames)} duplicate names!")

# Merge with existing
mergedTrimmedScrapedNames = nl.createMergedList(nl.forePath, trimmedScrapedNames)
print()
print(f"Merged and removed {len(mergedTrimmedScrapedNames) - len(trimmedScrapedNames)} duplicate names!")

# Write to file
outFilename = createFilename(startYear, endYear)
nl.buildTxtList(mergedTrimmedScrapedNames, outFilename)
print()
print(f"Written {len(mergedTrimmedScrapedNames)} scraped, trimmed and merged names to [./out/{outFilename}]!")

endTime = time.perf_counter()
print()
print()
print(f"Completed in {endTime - startTime:0.3f} seconds.")