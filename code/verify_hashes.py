"""Verify the finalized release's UTF-8 SHA256SUMS.txt before running checks."""
import hashlib
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    count = 0
    for line in (root/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
        digest, name = line.split('  ', 1)
        path = (root/name).resolve()
        if root not in path.parents or not path.is_file():
            raise ValueError('Missing or invalid manifest path: '+name)
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError('Digest mismatch: '+name)
        count += 1
    print(f'All {count} listed SHA-256 digests match.')


if __name__ == '__main__':
    main()
