# coding: utf-8


import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/home/rharriso/Code/Python/NLTKWorkspace'])
import nltk
from nltk.book import *
fdist1 = FreqDist(text1)
fdist1['whale']
len(fdist1)
words = set(text1)
long_words = [w for w in words if len(w) > 15]
len(long_words)
sorted(len(long_words))
sorted(long_words)
[[w, fdist1[w]] for w in long_words]
[[w, fdist1[w]] for w in long_words] # frequency of long words
[[w, fdist1[w]] for w in words if len(w) <= 4] # frequency of short words
[[w, fdist1[w]] for w in words if len(w) <= 2] # frequency of very short words
get_ipython().magic('save -f january23_2016_2.py 0-100000')
