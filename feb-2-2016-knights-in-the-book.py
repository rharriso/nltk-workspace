# coding: utf-8


import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/home/rharriso/Code/Python/NLTKWorkspace'])

# Page 79 Natural language processing in python
from __future__ import division
import nltk, re, pprint
import IndexedText
porter = nltk.PorterStemmer()
f = open('ASOIAF/A Clash of Kings A Song of Ice and Fire Book 2_nodrm.txt')
tokens = nltk.word_tokenize(f.read())
t = IndexedText.IndexedText(porter, tokens)
t.concordance("knight")
get_ipython().magic("save -f 'feb-2-2016-knights-in-the-book.py' 0-10000")
