# coding: utf-8


import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/home/rharriso/Code/Python/NLTKWorkspace'])

# Page 79 Natural language processing in python
from __future__ import division
import nltk, re, pprint
# Terrible tagger
#
raw = "I do not like green eggs and ham, I do not like them Sam I am!"
tokens = nltk.word_tokenize(raw)
default_tagger = nltk.DefaultTagger("NN")
default_tagger.tag(tokens)
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sets(categories='news')
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
default_tagger.evaluate(brown_tagged_sents)
#
#
# Reg tagger
#
patters = []
patters = [


(r'.*ing$', "VBG"), # gerunds


(r'.*ed$', "VBD"), # simple past


(r'.*es$', "VBZ"), # 3rd singular present


(r'.*ould$', "MD"), # modals


(r'.*\'s$', "NN"), # posessive nouns


(r'.*s$$', "NNS"), # plural noun


(r'.*', "NN"), # default noun ]


]
regexp_tagger = nltk.RegexpTagger(patters)
regexp_tagger.evaluate(brown_tagged_sents)
regexp_tagger.tag(brown_tagged_sents[3])
regexp_tagger.tag(brown_sents[3])
regexp_tagger.evaluate(brown_tagged_sents)
default_tagger.evaluate(brown_tagged_sents)
# Not really much better
#
# Frequency Lookup tagger
# uses how the word is mostly tagged
#
# Unigram Tagger
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
unigram_tagger.tag(brown_sets[2007])
unigram_tagger.tag(brown_sents[2007])
unigram_tagger.evaluate(brown_tagged_sents)
size = int(len(brown_tagged_sents) * 0.9)
size
tain_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
unigram_tagger = nltk.UnigramTagger(tain_sents)
unigram_tagger.evaluate(test_sents)
#
#
# Not so great when splitting
#
t0 = default_tagger
t1 = nltk.UnigramTagger(tain_sents, backoff=t0)
t2 = nltk.BigramTagger(tain_sents, backoff=t1)
t2.evaluate()
t2.evaluate(test_sents)
# a little better when using backoffs
get_ipython().magic("save -f 'feb-24-2016-Taggers.py' 0-10000")
