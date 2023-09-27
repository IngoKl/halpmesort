import shutil
from pathlib import Path

from halp_me_sort.halpers import hash_file


class HalpSort:
    def __init__(self, config, folder_to_sort):
        self.sorted_folder = Path(config['sorted_folder'])
        self.sorted_folder.mkdir(exist_ok=True)

        self.duplicate_folder = Path(self.sorted_folder, config['duplicate_folder'])
        self.duplicate_folder.mkdir(exist_ok=True)

        self.folder_to_sort = Path(folder_to_sort)

        self.hashes = {}
        self.duplicates = []

    def sort_files(self, dry_run=True):
        artifacts = list(self.folder_to_sort.glob('*'))

        files = [artifact for artifact in artifacts if artifact.is_file()]
        filetypes = set([file.suffix for file in files if file.suffix != ''])
        # folders = [artifact for artifact in artifacts if artifact.is_dir() and artifact.name != sort_folder.name]

        if dry_run:
            print('Dry Run')

        for filetype in filetypes:
            print(f'\n{filetype}')

            folder = Path(self.sorted_folder, filetype[1:])
            if not dry_run:
                folder.mkdir(exist_ok=True)

            for file in [f for f in files if f.suffix == filetype]:
                hash = hash_file(file)

                if hash not in self.hashes:
                    self.hashes[hash] = [file]
                    print(f'Moving {file} to {folder}')
                    if not dry_run:
                        shutil.move(file, Path(folder, file.name))
                else:
                    self.hashes[hash].append(file)
                    print(f'Found duplicate: {file}')
                    print(f'Moving {file} to {self.duplicate_folder}')

                    if not dry_run:
                        shutil.move(file, Path(self.duplicate_folder, file.name))

        self.duplicates = [
            self.hashes[hash] for hash in self.hashes if len(self.hashes[hash]) > 1
        ]

    def print_duplicates(self):
        print('\nDuplicates')

        if len(self.duplicates) == 0:
            print('No duplicates found')
        else:
            for i, duplicate in enumerate(self.duplicates):
                print(f' Duplicate {i}')
                for file in duplicate:
                    print(f'  {file}')