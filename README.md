# Halp Me Sort, Pls

![halp-me-sort-header](https://github.com/IngoKl/halpmesort/assets/16179317/6c584b2f-d106-43ee-b58e-19a1f47680c9)

*Halp Me Sort* is a simple and quite idiosyncratic CLI tool that, first and foremost, sorts all files within a folder into folders based on file type.

Imagine that you have a folder called `sort` with hundreds of random files. To help you sort these files, *Halp Me Sort* will first put them into folders based on their file type (e.g., all PDFs go into a `pdf` folder). By default, this target folder will always be the same. Hence, if you have multiple `sort` folders, the tool helps you aggregate them in one place. While doing so, duplicates will also be sorted into their own folder.

Of course, this is a completely arbitrary example as we always neatly sort our files and never start to just randomly put important files ~~junk~~ into `sort` folders.

Please note that this tool is *definitely not production ready* at all. I am sharing it here as it serves a very specific purpose for me, and there will be at least one more person for whom it will be helpful.

## Installation

1. Clone the repository `git clone https://github.com/IngoKl/halpmesort.git`
1. Change the `config.py` or create a PR for some actual configuration management 😅. Currently, my local preferences are the default for `sorted_folder` as well as for the `excluded_filetypes`.
1. Run `pip install .` within the folder. Alternatively, you can use `poetry`.

## Usage

Once installed, you can run `halp-me-sort`.

*Halp Me Sort* currently has six features:

1. Sorting files according to their file extension. You will need to supply a folder to sort as well as, for security reasons, explicitly disable "dry mode": `halp-me-sort sort . False`. This will move all files in `.` to subfolders in `sorted_folder` (`config.py`). For example, `./test.pdf` will be moved to `{sorted_folder}/pdf/test.pdf`.
1. Finding duplicates in a given folder. Run `halp-me-sort find-duplicates .` to move all duplicates in `.` to a duplicates folder.
1. Finding likely ebooks (based on the number of pages) and sorting them away. This can be used to approach a larger folder of PDFs. The tool also takes into account a naming convention for ebooks. Run `halp-me-sort sort-ebooks . False` to sort likely ebooks into separate folders based on their page count and the naming convention.
1. Finding empty folders recursively. Run `halp-me-sort find-empty-folders .` to find all empty folders in `.`.
1. Finding and removing unwanted files recusively (currently `*.tmp` and `*.~$.doc`, `*.~§.docx`). Run `halp-me-sort remove-unwanted-files . True` to find and remove all unwanted files in `.`.
1. Sorting files in a folder by year (e.g., all files from 2025 will be sorted into `sorted_folder/2025`).

## Development

This project uses `black` and `isort`. Run `poetry run black` and `poetry run isort` before committing.

To run the CLI during development, you can run `poetry run halp-me-sort`.

### ToDo

Currently, the most essential task is to implement better configuration management. This would include refactoring the existing code allowing users to change configuration options via CLI options.

- [ ] Switch to `logging`
- [ ] Implement a function to detect already existing duplicates in the `sorted_folder`
- [ ] Implement a function to sort/move folders
- [ ] Implement a function to cleverly rename files (e.g., too long)
- [ ] Add (sanity) checks
- [ ] Add tests
- [ ] Add sensible configuration management
- [ ] Add CLI option to overwrite the configuration
- [ ] Use Click to handle the `bool` type of `dry_run`
- [X] Implement a function to sort files by year
- [X] Implement a function to find empty folders
- [X] Add tool to sort away likely ebooks (PDF)
- [X] Add setting to exclude file types
- [X] Add CLI option for custom {sorted_folder}
- [X] Implement a function to find duplicates in a folder.
- [X] Switch to `argparse` or `Click`
