import os
import click


def calculate_fuel(crabs, position):
    fuel = 0
    for c in crabs:
        fuel += abs(c - position)
    return fuel


def run():
    f = open(os.getcwd() + '/year_2021/day07/input.txt')
    crabs = list(map(int, f.readline().split(',')))

    max_position = max(crabs)

    min_fuel = calculate_fuel(crabs, 0)

    for p in range(1, max_position):
        f = calculate_fuel(crabs, p)
        min_fuel = f if f < min_fuel else min_fuel

    click.echo(min_fuel)


if __name__ == "__main__":
    run()
