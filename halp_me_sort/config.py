# Default Configuration
config = {
    'sorted_folder': 'G:\\Sorted',
    'duplicate_folder': '#duplicates',
    'excluded_filetypes': [
        '.backup',
        '.ini',
        '.rtsz',
        '.pri',
        '.dbx-backup',
        '.dropbox',
        '.lock',
        '.lnk',
    ],
    'ebook_folder': './likely_ebooks',
    'ebook_folder_good_nc': './likely_ebooks/good_naming_convention',
    'ebook_folder_bad_nc': './likely_ebooks/bad_naming_convention',
    'ebook_page_threshold': 60,
    'ebook_naming_convention': r'[A-Z]{1}.*? [0-9]{4} - .*',
    'unwanted_files': [
        r'.*\.tmp',
        r'~\$.*\.doc$',
        r'~\$.*\.docx$',
    ],
}
