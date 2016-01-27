# coding: utf-8


import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/home/rharriso/Code/Python/NLTKWorkspace'])
# gutenberg corpus
import nltk
nltk.corpus.gutenberg.fileids()
macBeth = nltk.corpus.gutenberg.words('shakespeare-macbeth.txt')
caesar = nltk.corpus.gutenberg.words('shakespeare-caesar.txt')
from nltk.corpus import gutenberg
# display some info about these
for fId in gutenberg.fileids():
    nChars = len(gutenberg.raw(fId))
    nWords = len(gutenberg.words(fId))
    nSent = len(gutenberg.sents(fId))
    nVocap = len(set[w.lower() for w in gutenberg.words(fid)])
for fId in gutenberg.fileids():
    nChars = len(gutenberg.raw(fId))
    nSent = len(gutenberg.sents(fId))
    nWords = len(gutenberg.words(fId))
    nVocab = len(set([w.lower() for w in gutenberg.words(fId)]))
    print(int(nChars/nWords), int(nWords/nSent), int(nWords/nVocab), fId)
#
#brown corpus
#
from nltk.corpus import brown
brown.categories()
sfText = brown.words(categories='science_fiction')
sfText
fDist = nltk.FreqDist([w.lower() for w in sfText])
modal = ['robot', 'space', 'science', 'mad', 'future']
for m in modal:
    print(m + ":", fdist[m])
for m in modal:
    print(m + ":", fDist[m])
brown.fileids(['science_fiction'])
for fId in brown.fileids(['science_fiction']):
    brown.citation()
#
#
# There is also a reuters corpus
#
from nltk.corpus import reuters
reuters.fileids()
reuters.categories()
reuters.categories()
reuters.categories('test/16591')
reuters.categories('training/9865')
#
#
#
from nltk import chat
chat.fileids()
#
#
#
# Plain text corpora
#
#
from nltk.corpus import PlaintextCorpusReader
exec 'pwd'
exec('pwd')
import os
os.system('pwd')
curr_dir = os.system('pwd')
wordlists = PlaintextCorpusReader(curr_dir, 'ASOIAF/*.txt')
wordlists = PlaintextCorpusReader(curr_dir, '/ASOIAF/*.txt')
wordlists = PlaintextCorpusReader(curr_dir+'/ASOIAF/', *.txt')
wordlists = PlaintextCorpusReader(curr_dir+'/ASOIAF/', '*.txt')
curr_dir = os.system('ls '+curr_dir+'/ASOIAF/')
os.system('ls '+curr_dir+'/ASOIAF/')
wordlists = PlaintextCorpusReader(curr_dir+'/ASOIAF/', '*.txt')
os.system("ls "+curr_dir)
os.system("ls "+curr_dir.str())
curr_dir
os.path.dirname(os.path.realpath(__file__))
os.getcwd()
curr_dir = os.getcwd()
os.system("ls "+curr_dir)
wordlists = PlaintextCorpusReader(curr_dir+'/ASOIAF/', '*.txt')
os.system("ls "+curr_dir+'/ASOIAF/', '*.txt')
os.system("ls "+curr_dir+'/ASOIAF/')
os.system("ls "+curr_dir+'/ASOIAF/')
wordlists = PlaintextCorpusReader(curr_dir+'/ASOIAF/', '*.txt')
wordlists = PlaintextCorpusReader(curr_dir+'/ASOIAF/', '.*\.txt')
wordlist
wordlists
wordlists.words()
wordlists.concordance("Arya")
wordlists.fileids()
#
# Can also import bracket parse corpora (penn tree bank)
get_ipython().magic('save -f january_26_2016.py 0 - *')
get_ipython().magic('save -f january_26_2016.py')
get_ipython().magic('save -f january_23_2016.py 0-*')
get_ipython().magic('save january_26_2016.py 0-1000000')
