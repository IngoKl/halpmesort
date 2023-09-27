import hashlib


def hash_file(file):
    with open(file, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()
