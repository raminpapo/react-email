#!/usr/bin/env python3
"""
Per-Folder Documentation Generator
Creates index.md, doc.md, and sub.md for each folder.
"""

import os
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def get_folder_structure(docs_path, repo_path):
    """Build a tree of all folders in the docs directory"""
    folders = defaultdict(lambda: {'files': [], 'subdirs': [], 'path': ''})

    for root, dirs, files in os.walk(docs_path):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        rel_root = os.path.relpath(root, docs_path)
        if rel_root == '.':
            rel_root = ''

        # Collect documentation files (not the original source files)
        doc_files = [f for f in files if f.endswith('_docs.md') or f.endswith('_kw.md')]
        other_files = [f for f in files if not f.endswith('_docs.md') and not f.endswith('_kw.md') and f.endswith('.md')]

        folders[rel_root]['files'] = doc_files
        folders[rel_root]['other_files'] = other_files
        folders[rel_root]['subdirs'] = sorted(dirs)
        folders[rel_root]['path'] = rel_root

    return folders

def generate_folder_index(folder_path, folder_info, docs_path):
    """Generate index.md for a folder"""

    folder_name = os.path.basename(folder_path) if folder_path else 'Root'

    doc = []
    doc.append(f"# Index: {folder_name}\n\n")
    doc.append(f"**Folder Path:** `{folder_path if folder_path else '/'}`\n")
    doc.append(f"**Generated:** {datetime.utcnow().isoformat()}Z\n\n")
    doc.append("---\n\n")

    # Table of contents
    doc.append("## Contents\n\n")

    # Subdirectories
    if folder_info['subdirs']:
        doc.append("### Subdirectories\n\n")
        for subdir in sorted(folder_info['subdirs']):
            subdir_link = f"{subdir}/index.md" if folder_path else f"{subdir}/index.md"
            doc.append(f"- [{subdir}/]({subdir_link})\n")
        doc.append("\n")

    # Documentation files (group by source file)
    docs_files = [f for f in folder_info['files'] if f.endswith('_docs.md')]
    kw_files = [f for f in folder_info['files'] if f.endswith('_kw.md')]

    # Extract base filenames
    base_files = set()
    for df in docs_files:
        base = df.replace('_docs.md', '')
        base_files.add(base)

    if base_files:
        doc.append("### Files\n\n")
        doc.append("| File | Documentation | Keywords |\n")
        doc.append("|------|---------------|----------|\n")

        for base_file in sorted(base_files):
            docs_link = f"{base_file}_docs.md"
            kw_link = f"{base_file}_kw.md"

            has_docs = docs_link in folder_info['files']
            has_kw = kw_link in folder_info['files']

            docs_cell = f"[View]({docs_link})" if has_docs else "-"
            kw_cell = f"[View]({kw_link})" if has_kw else "-"

            doc.append(f"| `{base_file}` | {docs_cell} | {kw_cell} |\n")

        doc.append("\n")

    # Other markdown files (like this index, doc, sub)
    if folder_info.get('other_files'):
        doc.append("### Documentation\n\n")
        for other in sorted(folder_info['other_files']):
            if other not in ['index.md', 'doc.md', 'sub.md']:
                doc.append(f"- [{other}]({other})\n")
        doc.append("\n")

    doc.append("---\n\n")

    # Navigation
    doc.append("## Navigation\n\n")
    if folder_path:
        parent = os.path.dirname(folder_path)
        parent_link = "../index.md" if parent else "../index.md"
        doc.append(f"- [↑ Parent Directory]({parent_link})\n")
    doc.append("- [📚 Documentation Overview](doc.md)\n")
    doc.append("- [🔍 Keywords Index](sub.md)\n")
    doc.append("- [🏠 Root Index](../index.md)\n" if folder_path else "- [🏠 Root Index](index.md)\n")

    return ''.join(doc)

def generate_folder_doc(folder_path, folder_info, docs_path, repo_path):
    """Generate doc.md (narrative context) for a folder"""

    folder_name = os.path.basename(folder_path) if folder_path else 'react-email'

    doc = []
    doc.append(f"# Documentation: {folder_name}\n\n")
    doc.append(f"**Folder Path:** `{folder_path if folder_path else '/'}`\n")
    doc.append(f"**Generated:** {datetime.utcnow().isoformat()}Z\n\n")
    doc.append("---\n\n")

    doc.append("## Overview\n\n")

    # Try to infer folder purpose from structure
    has_package_json = any('package.json' in f for f in folder_info['files'])
    has_src = 'src' in folder_info['subdirs']
    has_test = any('test' in s or 'tests' in s for s in folder_info['subdirs'])
    has_components = 'components' in folder_info['subdirs']

    if not folder_path:
        doc.append("This is the root directory of the react-email repository. ")
        doc.append("React Email is a library for building email templates with React components.\n\n")
    else:
        doc.append(f"This directory (`{folder_path}`) contains ")

        if has_package_json:
            doc.append("a Node.js package. ")

        if has_src:
            doc.append("source code in the `src/` subdirectory. ")

        if has_test:
            doc.append("test files. ")

        if has_components:
            doc.append("React components. ")

        doc.append("\n\n")

    # File statistics
    doc.append("## Structure\n\n")
    doc.append(f"- **Subdirectories:** {len(folder_info['subdirs'])}\n")
    doc.append(f"- **Documentation Files:** {len([f for f in folder_info['files'] if f.endswith('_docs.md')])}\n")
    doc.append(f"- **Keyword Files:** {len([f for f in folder_info['files'] if f.endswith('_kw.md')])}\n\n")

    # List subdirectories
    if folder_info['subdirs']:
        doc.append("### Subdirectories\n\n")
        for subdir in sorted(folder_info['subdirs']):
            doc.append(f"- `{subdir}/`\n")
        doc.append("\n")

    doc.append("## Purpose & Concepts\n\n")
    doc.append("*This section provides narrative context about the role and architecture of this directory.*\n\n")

    # Infer purpose based on common patterns
    folder_lower = folder_path.lower() if folder_path else 'root'

    if 'src' in folder_lower or 'source' in folder_lower:
        doc.append("This is a source code directory containing the implementation files.\n\n")
    elif 'test' in folder_lower or 'tests' in folder_lower or '__tests__' in folder_lower:
        doc.append("This directory contains test files for validating functionality.\n\n")
    elif 'docs' in folder_lower or 'documentation' in folder_lower:
        doc.append("This directory contains documentation files.\n\n")
    elif 'examples' in folder_lower or 'demo' in folder_lower:
        doc.append("This directory contains example code and demonstrations.\n\n")
    elif 'components' in folder_lower:
        doc.append("This directory contains reusable component definitions.\n\n")
    elif 'utils' in folder_lower or 'helpers' in folder_lower:
        doc.append("This directory contains utility functions and helper modules.\n\n")
    elif 'config' in folder_lower or 'configs' in folder_lower:
        doc.append("This directory contains configuration files.\n\n")
    elif 'scripts' in folder_lower:
        doc.append("This directory contains build scripts and automation tools.\n\n")

    doc.append("---\n\n")
    doc.append("*For detailed file-by-file analysis, see the individual documentation files linked in the index.*\n\n")

    return ''.join(doc)

def generate_folder_keywords(folder_path, folder_info, docs_path):
    """Generate sub.md (merged keyword index) for a folder"""

    folder_name = os.path.basename(folder_path) if folder_path else 'Root'

    doc = []
    doc.append(f"# Keywords Index: {folder_name}\n\n")
    doc.append(f"**Folder Path:** `{folder_path if folder_path else '/'}`\n")
    doc.append(f"**Generated:** {datetime.utcnow().isoformat()}Z\n\n")
    doc.append("---\n\n")

    doc.append("## About\n\n")
    doc.append("This is a merged keyword index for all files in this directory and its subdirectories.\n\n")
    doc.append("Keywords are organized alphabetically (A-Z) with links to their source documentation.\n\n")

    # Collect all keywords from _kw.md files in this folder
    all_keywords = defaultdict(list)

    kw_files = [f for f in folder_info['files'] if f.endswith('_kw.md')]

    for kw_file in kw_files:
        file_path = os.path.join(docs_path, folder_path, kw_file) if folder_path else os.path.join(docs_path, kw_file)

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Simple parsing: look for lines like "- **`keyword`** (category) - ..."
            import re
            matches = re.findall(r'-\s+\*\*`([^`]+)`\*\*\s+\(([^)]+)\)', content)

            for keyword, category in matches:
                # Link to the source keyword file
                all_keywords[keyword].append((category, kw_file))

        except Exception as e:
            pass

    # Sort and output A-Z
    doc.append("---\n\n")

    if all_keywords:
        sorted_keywords = sorted(all_keywords.items(), key=lambda x: x[0].lower())

        current_letter = None
        for keyword, sources in sorted_keywords:
            first_letter = keyword[0].upper()

            if first_letter != current_letter:
                if current_letter is not None:
                    doc.append("\n")
                doc.append(f"## {first_letter}\n\n")
                current_letter = first_letter

            # List all sources for this keyword
            categories = ', '.join(set(cat for cat, _ in sources))
            source_links = ', '.join(set(f"[{src}]({src})" for _, src in sources))

            doc.append(f"- **`{keyword}`** ({categories}) - Found in: {source_links}\n")

    else:
        doc.append("*No keywords found in this directory.*\n\n")

    return ''.join(doc)

def main():
    repo_path = '.'
    docs_path = './docs'

    print("Analyzing folder structure...")
    folders = get_folder_structure(docs_path, repo_path)

    print(f"Found {len(folders)} folders to document")

    folders_processed = 0

    for folder_path, folder_info in sorted(folders.items()):
        try:
            # Create folder documentation directory
            full_path = os.path.join(docs_path, folder_path) if folder_path else docs_path

            # Generate index.md
            index_content = generate_folder_index(folder_path, folder_info, docs_path)
            index_file = os.path.join(full_path, 'index.md')
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(index_content)

            # Generate doc.md
            doc_content = generate_folder_doc(folder_path, folder_info, docs_path, repo_path)
            doc_file = os.path.join(full_path, 'doc.md')
            with open(doc_file, 'w', encoding='utf-8') as f:
                f.write(doc_content)

            # Generate sub.md
            sub_content = generate_folder_keywords(folder_path, folder_info, docs_path)
            sub_file = os.path.join(full_path, 'sub.md')
            with open(sub_file, 'w', encoding='utf-8') as f:
                f.write(sub_content)

            folders_processed += 1

            if folders_processed % 20 == 0:
                print(f"Processed {folders_processed}/{len(folders)} folders...")

        except Exception as e:
            print(f"Error processing folder {folder_path}: {e}")

    print(f"\n=== Folder Documentation Complete ===")
    print(f"Folders processed: {folders_processed}")

if __name__ == '__main__':
    main()
