import shutil
from pathlib import Path


class HalpEmptyFolders:
    def __init__(self, config, folder_to_check):
        self.config = config

        self.folder_to_check = Path(folder_to_check)

        self.empty_folders = []

    def find_empty_folders(self):
        for folder in self.folder_to_check.rglob('*'):
            # Check if the path is a directory and if it is empty
            if folder.is_dir() and not any(folder.iterdir()):
                self.empty_folders.append(folder)

        print(f'Found {len(self.empty_folders)} empty folders.')
        if len(self.empty_folders) > 0:
            self.print_empty_folders()

    def print_empty_folders(self):
        print('\n')
        for folder in self.empty_folders:
            print(folder)
