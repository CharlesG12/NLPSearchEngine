from FeatureExtrator import FeatureExtractor

testing = FeatureExtractor("WikipediaArticles")


def test_clean_sentence():
    sentence = "Sam\\'s home is the\nbest."
    result = testing.clean_sentence(sentence)
    assert result == "Sam's home is the best."


test_clean_sentence()
