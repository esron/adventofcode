from sys import stdin

depth = 0
position = 0

for line in stdin:
    comand, value  = line.rstrip().split(' ')
    if comand == 'forward':
        position += int(value)
    if comand == 'down':
        depth += int(value)
    if comand == 'up':
        depth -= int(value)

print(depth * position)
