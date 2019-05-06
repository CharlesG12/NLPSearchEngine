import math
import os
import re
import nltk
from textblob import TextBlob as tb
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


def tf(word, _blob):
    return _blob.words.count(word) / len(_blob.words)


def n_containing(word, _bloblist):
    return sum(1 for _blob in _bloblist if word in _blob.words)


def idf(word, _bloblist):
    return math.log(len(_bloblist) / (1 + n_containing(word, _bloblist)))


def tfidf(word, _blob, _bloblist):
    return tf(word, _blob) * idf(word, _bloblist)

texts = []
path = "WikipediaArticles"
stemmer = PorterStemmer()


def read_file():
    file_names = os.listdir(path)
    for _i in range(3):
        current_file = path + "/" + file_names[_i]
        # _name = re.search("\\w?", file_names[_i])
        with open(current_file, 'r', encoding='utf-8-sig') as pearl:
            text = pearl.read()
            formatted = format_article(text)
            text_tb = tb(formatted)
            texts.append(text_tb)


def format_article(_text):
    stemmed = []
    lowers = _text.lower()
    no_punctuation = re.sub(r'[^\w]', ' ', lowers)
    tokens = nltk.word_tokenize(no_punctuation)
    filtered = [w for w in tokens if w not in stopwords.words('english')]
    for item in filtered:
        stemmed.append(stemmer.stem(item))
    seperator = ' '
    return seperator.join(stemmed)


read_file()
for i, blob in enumerate(texts):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:10]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))

