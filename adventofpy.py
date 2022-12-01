import click
from importlib import import_module


@click.command()
@click.option('-y', '--year', type=click.IntRange(2015, 2022), required=True,
              help='Event year')
@click.option('-d', '--day', type=click.IntRange(1, 25), required=True,
              help='Problem day')
@click.option('-p', '--part', type=click.Choice(['1', '2']), required=True,
              help='Problem part')
def cli(year: int, day: int, part: str):
    """Advent of Python

       Python solutions to Advent of Code."""
    click.echo(f'Running script for year: {year}, day: {day:02d}, part: {part}')
    try:
        script = import_module(f'.part{part}', f'year_{year}.day{day:02d}')
        script.run()
    except ModuleNotFoundError:
        click.echo(f'Module year_{year}.day{day:02d}.part{part} not found.', err=True)
        exit(1)
