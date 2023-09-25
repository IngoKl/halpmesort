import sys

import pkg_resources

from halp_me_sort.config import config
from halp_me_sort.halp import HalpSort


def cli(config=config):
    args = sys.argv
    if len(args) < 2:
        print(f'Halp Me Sort {pkg_resources.get_distribution("halp_me_sort").version}')
        print('Usage: halp_me_sort <folder_to_sort> <dry_run True/False>')
        sys.exit(1)

    folder_to_sort = args[1]
    dry_run = True if args[2] == 'True' else False

    print(f'Sorting {folder_to_sort} (Dry Run: {dry_run})')

    halp = HalpSort(config=config, folder_to_sort=folder_to_sort)
    halp.sort_files(dry_run=dry_run)
    halp.print_duplicates()


if __name__ == "__main__":
    cli()
