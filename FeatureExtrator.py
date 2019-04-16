import os
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.parse.corenlp import CoreNLPParser
from pprint import pprint


class FeatureExtractor:
    path = ""
    files = []
    info = {}

    def __init__(self, _path):
        self.path = _path

    def write(self):
        for article, value in self.info.items():
            print()

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
        dict_wordnet = {}
        # for j in range(len(_sentences)):
        for j in range(20):
            print("processing tokens")
            dict_token[j] = nltk.word_tokenize(_sentences[j])
            print("processing lemma")
            dict_lemma[j] = self.lemma_generator(dict_token[j])
            print("processing tagging")
            dict_tag[j] = nltk.pos_tag(dict_lemma[j])
            print("processing parsering")
            dict_parser[j] = self.parser_generator(dict_lemma[j])
            # self.print_parser(dict_parser[j])
            print("processing sysnet")
            self.sysnet_generator(dict_lemma[j], dict_wordnet)
        return {"token": dict_token, "lemma": dict_lemma, "tag": dict_tag,
                "parser": dict_parser, "wordnet_feather": dict_wordnet}

    @staticmethod
    def lemma_generator(_tokens):
        lemmatizer = WordNetLemmatizer()
        lemmas = []
        for i in range(len(_tokens)):
            lemma = lemmatizer.lemmatize(_tokens[i])
            lemmas.append(lemma)
        return lemmas

    def sysnet_generator(self, sentence, dict_wordnet):
        for k in range(len(sentence)):
            self.word_sysnet(sentence[k], dict_wordnet)

    @staticmethod
    def word_sysnet(_word, dict_wordnet):
        for synset in wn.synsets(_word):
            nyms = {"hypernyms": [], "hyponyms": [], "part_meronyms": [], "part_holonyms": []}
            # for n in nyms:
            for attr, value in nyms.items():
                try:
                    value = getattr(synset, attr)()
                    if len(value) > 0:
                        nyms[attr] = [o._name for o in value]
                except AttributeError as e:
                    print(e)
                    pass
            dict_wordnet[synset._name] = nyms

    @staticmethod
    def parser_generator(_words):
        lemma_sent = " ".join(_words)
        parser = CoreNLPParser(url='http://localhost:9000')
        # next(parser.raw_parse(lemma_sent)).pretty_print()
        return parser.raw_parse(lemma_sent)

    @staticmethod
    def print_parser(_parser):
        next(_parser).pretty_print()


if __name__ == "__main__":
    extractor = FeatherExtractor("WikipediaArticles")
    extractor.read_files()
    # extractor.write()
    print()
