import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.strip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 0:
            numlist.append(stuff)
print(max(numlist))
