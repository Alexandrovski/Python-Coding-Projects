fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    if not line.startswith('From'): continue
    words = line.split()
    if len(words) > 2:
        long = words
    print(long[2])
