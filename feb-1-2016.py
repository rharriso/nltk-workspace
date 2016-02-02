# coding: utf-8


import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/home/rharriso/Code/Python/NLTKWorkspace'])

# Page 79 Natural language processing in python
from __future__ import division
import nltk, re, pprint
f = open('ASOIAF/A Clash of Kings A Song of Ice and Fire Book 2_nodrm.txt')
txt = f.read()
text = nltk.text(text)
text = nltk.text(nltk.tokenize(text))
text = nltk.text(nltk.word_tokenize(text))
nltk.word_tokenize(txt)
tokens = nltk.word_tokenize(txt)
text = nltk.Text(tokens)
text.concordance("Arya")
#
# Load a feed
#
import feedparser
import feedparser
llog = feedparser.parse("http://rharriso.github.io/feed.xml")
llog['feed']
llog['feed']['title']
len(llog.entries)
post = llog[2]
llog.entries[2]
post = llog.entries[2]
post.content
post
post.summary
nltk.clean_html(post.summary)
nltk.clean_html(post.summary.value)
nltk.html_clean(post.summary)
nltk.clean_html(post.summary.value)
nltk.clean_html(post.summary)
get_ipython().magic("save -f 'feb-1-2016.py' 0-1000000")
