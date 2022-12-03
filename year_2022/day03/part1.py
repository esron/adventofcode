import os
import click


def run():
    f = open(os.getcwd() + '/year_2022/day03/input.txt')
    priority_sum = 0
    for line in f:
        line = line.rstrip()
        pocket_a, pocket_b =\
            set(line[:len(line) // 2]), set(line[len(line) // 2:])
        intersect = pocket_a.intersection(pocket_b)
        item = ''.join(intersect)
        priority_sum += ord(item) - 38 if item.isupper() else ord(item) - 96
    click.echo(priority_sum)


if __name__ == "__main__":
    run()
