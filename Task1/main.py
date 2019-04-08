import os
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

mypath = "../WikipediaArticles"

files = os.listdir(mypath)
print(files)

# for i in range(len(files)):
for i in range(1):
    file = mypath + "/" + files[i]
    print()
    print(file)
    print("*********************************************")
    print()
    f = open(file, encoding="utf8")
    content = f.read()
    # print(content)
    sentences = nltk.sent_tokenize(content)
    for i in range(len(sentences)):
        # print(sentences[i])
        # print()
        tokens = nltk.word_tokenize(sentences[i])
        lemmatizer = WordNetLemmatizer()
        lemmatizes = []
        for j in range(len(tokens)):
            lemma = lemmatizer.lemmatize(tokens[j])
            lemmatizes.append(lemma)

        tagged = nltk.pos_tag(lemmatizes)
        print("TOKENS:   ")
        print(tokens)
        print()
        print("LEMMA:   ")
        print(lemmatizes)
        print()
        print("TAG:     ")
        print(tagged)
        print()

