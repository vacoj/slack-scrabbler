#!/usr/bin/python

from sys import argv

results = ""
letters = "abcdefghijklmnopqrstuvwxyz"
for i in argv[1:]:
    for j in i:
        j = j.lower()
        if j in letters:
            results += ":" + j + "-ce:"
    results += "     "

print(results)
