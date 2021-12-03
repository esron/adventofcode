from sys import stdin

input = []

for line in stdin:
    input.append(line.rstrip())

lineSize = len(input[0])

ones_zeros_count = []

for _ in range(0, lineSize):
    ones_zeros_count.append([0,0])

for value in input:
    for i in range(0, len(value.rstrip())):
        if line[i] == '1':
            ones_zeros_count[i][1] += 1
        else:
            ones_zeros_count[i][0] += 1
