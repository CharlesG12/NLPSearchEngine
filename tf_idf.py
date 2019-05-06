import nltk
import string
import os
import re
import numpy as np
import pandas as pd

from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer

path = "WikipediaArticles"
token_dict = {}
stemmer = PorterStemmer()


def get_stemms(_tokens, _stemmer):
    _stemmed = []
    for word in _tokens:
        _stemmed.append(_stemmer.stem(word))
    return _stemmed


def tokenize(text):
    _tokens = nltk.word_tokenize(text)
    stems = get_stemms(_tokens, stemmer)
    return stems


def get_tokens():
    _dicts = {}
    file_names = os.listdir(path)
    for i in range(2):
        current_file = path + "/" + file_names[i]
        _name = re.search("\\w?", file_names[i])
        # read_file(_name, current_file)
        with open(current_file, 'r', encoding='utf-8-sig') as pearl:
            text = pearl.read()
            read_file(_name, text)


def read_file(_name, _sentence):
        lowers = _sentence.lower()
        no_punctuation = re.sub(r'[^\w]', ' ', lowers)
        token_dict[_name] = no_punctuation


get_tokens()
tvec = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tvec_weights = tvec.fit_transform(token_dict.values())
feature_names = tvec .get_feature_names()
weights = np.asarray(tvec_weights.mean(axis=0)).ravel().tolist()
weights_df = pd.DataFrame({'term': tvec.get_feature_names(), 'weight': weights})
weights_df.sort_values(by='weight', ascending=False).head(20)

print(weights_df.sort_values(by='weight', ascending=False).head(20))
# features_df = pd.DataFrame(tfs[0], feature_names)
# lemmas = pd.concat([tfs, features_df])

# dict_stem_tfidf = {}
# for col in tfs.nonzero()[1]:
#     print(feature_names[col], ' - ', tfs[0, col])
#     dict_stem_tfidf[feature_names[col]] = tfs[0, col]

print()


















# tokens = get_tokens()
# stemmed = get_stemms(tokens, stemmer)
# count = Counter(stemmed)
# print(count.most_common(100))

# import nltk
# import string
# import os
# from sklearn.feature_extraction.text import TfidfVectorizer
# from nltk.stem.porter import PorterStemmer
# from nltk.corpus import stopwords
#
#
# path = "WikipediaArticles"
# token_dict = {}
#
#
# def tokenize(_text):
#     tokens = nltk.word_tokenize(_text)
#     stems = []
#     for item in tokens:
#         stems.append(PorterStemmer().stem(item))
#     return stems
#
#
# files_name = os.listdir(path)
# for i in range(1):
#     current_file = path + "/" + files_name[i]
#     with open(current_file) as pearl:
#         current_content = pearl.read()
#         token_dict[files_name[i]] = current_content.lower()
#
# # for dirpath, dirs, files in os.walk(path):
# #     print("ok")
# #     for f in files:
# #         fname = os.path.join(dirpath, f)
# #         # print"fname=", fname
# #         with open(fname) as pearl:
# #             text = pearl.read()
# #             token_dict[f] = text.lower().translate(None, string.punctuation)
#
# stopWords = set(stopwords.words('english'))
# tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words=stopWords)
# tfs = tfidf.fit_transform(token_dict.values())
#
# _str = 'all great and precious things are lonely.'
# response = tfidf.transform([_str])
# print(response)
#
# feature_names = tfidf.get_feature_names()
# for col in response.nonzero()[1]:
#     print(str(feature_names[col]) + ' - ' + str(response[0, col]))
