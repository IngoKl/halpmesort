import sys
from importlib import metadata

import click

from halp_me_sort.config import config
from halp_me_sort.halp_deduplicate import HalpDeduplicate
from halp_me_sort.halp_folders import HalpEmptyFolders
from halp_me_sort.halp_sort import HalpSort
from halp_me_sort.halp_sort_ebooks import HalpSortPdfEbooks
from halp_me_sort.halp_unwanted_files import HalpUnwantedFiles


@click.group()
@click.version_option()
def cli():
    version = metadata.version("halp_me_sort")
    click.echo(f'Halp Me Sort {version}')
    pass


@click.command()
@click.argument('folder_to_sort', type=click.Path(exists=True))
@click.argument('dry_run')
@click.option('--sorted_folder', help='Folder to sort files into.')
def sort(folder_to_sort, dry_run, sorted_folder):
    """Sort the files in folder_to_sort according to file extension."""
    click.echo('Sorting the folder.')
    dry_run = True if dry_run == 'True' else False

    click.echo(f'Sorting {folder_to_sort} (Dry Run: {dry_run})')

    halp = HalpSort(
        config=config,
        folder_to_sort=folder_to_sort,
        sorted_folder=sorted_folder,
        dry_run=dry_run,
    )
    halp.sort_files()
    halp.print_duplicates()


@click.command()
@click.argument('folder_to_sort', type=click.Path(exists=True))
@click.argument('dry_run')
def sort_ebooks(folder_to_sort, dry_run):
    """Find likely ebooks (PDF) in folder_to_sort and move them to a new folder."""
    click.echo('Sorting the folder.')
    dry_run = True if dry_run == 'True' else False

    click.echo(f'Sorting {folder_to_sort} (Dry Run: {dry_run})')

    halp = HalpSortPdfEbooks(
        config=config,
        folder_to_sort=folder_to_sort,
        dry_run=dry_run,
    )
    halp.sort_ebooks()


@click.command()
@click.argument('folder_to_deduplicate', type=click.Path(exists=True))
def find_duplicates(folder_to_deduplicate):
    """Deduplicates files in folder_to_deduplicate."""
    click.echo('Finding duplicates in the folder.')

    halp = HalpDeduplicate(config=config, folder_to_deduplicate=folder_to_deduplicate)
    halp.deduplicate_files()


@click.command()
@click.argument('folder_to_check', type=click.Path(exists=True))
def find_empty_folders(folder_to_check):
    """Recursively finds empty folders."""
    click.echo('Finding empty folders.')

    halp = HalpEmptyFolders(config=config, folder_to_check=folder_to_check)
    halp.find_empty_folders()


@click.command()
@click.argument('folder_to_check', type=click.Path(exists=True))
@click.argument('dry_run')
def remove_unwanted_files(folder_to_check, dry_run):
    """Recursively finds and removes unwanted files."""
    click.echo('Finding unwanted files.')
    dry_run = True if dry_run == 'True' else False

    click.echo(f'Deleting unwanted files in {folder_to_check} (Dry Run: {dry_run})')

    halp = HalpUnwantedFiles(
        config=config, folder_to_check=folder_to_check, dry_run=dry_run
    )
    halp.find_unwanted_files()


cli.add_command(sort)
cli.add_command(find_duplicates)
cli.add_command(sort_ebooks)
cli.add_command(find_empty_folders)
cli.add_command(remove_unwanted_files)


if __name__ == "__main__":
    cli()
