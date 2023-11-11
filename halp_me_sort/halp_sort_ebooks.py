import re
import shutil
from pathlib import Path

from pypdf import PdfReader


class HalpSortPdfEbooks:
    """Sorts likely ebooks (PDF) from a folder into a new folder."""

    def __init__(self, config, folder_to_sort, dry_run=True):
        self.config = config

        self.dry_run = dry_run

        self.folder_to_sort = Path(folder_to_sort)

        self.ebook_folder = Path(config['ebook_folder'])
        self.ebook_folder_good_nc = Path(config['ebook_folder_good_nc'])
        self.ebook_folder_bad_nc = Path(config['ebook_folder_bad_nc'])

        if not self.dry_run:
            self.ebook_folder.mkdir(exist_ok=True)
            self.ebook_folder_good_nc.mkdir(exist_ok=True)
            self.ebook_folder_bad_nc.mkdir(exist_ok=True)

    def check_if_ebook(self, file):
        try:
            reader = PdfReader(file)
            if len(reader.pages) >= self.config['ebook_page_threshold']:
                return True
            else:
                return False
        except:
            False

    def check_naming_convention(self, filename):
        if re.search(self.config['ebook_naming_convention'], filename):
            return True
        else:
            return False

    def sort_ebooks(self):
        if self.dry_run:
            print('Dry Run – No files will be moved')

        artifacts = list(self.folder_to_sort.glob('*.pdf'))

        files = [artifact for artifact in artifacts if artifact.is_file()]

        for file in files:
            if self.check_if_ebook(file):
                good_nc = self.check_naming_convention(file.name)

                print(f'Found likely ebook: {file} (Good Naming Convention: {good_nc})')

                if good_nc:
                    print(f'Moving {file} to {self.ebook_folder_good_nc}')

                    if not self.dry_run:
                        shutil.move(file, Path(self.ebook_folder_good_nc, file.name))
                else:
                    print(f'Moving {file} to {self.ebook_folder_good_nc}')

                    if not self.dry_run:
                        shutil.move(file, Path(self.ebook_folder_bad_nc, file.name))
