import nltk
from os import walk

mypath = "../WikipediaArticles"
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    file = read(dirnames, "r")
    print(file)
    break

print(f)

