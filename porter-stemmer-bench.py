import nltk
import re
import os
import time

p = nltk.PorterStemmer()

b = re.compile(r"\b\w+\b")
tokens = b.findall(open("./text/de-bello-gallico.txt").read().lower())

def test(tokens):
    print("call...")
    for i in range(0, 10):
        print("loop...", i)
        [p.stem(t) for t in tokens]

start = time.time()
test(tokens)
end = time.time()

print((end - start))
