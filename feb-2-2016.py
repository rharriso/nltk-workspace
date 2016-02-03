# coding: utf-8


import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/home/rharriso/Code/Python/NLTKWorkspace'])

# Page 79 Natural language processing in python
from __future__ import division
import nltk, re, pprint
#
#
# Stemmer
#
#
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
f = open('ASOIAF/A Clash of Kings A Song of Ice and Fire Book 2_nodrm.txt')
txt = f.read()
text = nltk.Text(tokens)
tokens = nltk.word_tokenize(txt)
text = nltk.Text(tokens)
[porter.stem(w) for w in tokens[:100]]
[porter.stem(w) for w in tokens[1000:1100]]
[porter.stem(w)+" : "+w for w in tokens[1000:1100]]
[porter.stem(w)+" : "+w for w in tokens[990:1100]]
[lancaster.stem(w)+" : "+w for w in tokens[990:1100]]
[w+" : "+lancaster.stem(w)+" : "+porter.stem(w) for w in tokens[990:1100]]
import IndexedText
t = IndexedText(tokens)
t = IndexedText.IndexedText(tokens)
t = IndexedText.IndexedText(porter, tokens)
t.concordance("arya")
get_ipython().magic('save -f "feb-2-2016.py" 0-100000')
