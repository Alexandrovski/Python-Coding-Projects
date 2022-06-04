counts = dict()
line = input("Type a sentence")
words = line.split()
print(words)
for word in words:
    counts[word] = counts.get(word,0) + 1
print(counts)
