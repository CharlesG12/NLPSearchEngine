import os
from nltk.stem import WordNetLemmatizer
from nltk.parse.corenlp import CoreNLPParser
from nltk.corpus import wordnet as wn
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
            for synset in wn.synsets(lemma):
                print(synset)
                print()
                nyms = ['hypernyms', 'hyponyms', 'part_meronyms', 'part_holonyms']
                for n in nyms:
                    try:
                        print(n, end=" ")
                        print(getattr(synset, n)())
                    except AttributeError as e:
                        print(e)
                        pass

        lemma_sent = " ".join(lemmatizes)
        tagged = nltk.pos_tag(lemmatizes)
        # parser = CoreNLPParser(url='http://localhost:9000')
        # next(parser.raw_parse(lemma_sent)).pretty_print()

        # print("TOKENS:   ")
        # print(tokens)
        # print()
        # print("LEMMA:   ")
        # print(lemmatizes)
        # print()
        # print("TAG:     ")
        # print(tagged)
        # print()

