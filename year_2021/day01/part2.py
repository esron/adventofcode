import os
import click


def run():
    f = open(os.getcwd() + '/year_2021/day01/input.txt')
    increased = 0
    values = []

    for line in f:
        values.append(int(line))

    firstWindown = values[0] + values[1] + values[2]
    secondWindown = values[1] + values[2] + values[3]
    for i in range(2, len(values) - 2):
        thirdWindow = values[i] + values[i+1] + values[i+2]

        if secondWindown > firstWindown:
            increased += 1

        firstWindown = secondWindown
        secondWindown = thirdWindow

    if secondWindown > firstWindown:
        increased += 1

    click.echo(increased)


if __name__ == "__main__":
    run()
