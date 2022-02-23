from sys import stdin

count = 0

for line in stdin:
    output = line.rstrip().split('|')[1].lstrip().split(' ')
    for s in output:
        if len(s) in (2, 3, 4, 7):
            count += 1

print(count)
