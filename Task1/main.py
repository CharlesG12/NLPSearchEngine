import nltk
nltk.download('punkt')
import os

mypath = "../WikipediaArticles"

files = os.listdir(mypath)
print(files)

for i in range(len(files)):
    file = mypath + "/" + files[i]
    print(file)
    print("*********************************************")
    f = open(file, encoding="utf8")
    content = f.read()
    # print(content)
    sentences = nltk.sent_tokenize(content)
    for i in range(len(sentences)):
        print(sentences[i])
        print()

