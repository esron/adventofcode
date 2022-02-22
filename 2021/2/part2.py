from sys import stdin

depth = 0
position = 0
aim = 0

for line in stdin:
    comand, value  = line.rstrip().split(' ')
    value = int(value)

    if comand == 'forward':
        position += value
        depth += value * aim
    if comand == 'down':
        aim += value
    if comand == 'up':
        aim -= value

print(depth * position)
