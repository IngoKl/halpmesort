import hashlib


def hash_file(file):
    try:
        with open(file, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    except PermissionError:
        print(f'Could not hash {file} due to a permission error.')
        return None
