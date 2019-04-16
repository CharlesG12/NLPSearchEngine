from FeatureExtrator import FeatureExtractor


def extract_feather():
    extractor = FeatureExtractor("WikipediaArticles")
    extractor.read_files()


if __name__ == "__main__":
    extract_feather()
    # extractor.write()
    print()