from sys import stdin


def main():
    increased = 0
    previous = int(input())
    print(previous)
    actual = int(input())
    print(actual)
    if actual > previous:
        increased += 1
    for line in stdin:
        print(f'line {line}', end='')
        previous = actual
        actual = int(line)
        if actual > previous:
            increased += 1
    print(increased)
