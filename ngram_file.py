import os

from itertools import izip_longest
each_
itercons(iterable, 3)
iterslice(iterable, 3)


def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

frequencies = {}
	
for ftype in os.listdir("data"):
    for fname in os.listdir(os.path.join("data", ftype)):
		frequencies[ftype] = {}
		filepath = os.path.join("data", ftype, fname)
		with open(filepath, 'rb') as f:
			data = f.read()
		for ngram in grouper(3, data):
			
			frequencies[ftype][ngram] = frequencies[ftype].get(ngram, 0) + 1
			
print frequencies
