import nltk
import re
import os
import time

p = nltk.PorterStemmer()

b = re.compile(r"\b\w+\b")
tokens = b.findall(open("./text/de-bello-gallico.txt").read().lower())

def test(tokens):
    stems = []
    print("call...")
    for i in range(0, 10):
        print("loop...", i)
        stems = [p.stem(t) for t in tokens]

    return stems

start = time.time()
stems = test(tokens)
end = time.time()

print((end - start))

outPath = "./text/stem-bello-gallico.txt"
print("Outputting stems to: ", outPath)

if os.path.isfile(outPath):
    os.remove(outPath)
outF = open(outPath, "a+")

for s in stems:
    outF.write(s)
    outF.write("\n")
