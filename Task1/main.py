import nltk
import os

mypath = "../WikipediaArticles"

files = os.listdir(mypath)
print(files)

for i in range(len(files)):
    file = mypath + "/" + files[i]
    print(file)
    f = open(file, encoding="utf8")
    content = f.read()
    print(content)
