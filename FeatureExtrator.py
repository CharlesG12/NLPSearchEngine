import os
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.parse.corenlp import CoreNLPParser


class FeatherExtractor:
    path = ""
    files = []
    info = {}

    def __init__(self, _path):
        self.path = _path

    def read_files(self):
        self.files = os.listdir(self.path)

        for i in range(1):
            current_file = self.path + "/" + self.files[i]
            # print(current_file)
            _tuple = self.read_file(current_file)
            self.info[self.files[i]] = _tuple

    def read_file(self, _file):
        f = open(_file, encoding="utf8")
        current_content = f.read()
        # print(current_content)
        sentences = nltk.sent_tokenize(current_content)
        return self.run(sentences)

    def run(self, _sentences):
        dict_token = {}
        dict_lemma = {}
        dict_tag = {}
        dict_parser = {}
        for j in range(len(_sentences)):
            dict_token[j] = nltk.word_tokenize(_sentences[j])
            # print(_tokens)
            dict_lemma[j] = self.lemma_generator(dict_token[j])
            # print(_lemmas)
            dict_tag[j] = nltk.pos_tag(dict_lemma[j])
            # print(_tagged)
            dict_parser[j] = self.parser_generator(dict_lemma[j])

            # for k in range(len(dict_lemma[j])):
            #     self.sysnet_generator(dict_lemma[j][k])
        return {"token": dict_token, "lemma": dict_lemma, "tag": dict_tag, "parser": dict_parser}

    @staticmethod
    def lemma_generator(_tokens):
        lemmatizer = WordNetLemmatizer()
        lemmas = []
        for i in range(len(_tokens)):
            lemma = lemmatizer.lemmatize(_tokens[i])
            lemmas.append(lemma)
        return lemmas

    @staticmethod
    def sysnet_generator(_word):
        for synset in wn.synsets(_word):
            print()
            print(synset)
            nyms = ['hypernyms', 'hyponyms', 'part_meronyms', 'part_holonyms']
            for n in nyms:
                try:
                    print(n, end=" ")
                    print(getattr(synset, n)())
                except AttributeError as e:
                    print(e)
                    pass

    @staticmethod
    def parser_generator(_words):
        lemma_sent = " ".join(_words)
        parser = CoreNLPParser(url='http://localhost:9000')
        # next(parser.raw_parse(lemma_sent)).pretty_print()
        return parser.raw_parse(lemma_sent)


if __name__ == "__main__":
    extractor = FeatherExtractor("WikipediaArticles")
    extractor.read_files()
    print()
