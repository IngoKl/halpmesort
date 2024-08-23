import re
from pathlib import Path


class HalpUnwantedFiles:
    def __init__(self, config, folder_to_check, dry_run=True):
        self.config = config

        self.dry_run = dry_run

        self.folder_to_check = Path(folder_to_check)

        self.unwanted_files = []

    def find_unwanted_files(self):
        """Recursively finds and removes unwanted files."""
        artifacts = list(self.folder_to_check.glob('**/*'))
        files = [artifact for artifact in artifacts if artifact.is_file()]

        if self.dry_run:
            print('Dry Run – No files will be deleted')

        for file in files:
            for unwanted_file in self.config['unwanted_files']:
                if re.match(unwanted_file, file.name):
                    print(f'Found unwanted file: {file.name}')
                    self.unwanted_files.append(file)

        if not self.dry_run:
            for unwanted_file in self.unwanted_files:
                print(f'Deleting {unwanted_file.name}')
                unwanted_file.unlink()
