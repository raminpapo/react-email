#!/usr/bin/env python3
"""
Global Documentation Generator
Creates keywords.md, index.md, and comprehensive_book.md
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def collect_all_keywords(docs_path):
    """Collect all keywords from all _kw.md files"""
    all_keywords = defaultdict(list)

    for root, dirs, files in os.walk(docs_path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        for file in files:
            if file.endswith('_kw.md'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, docs_path)

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Parse keywords
                    matches = re.findall(r'-\s+\*\*`([^`]+)`\*\*\s+\(([^)]+)\)', content)

                    for keyword, category in matches:
                        all_keywords[keyword].append({
                            'category': category,
                            'file': rel_path,
                            'source_file': file.replace('_kw.md', '')
                        })

                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    return all_keywords

def generate_global_keywords(all_keywords, docs_path):
    """Generate the global keywords.md file"""

    doc = []
    doc.append("# Global Keywords Index\n\n")
    doc.append("**Repository:** react-email\n")
    doc.append(f"**Total Keywords:** {len(all_keywords):,}\n")
    doc.append(f"**Generated:** {datetime.utcnow().isoformat()}Z\n\n")
    doc.append("---\n\n")

    doc.append("## About\n\n")
    doc.append("This is a comprehensive A-Z index of all keywords, identifiers, functions, classes, ")
    doc.append("and types found across the entire repository.\n\n")
    doc.append("Each keyword links to the files where it appears.\n\n")
    doc.append("---\n\n")

    # Generate A-Z sections
    sorted_keywords = sorted(all_keywords.items(), key=lambda x: x[0].lower())

    current_letter = None
    for keyword, sources in sorted_keywords:
        first_letter = keyword[0].upper()

        if first_letter != current_letter:
            if current_letter is not None:
                doc.append("\n")
            doc.append(f"## {first_letter}\n\n")
            current_letter = first_letter

        # Get unique categories
        categories = ', '.join(sorted(set(s['category'] for s in sources)))

        # Create links to source files (limit to avoid extremely long lines)
        source_links = []
        for src in sources[:10]:  # Limit to 10 sources per keyword
            link = f"[{src['source_file']}]({src['file']})"
            if link not in source_links:
                source_links.append(link)

        if len(sources) > 10:
            source_links.append(f"*...and {len(sources) - 10} more*")

        sources_str = ', '.join(source_links)

        doc.append(f"- **`{keyword}`** ({categories}) — {sources_str}\n")

    return ''.join(doc)

def generate_root_index(docs_path):
    """Generate the root index.md file"""

    doc = []
    doc.append("# React Email - Repository Documentation\n\n")
    doc.append("**Repository:** react-email\n")
    doc.append(f"**Generated:** {datetime.utcnow().isoformat()}Z\n\n")
    doc.append("---\n\n")

    doc.append("## Welcome\n\n")
    doc.append("This is the comprehensive documentation for the react-email repository. ")
    doc.append("Every file has been analyzed and documented with detailed explanations, ")
    doc.append("keyword extraction, and cross-references.\n\n")

    doc.append("## Quick Links\n\n")
    doc.append("- [📖 Comprehensive Book](comprehensive_book.md) - Full documentation book\n")
    doc.append("- [🔍 Global Keywords Index](keywords.md) - A-Z index of all keywords\n")
    doc.append("- [📊 Verification Report](verification_report.md) - Documentation quality report\n")
    doc.append("- [ℹ️ How to Use This Documentation](README.md)\n\n")

    doc.append("---\n\n")

    doc.append("## Repository Structure\n\n")
    doc.append("Browse the documentation by directory:\n\n")

    # Find all folder index files
    folder_indexes = []
    for root, dirs, files in os.walk(docs_path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        if 'doc.md' in files:
            rel_path = os.path.relpath(root, docs_path)
            if rel_path == '.':
                rel_path = ''

            folder_indexes.append(rel_path)

    # Sort and display
    folder_indexes = sorted(folder_indexes)

    for folder_path in folder_indexes:
        if not folder_path:
            # Root
            doc.append("### Root Directory\n\n")
            doc.append("- [📁 Index](index.md)\n")
            doc.append("- [📚 Documentation](doc.md)\n")
            doc.append("- [🔍 Keywords](sub.md)\n\n")
        else:
            # Subdirectory
            depth = folder_path.count(os.sep)
            indent = "  " * depth

            folder_name = os.path.basename(folder_path)
            index_link = os.path.join(folder_path, 'index.md')
            doc_link = os.path.join(folder_path, 'doc.md')

            doc.append(f"{indent}- **{folder_path}/** — [Index]({index_link}) | [Docs]({doc_link})\n")

    doc.append("\n---\n\n")

    doc.append("## Documentation Types\n\n")
    doc.append("Each file in the repository has two types of documentation:\n\n")
    doc.append("1. **`<filename>_docs.md`** - Comprehensive documentation including:\n")
    doc.append("   - Full source code\n")
    doc.append("   - Detailed analysis\n")
    doc.append("   - Function and class documentation\n")
    doc.append("   - Usage examples\n\n")
    doc.append("2. **`<filename>_kw.md`** - Keyword index with:\n")
    doc.append("   - Extracted identifiers\n")
    doc.append("   - Function and class names\n")
    doc.append("   - Type definitions\n")
    doc.append("   - Links to documentation\n\n")

    doc.append("Each folder also has:\n\n")
    doc.append("- **`index.md`** - Directory listing with links to all files\n")
    doc.append("- **`doc.md`** - Narrative overview of the folder's purpose\n")
    doc.append("- **`sub.md`** - Merged keyword index for the folder\n\n")

    return ''.join(doc)

def generate_comprehensive_book(docs_path):
    """Generate the comprehensive book by stitching together all content"""

    doc = []
    doc.append("# React Email - Comprehensive Documentation Book\n\n")
    doc.append("**Repository:** react-email\n")
    doc.append(f"**Generated:** {datetime.utcnow().isoformat()}Z\n\n")
    doc.append("---\n\n")

    doc.append("## Table of Contents\n\n")
    doc.append("This book is organized by folder, with each folder's documentation ")
    doc.append("presented as a chapter.\n\n")

    # Build TOC first
    chapters = []
    for root, dirs, files in os.walk(docs_path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        if 'doc.md' in files:
            rel_path = os.path.relpath(root, docs_path)
            if rel_path == '.':
                rel_path = 'Root'

            chapters.append(rel_path)

    chapters = sorted(chapters, key=lambda x: (x != 'Root', x))

    for i, chapter in enumerate(chapters, 1):
        doc.append(f"{i}. [{chapter}](#{chapter.lower().replace('/', '-').replace(' ', '-')})\n")

    doc.append("\n---\n\n")

    # Generate each chapter
    for i, chapter_path in enumerate(chapters, 1):
        if chapter_path == 'Root':
            folder_path = docs_path
            rel_path = ''
        else:
            folder_path = os.path.join(docs_path, chapter_path)
            rel_path = chapter_path

        doc.append(f"# Chapter {i}: {chapter_path}\n\n")

        # Include the folder's doc.md content
        doc_file = os.path.join(folder_path, 'doc.md')
        if os.path.exists(doc_file):
            try:
                with open(doc_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Remove the title line (first line) to avoid duplication
                lines = content.split('\n')
                if lines:
                    content = '\n'.join(lines[1:])

                doc.append(content)
                doc.append("\n\n")

            except Exception as e:
                doc.append(f"*Error reading chapter content: {e}*\n\n")

        # Add a list of files in this chapter
        doc.append(f"### Files in {chapter_path}\n\n")

        index_file = os.path.join(folder_path, 'index.md')
        if os.path.exists(index_file):
            try:
                with open(index_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract file list from index
                # Look for the Files section
                if '### Files' in content:
                    files_section = content.split('### Files')[1].split('###')[0]
                    doc.append(files_section)
                    doc.append("\n")

            except Exception as e:
                pass

        doc.append("---\n\n")

        if i % 50 == 0:
            print(f"Generated {i}/{len(chapters)} chapters...")

    return ''.join(doc)

def main():
    docs_path = './docs'

    print("Collecting all keywords...")
    all_keywords = collect_all_keywords(docs_path)
    print(f"Found {len(all_keywords):,} unique keywords")

    print("Generating global keywords.md...")
    keywords_content = generate_global_keywords(all_keywords, docs_path)
    keywords_file = os.path.join(docs_path, 'keywords.md')
    with open(keywords_file, 'w', encoding='utf-8') as f:
        f.write(keywords_content)
    print(f"Saved to {keywords_file}")

    print("Generating root index.md...")
    index_content = generate_root_index(docs_path)
    # Note: The folder generator already created index.md, but we want to overwrite with the root one
    index_file = os.path.join(docs_path, 'ROOT_INDEX.md')
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print(f"Saved to {index_file}")

    print("Generating comprehensive_book.md...")
    book_content = generate_comprehensive_book(docs_path)
    book_file = os.path.join(docs_path, 'comprehensive_book.md')
    with open(book_file, 'w', encoding='utf-8') as f:
        f.write(book_content)
    print(f"Saved to {book_file}")

    print("\n=== Global Documentation Complete ===")
    print(f"Keywords: {len(all_keywords):,}")
    print(f"Book size: {len(book_content):,} characters")

if __name__ == '__main__':
    main()
