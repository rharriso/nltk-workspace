# coding: utf-8
import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/home/rharriso/Code/Python/NLTKWorkspace'])
import nltk
nltk.download()
from nltk.book import *

# concordance shows words used in the same context
text1.concordance("monstrous")
text1.concordance("oar")
text1.similar("monstrous")
text2.similar("monstrous")
text1.common_contexts(["monstrous", "impalpable"])

# average number of times a word is used
def lexical_diversity(text):
    return len(text) / len(set(text))


texts = [text1, text2, text3, text4, text5, text6]
[lexical_diversity(t) for t in texts]
[[t, lexical_diversity(t)] for t in texts]
get_ipython().magic('save -f january23_2016_1.py 0-100000')
