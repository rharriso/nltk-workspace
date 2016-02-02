# coding: utf-8


import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/home/rharriso/Code/Python/NLTKWorkspace'])

# Page 79 Natural language processing in python
from __future__ import division
import nltk, re, pprint
#
# tokenize asoiaf
#
f = open('ASOIAF/A Clash of Kings A Song of Ice and Fire Book 2_nodrm.txt')
raw = f.read()
len(raw)
raw[:125]
tokens = nltk.tokenize.word_tokenize(raw)
tokens[:20]
tokens[:25]
text = nltk.Text(tokens)
text
text.collocations()
text.collocations("Arya")
text.collocations("Iron")
raw.find("Arya")
get_ipython().magic('save -f "january-31-2016-quickie.py" 0:10000000')
