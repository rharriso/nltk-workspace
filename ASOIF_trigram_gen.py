import nltk, os, sys
from nltk.corpus import PlaintextCorpusReader

class ASOIFGenerator:
    def __init__(self):
        curr_dir = os.getcwd()

        # didn't include self folder in git,
        # because i'm not looking to get a cease and desist notice
        wordlists = PlaintextCorpusReader(curr_dir+"/ASOIAF/", ".*\.txt")
        self.words = wordlists.words()

        # get cfg tri and bigrams
        trigrams = nltk.trigrams(self.words)
        self.cfd_t = nltk.ConditionalFreqDist()
        for t in list(trigrams):
            self.cfd_t[t[0]+"|"+t[1]][t[2]] += 1
        bigrams = nltk.bigrams(self.words)
        self.cfd_b = nltk.ConditionalFreqDist(bigrams)

    #
    # use bigram only to generate
    #
    def generate_bigram_dumb(self, word0, n=15):
        for i in range(n):
            print(word0)
            word0 = self.cfd_b[word0].max()

    #
    # use bigram and then trigram to generate
    #
    def generate_bigram(self, word0, n=15):
        word1 = self.cfd_b[word0].max()
        self.generate_trigram(word0, word1, n)

    #
    # use trigram to generate
    #
    def generate_trigram(self, word0, word1, n=15):
        print(word0)

        for i in range(n):
            print(word1)
            word2 = self.cfd_t[word0+"|"+word1].max()
            word0 = word1
            word1 = word2
