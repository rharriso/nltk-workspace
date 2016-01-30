# coding: utf-8


import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/home/rharriso/Code/Python/NLTKWorkspace'])
import nltk
import ASOIF_trigram_gen
ag = ASOIF_trigram_gen.ASOIFGenerator()
set(ag.words)
# how many words aren't just stop words
def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words("english")
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)
content_fraction(set(ag.words))
nltk.corpus.reuters.words()
nltk.corpus.gutenberg.words()
content_fraction(nltk.corpus.gutenberg.words())
type(ag.words)
i = 0
content = [w.lower() for w in ag.words]
content
content_fraction(ag.words)
nltk.corpus.gutenberg.words()
content_fraction(nltk.corpus.gutenberg.words())
content_fraction(ag.words)
# ASOIF uses 1.5% fewer stop words than the gutenberg corpus
#
#
# names word list
#
names = nltk.corpus.names
names.fileids()
maleNames = names.words("male.txt")
ladyNames = names.words('female.txt')
# cfd of first letters of names v gender
cfd = nltk.ConditionalFreqDist(
    (fileid, name[-1])
    for fileid in names.fileids()
    for name in names.words(fileid))
cfd.plot()
