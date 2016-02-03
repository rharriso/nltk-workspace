import nltk
#
# User stemmer to nomalize text
#

class IndexedText(object):

    def __init__(self, stemmer, text):
        self.mText = text
        self.mStemmer = stemmer
        self.mIndex = nltk.Index((self.stem(word), i)
                                 for (i, word) in enumerate(text))


    def concordance(self, word, width=40):
        key = self.stem(word)
        wc = int(width/4)    # words of context
        for i in self.mIndex[key]:
            lcontext = ' '.join(self.mText[i-wc:i])
            rcontext = ' '.join(self.mText[i:i+wc])
            ldisplay = '%*s'  % (width, lcontext[-width:])
            rdisplay = '%*s'  % (width, rcontext[:width])
            print(ldisplay, rdisplay)


    def stem(self, word):
        return self.mStemmer.stem(word).lower()