# Halp Me Sort, Pls

*Halp Me Sort* is a simple and quite idiosyncratic CLI tool that sorts all files within a folder into folders based on file type.

Imagine that you have a folder called `sort` with hundreds of random files. To help you sort these files, *Halp Me Sort* will first put them into folders based on their file type (e.g., all PDFs go into a `pdf` folder). By default, this target folder will always be the same. Hence, if you have multiple `sort` folders, the tool helps you aggregate them in one place. While doing so, duplicates will also be sorted into their own folder.

Of course, this is a completely arbitrary example as we always neatly sort our files and never start to just randomly put important files ~~junk~~ into `sort` folders.

Please note that this tool is *definitely not production ready* at all. I am sharing it here as it serves a very specific purpose for me, and there will be at least one more person for whom it will be helpful.

## Installation

1. Clone the repository `git clone https://github.com/IngoKl/halpmesort.git`
1. Change the `config.py` or create a PR for some actual configuration management 😅. Currently, my local preference is the default for `sorted_folder`.
1. Run `pip install .` within the folder. Alternatively, you can use `poetry`.

## Usage

Once installed, you can run `halp-me-sort`. You will need to supply a folder to sort as well as, for security reasons, explicitly disable "dry mode": `halp-me-sort . False`

This will move all files in `.` to subfolders in `sorted_folder` (`config.py`). For example, `./test.pdf` will be moved to `{sorted_folder}/pdf/test.pdf`.

## Development

This project uses `black` and `isort`. Run `poetry run black` and `poetry run isort` before committing.

### ToDo

- Switch to `logging`
- Switch to `argparse` or `Click`
- Implement a function to detect already existing duplicates in the `sorted_folder`
- Implement a function to sort folders
- Add (sanity) checks
- Add tests
