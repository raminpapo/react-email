#!/usr/bin/env python3
"""
Repository Scanner and Classifier
Scans the repo, classifies files, and builds the initial file inventory.
"""

import os
import json
import hashlib
import mimetypes
from pathlib import Path
from datetime import datetime

# Binary file extensions to skip detailed docs
BINARY_EXTENSIONS = {
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.svg',
    '.pdf', '.zip', '.tar', '.gz', '.bz2', '.xz',
    '.woff', '.woff2', '.ttf', '.eot', '.otf',
    '.mp4', '.mp3', '.wav', '.avi', '.mov',
    '.exe', '.dll', '.so', '.dylib', '.a',
    '.pyc', '.pyo', '.class', '.jar',
    '.lock'  # lock files are generally binary or auto-generated
}

# Files to skip entirely
SKIP_PATTERNS = {
    'node_modules', '.git', '.next', 'dist', 'build',
    '.turbo', 'coverage', '.cache', '__pycache__',
    '.DS_Store', 'thumbs.db'
}

# Large file threshold (100MB)
LARGE_FILE_THRESHOLD = 100 * 1024 * 1024

def should_skip(path_str):
    """Check if path should be skipped"""
    parts = Path(path_str).parts
    return any(pattern in parts for pattern in SKIP_PATTERNS)

def classify_file(file_path):
    """Classify a file as text, binary, or large"""
    try:
        size = os.path.getsize(file_path)
        ext = os.path.splitext(file_path)[1].lower()

        if size > LARGE_FILE_THRESHOLD:
            return 'large', size

        if ext in BINARY_EXTENSIONS:
            return 'binary', size

        # Try to read as text
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                f.read(1024)  # Try reading first 1KB
            return 'text', size
        except (UnicodeDecodeError, PermissionError):
            return 'binary', size

    except Exception as e:
        return 'error', 0

def compute_repo_fingerprint(repo_path, commit_sha):
    """Compute a fingerprint for the repo state"""
    if commit_sha:
        return commit_sha

    # Fallback: hash of file list + sizes
    hasher = hashlib.sha256()
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if not should_skip(os.path.join(root, d))]
        for file in sorted(files):
            file_path = os.path.join(root, file)
            if not should_skip(file_path):
                try:
                    hasher.update(file_path.encode())
                    hasher.update(str(os.path.getsize(file_path)).encode())
                except:
                    pass
    return hasher.hexdigest()

def scan_repository(repo_path, commit_sha=None):
    """Scan repository and build file inventory"""

    file_inventory = {
        'text': [],
        'binary': [],
        'large': [],
        'error': []
    }

    total_size = 0

    for root, dirs, files in os.walk(repo_path):
        # Filter out skip patterns
        dirs[:] = [d for d in dirs if not should_skip(os.path.join(root, d))]

        for file in sorted(files):
            file_path = os.path.join(root, file)

            if should_skip(file_path):
                continue

            rel_path = os.path.relpath(file_path, repo_path)
            file_type, size = classify_file(file_path)

            file_info = {
                'path': rel_path,
                'absolute_path': file_path,
                'size': size,
                'extension': os.path.splitext(file)[1].lower()
            }

            file_inventory[file_type].append(file_info)
            total_size += size

    # Build manifest
    manifest = {
        'generator_version': '1.0.0',
        'repo_name': os.path.basename(repo_path),
        'repo_path': repo_path,
        'commit_sha': commit_sha,
        'repo_fingerprint': compute_repo_fingerprint(repo_path, commit_sha),
        'scan_timestamp': datetime.utcnow().isoformat() + 'Z',
        'file_counts': {
            'text': len(file_inventory['text']),
            'binary': len(file_inventory['binary']),
            'large': len(file_inventory['large']),
            'error': len(file_inventory['error']),
            'total': sum(len(v) for v in file_inventory.values())
        },
        'total_bytes': total_size,
        'file_inventory': file_inventory
    }

    return manifest

if __name__ == '__main__':
    import sys

    repo_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    commit_sha = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"Scanning repository: {repo_path}")
    print(f"Commit SHA: {commit_sha}")

    manifest = scan_repository(repo_path, commit_sha)

    # Save manifest
    output_path = os.path.join(repo_path, 'docs', 'manifest.json')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\nScan complete!")
    print(f"Text files: {manifest['file_counts']['text']}")
    print(f"Binary files: {manifest['file_counts']['binary']}")
    print(f"Large files: {manifest['file_counts']['large']}")
    print(f"Error files: {manifest['file_counts']['error']}")
    print(f"Total files: {manifest['file_counts']['total']}")
    print(f"Total size: {manifest['total_bytes'] / (1024*1024):.2f} MB")
    print(f"\nManifest saved to: {output_path}")
