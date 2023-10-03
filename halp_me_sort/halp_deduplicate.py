import shutil
from pathlib import Path

from halp_me_sort.halpers import hash_file


class HalpDeduplicate:
    def __init__(self, config, folder_to_deduplicate):
        self.config = config

        self.duplicate_folder = Path(folder_to_deduplicate, config['duplicate_folder'])
        self.duplicate_folder.mkdir(exist_ok=True)

        self.folder_to_deduplicate = Path(folder_to_deduplicate)

        self.hashes = {}
        self.duplicates = []

    def deduplicate_files(self):
        artifacts = list(self.folder_to_deduplicate.glob('*'))

        files = [artifact for artifact in artifacts if artifact.is_file()]

        for file in files:
            hash = hash_file(file)

            if hash not in self.hashes:
                self.hashes[hash] = [file]
            else:
                self.hashes[hash].append(file)
                print(f'Found duplicate: {file}')
                print(f'Moving {file} to {self.duplicate_folder}')

                shutil.move(file, Path(self.duplicate_folder, file.name))

        self.duplicates = [
            self.hashes[hash] for hash in self.hashes if len(self.hashes[hash]) > 1
        ]

        if len(self.duplicates) == 0:
            print('No duplicates found')
