import sys

import click
import pkg_resources

from halp_me_sort.config import config
from halp_me_sort.halp_deduplicate import HalpDeduplicate
from halp_me_sort.halp_sort import HalpSort


@click.group()
def cli():
    pass


@click.command()
@click.argument('folder_to_sort', type=click.Path(exists=True))
@click.argument('dry_run')
def sort(folder_to_sort, dry_run):
    click.echo('Sorting the folder.')
    dry_run = True if dry_run == 'True' else False

    click.echo(f'Sorting {folder_to_sort} (Dry Run: {dry_run})')

    halp = HalpSort(config=config, folder_to_sort=folder_to_sort)
    halp.sort_files(dry_run=dry_run)
    halp.print_duplicates()


@click.command()
@click.argument('folder_to_deduplicate', type=click.Path(exists=True))
def find_duplicates(folder_to_deduplicate):
    click.echo('Finding duplicates in the folder.')

    halp = HalpDeduplicate(config=config, folder_to_deduplicate=folder_to_deduplicate)
    halp.deduplicate_files()


cli.add_command(sort)
cli.add_command(find_duplicates)


if __name__ == "__main__":
    cli()
