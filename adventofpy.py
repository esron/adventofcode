import click


@click.command()
@click.option('-y', '--year', type=click.IntRange(2015, 2021), required=True,
              help='Event year')
@click.option('-d', '--day', type=click.IntRange(1, 25), required=True,
              help='Problem day')
@click.option('-p', '--part', type=click.Choice(['1', '2']), required=True,
              help='Problem part')
def cli(year: int, day: int, part: str):
    """Advent of Python

       Python solutions to Advent of Code."""
    click.echo(f'year: {year}, day: {day}, part: {part}')
