import os
import re
import nltk
import json
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.parse.corenlp import CoreNLPParser
from nltk.tokenize import RegexpTokenizer
from pprint import pprint


class FeatureExtractor:
    path = ""
    files = []
    info = {}

    def __init__(self, _path=None):
        self.path = _path

    def run(self):
        files_name = os.listdir(self.path)

        for i in range(1):
            current_file = self.path + "/" + files_name[i]
            # print(current_file)
            _tuple = self.read_file(files_name[i].replace(".txt", ""), current_file)
            self.info[files_name[i]] = _tuple
        return self.info

    def read_file(self, name, _file):
        self.make_dir("info")
        f = open(_file, encoding="utf8")
        current_content = f.read()
        self.files.append(current_content)
        # print(current_content)
        sentences = nltk.sent_tokenize(current_content)

        return self.run_article(name, sentences)

    def run_article(self, _name, _sentences):
        print("processing {}".format(_name))
        dict_token = {}
        dict_lemma = {}
        dict_tag = {}
        dict_parser = {}
        dict_wordnet = {}
        tokenizer = RegexpTokenizer('\s+', gaps=True)
        for j in range(len(_sentences)):
            sent = self.clean_sentence(_sentences[j])

            print("processing tokens")
            dict_token[j] = tokenizer.tokenize(sent)
            print("processing lemma")
            dict_lemma[j] = self.lemma_generator(dict_token[j])
            print("processing tagging")
            dict_tag[j] = nltk.pos_tag(dict_lemma[j])
            # print("processing parsering")
            # dict_parser[j] = self.parser_generator(dict_lemma[j])
            # self.print_parser(dict_parser[j])
            print("processing sysnet")
            self.sysnet_generator(dict_lemma[j], dict_wordnet)
        self.write("info/token/", _name, dict_token)
        self.write("info/lemma/", _name, dict_lemma)
        self.write("info/tag/", _name, dict_tag)
        # self.write("info/parser/", _name, dict_parser)
        self.write("info/sysnet/", _name, dict_wordnet)
        return {"token": dict_token, "lemma": dict_lemma, "tag": dict_tag,
                "parser": dict_parser, "wordnet_feather": dict_wordnet}

    def write(self, directory, filename, data):
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(directory + filename + '.json', 'w') as fp:
            json.dump(data, fp)

    @staticmethod
    def clean_sentence(sentence):
        x = re.sub(r'(\n)', " ", sentence)
        return x.replace("\\", "")

    @staticmethod
    def make_dir(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

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
    extractor = FeatureExtractor("WikipediaArticles")
    extractor.run()
    # extractor.write()
    print()
