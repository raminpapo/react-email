#!/usr/bin/env python3
"""
Per-File Documentation Generator
Generates comprehensive _docs.md and _kw.md for each file.
"""

import os
import json
import re
import hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Common programming keywords to filter out
COMMON_KEYWORDS = {
    'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
    'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'be',
    'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
    'would', 'should', 'could', 'may', 'might', 'can', 'this', 'that',
    'var', 'let', 'const', 'if', 'else', 'for', 'while', 'return',
    'function', 'class', 'import', 'export', 'default', 'new', 'null',
    'undefined', 'true', 'false', 'not', 'none', 'self', 'def', 'try',
    'catch', 'finally', 'throw', 'async', 'await', 'yield', 'break',
    'continue', 'switch', 'case', 'typeof', 'instanceof'
}

def extract_keywords(content, file_path):
    """Extract meaningful keywords from file content"""
    keywords = defaultdict(list)

    # Get file extension for context
    ext = os.path.splitext(file_path)[1].lower()

    # Extract identifiers (camelCase, PascalCase, snake_case, CONSTANT_CASE)
    identifiers = re.findall(r'\b[A-Z][a-zA-Z0-9]*\b|\b[a-z][a-zA-Z0-9]*\b|\b[a-z_][a-z0-9_]+\b|\b[A-Z_][A-Z0-9_]+\b', content)

    # Extract import/require statements
    imports = re.findall(r'(?:from|import|require)\s+["\']([^"\']+)["\']', content)

    # Extract function names
    if ext in ['.js', '.jsx', '.ts', '.tsx']:
        functions = re.findall(r'(?:function|const|let|var)\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\s*[=\(]', content)
        classes = re.findall(r'class\s+([A-Z][a-zA-Z0-9]*)', content)
        interfaces = re.findall(r'interface\s+([A-Z][a-zA-Z0-9]*)', content)
        types = re.findall(r'type\s+([A-Z][a-zA-Z0-9]*)', content)

        for func in functions:
            if func.lower() not in COMMON_KEYWORDS:
                keywords['function'].append(func)

        for cls in classes:
            keywords['class'].append(cls)

        for iface in interfaces:
            keywords['interface'].append(iface)

        for typ in types:
            keywords['type'].append(typ)

    elif ext in ['.py']:
        functions = re.findall(r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)', content)
        classes = re.findall(r'class\s+([A-Z][a-zA-Z0-9_]*)', content)

        for func in functions:
            if func.lower() not in COMMON_KEYWORDS:
                keywords['function'].append(func)

        for cls in classes:
            keywords['class'].append(cls)

    # Filter and deduplicate
    unique_identifiers = set()
    for ident in identifiers:
        if (len(ident) >= 3 and
            ident.lower() not in COMMON_KEYWORDS and
            not ident.isdigit() and
            not re.match(r'^[A-Z]+$', ident)):  # Skip all caps like HTML, CSS
            unique_identifiers.add(ident)

    for ident in sorted(unique_identifiers):
        keywords['identifier'].append(ident)

    for imp in imports:
        keywords['import'].append(imp)

    return keywords

def generate_file_docs(file_path, content, rel_path):
    """Generate comprehensive documentation for a single file"""

    file_name = os.path.basename(file_path)
    file_ext = os.path.splitext(file_name)[1]
    file_size = len(content)
    line_count = content.count('\n') + 1

    # Determine file type/language
    lang_map = {
        '.js': 'javascript', '.jsx': 'jsx', '.ts': 'typescript', '.tsx': 'tsx',
        '.py': 'python', '.json': 'json', '.md': 'markdown', '.yaml': 'yaml',
        '.yml': 'yaml', '.css': 'css', '.scss': 'scss', '.html': 'html',
        '.sh': 'bash', '.xml': 'xml', '.toml': 'toml', '.ini': 'ini',
        '.c': 'c', '.cpp': 'cpp', '.h': 'c', '.hpp': 'cpp',
        '.java': 'java', '.go': 'go', '.rs': 'rust', '.rb': 'ruby',
        '.php': 'php', '.swift': 'swift', '.kt': 'kotlin'
    }
    language = lang_map.get(file_ext, '')

    # Extract keywords
    keywords = extract_keywords(content, file_path)

    # Build documentation
    doc = []
    doc.append(f"# Documentation: {file_name}\n")
    doc.append(f"**File Path:** `{rel_path}`\n")
    doc.append(f"**Language:** {language if language else 'Unknown'}\n")
    doc.append(f"**Size:** {file_size:,} bytes\n")
    doc.append(f"**Lines:** {line_count:,}\n")
    doc.append(f"**Generated:** {datetime.utcnow().isoformat()}Z\n")
    doc.append("\n---\n\n")

    # Table of Contents
    doc.append("## Table of Contents\n\n")
    doc.append("1. [File Metadata](#file-metadata)\n")
    doc.append("2. [Original Source](#original-source)\n")
    doc.append("3. [Overview](#overview)\n")
    doc.append("4. [Detailed Analysis](#detailed-analysis)\n")
    doc.append("5. [Keywords & Identifiers](#keywords--identifiers)\n")
    doc.append("6. [Related Files](#related-files)\n")
    doc.append("\n---\n\n")

    # File Metadata
    doc.append("## File Metadata\n\n")
    doc.append(f"- **Path:** `{rel_path}`\n")
    doc.append(f"- **Name:** `{file_name}`\n")
    doc.append(f"- **Extension:** `{file_ext}`\n")
    doc.append(f"- **Language:** {language if language else 'Unknown'}\n")
    doc.append(f"- **Size:** {file_size:,} bytes ({file_size / 1024:.2f} KB)\n")
    doc.append(f"- **Lines of Code:** {line_count:,}\n")
    doc.append("\n---\n\n")

    # Original Source
    doc.append("## Original Source\n\n")
    if file_size > 500000:  # 500KB
        doc.append(f"*Note: File is large ({file_size / 1024:.2f} KB). Showing first 10,000 lines.*\n\n")
        lines = content.split('\n')[:10000]
        content_display = '\n'.join(lines)
    else:
        content_display = content

    doc.append(f"```{language}\n")
    doc.append(content_display)
    doc.append("\n```\n\n")
    doc.append("---\n\n")

    # Overview
    doc.append("## Overview\n\n")

    # Basic analysis based on file type
    if file_ext in ['.js', '.jsx', '.ts', '.tsx']:
        doc.append("This is a JavaScript/TypeScript file. ")

        if 'react' in content.lower() or 'jsx' in file_ext.lower():
            doc.append("It appears to be a React component or React-related module. ")

        if 'export default' in content:
            doc.append("It exports a default export. ")

        if 'export {' in content or 'export const' in content or 'export function' in content:
            doc.append("It contains named exports. ")

    elif file_ext == '.py':
        doc.append("This is a Python file. ")

        if 'class ' in content:
            doc.append("It defines one or more classes. ")

        if 'def ' in content:
            doc.append("It contains function definitions. ")

    elif file_ext == '.json':
        doc.append("This is a JSON configuration or data file. ")

    elif file_ext == '.md':
        doc.append("This is a Markdown documentation file. ")

    elif file_ext in ['.yaml', '.yml']:
        doc.append("This is a YAML configuration file. ")

    doc.append("\n\n")
    doc.append("---\n\n")

    # Detailed Analysis
    doc.append("## Detailed Analysis\n\n")

    # Functions
    if keywords.get('function'):
        doc.append("### Functions\n\n")
        doc.append("The following functions are defined in this file:\n\n")
        for func in sorted(set(keywords['function']))[:100]:  # Limit to 100
            doc.append(f"- `{func}()`\n")
        doc.append("\n")

    # Classes
    if keywords.get('class'):
        doc.append("### Classes\n\n")
        doc.append("The following classes are defined:\n\n")
        for cls in sorted(set(keywords['class']))[:50]:
            doc.append(f"- `{cls}`\n")
        doc.append("\n")

    # Interfaces/Types (TypeScript)
    if keywords.get('interface'):
        doc.append("### Interfaces\n\n")
        for iface in sorted(set(keywords['interface']))[:50]:
            doc.append(f"- `{iface}`\n")
        doc.append("\n")

    if keywords.get('type'):
        doc.append("### Type Definitions\n\n")
        for typ in sorted(set(keywords['type']))[:50]:
            doc.append(f"- `{typ}`\n")
        doc.append("\n")

    # Imports
    if keywords.get('import'):
        doc.append("### Dependencies\n\n")
        doc.append("This file imports/requires:\n\n")
        for imp in sorted(set(keywords['import']))[:100]:
            doc.append(f"- `{imp}`\n")
        doc.append("\n")

    doc.append("---\n\n")

    # Keywords & Identifiers
    doc.append("## Keywords & Identifiers\n\n")
    if keywords.get('identifier'):
        unique_idents = sorted(set(keywords['identifier']))[:200]  # Top 200
        doc.append(f"**Total Unique Identifiers:** {len(unique_idents)}\n\n")
        for ident in unique_idents:
            doc.append(f"- `{ident}`\n")
    else:
        doc.append("*No significant identifiers extracted.*\n")

    doc.append("\n---\n\n")

    # Related Files
    doc.append("## Related Files\n\n")
    doc.append("*Related files analysis would require cross-referencing imports and exports across the codebase.*\n\n")

    return ''.join(doc)

def generate_file_keywords(file_path, keywords, rel_path):
    """Generate keyword index file for a single file"""

    file_name = os.path.basename(file_path)

    kw_doc = []
    kw_doc.append(f"# Keywords: {file_name}\n\n")
    kw_doc.append(f"**Source File:** `{rel_path}`\n")
    kw_doc.append(f"**Generated:** {datetime.utcnow().isoformat()}Z\n\n")
    kw_doc.append("---\n\n")

    # Build A-Z index
    all_keywords = []

    for category, items in keywords.items():
        for item in items:
            all_keywords.append((item, category))

    # Sort and group by first letter
    all_keywords = sorted(set(all_keywords), key=lambda x: x[0].lower())

    current_letter = None
    for keyword, category in all_keywords:
        first_letter = keyword[0].upper()

        if first_letter != current_letter:
            if current_letter is not None:
                kw_doc.append("\n")
            kw_doc.append(f"## {first_letter}\n\n")
            current_letter = first_letter

        # Link to docs file
        docs_link = f"{os.path.splitext(file_name)[0]}_docs.md"
        kw_doc.append(f"- **`{keyword}`** ({category}) - [View in docs]({docs_link})\n")

    if not all_keywords:
        kw_doc.append("*No keywords extracted from this file.*\n")

    return ''.join(kw_doc)

def process_file(file_info, repo_path, docs_path, progress_log):
    """Process a single file and generate documentation"""

    file_path = file_info['absolute_path']
    rel_path = file_info['path']

    try:
        # Read file content
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Generate docs
        docs_content = generate_file_docs(file_path, content, rel_path)

        # Extract keywords
        keywords = extract_keywords(content, file_path)

        # Generate keyword doc
        kw_content = generate_file_keywords(file_path, keywords, rel_path)

        # Create output directory structure
        file_dir = os.path.dirname(rel_path)
        docs_dir = os.path.join(docs_path, file_dir) if file_dir else docs_path
        os.makedirs(docs_dir, exist_ok=True)

        # Write documentation files
        file_base = os.path.basename(file_path)
        docs_file = os.path.join(docs_dir, f"{file_base}_docs.md")
        kw_file = os.path.join(docs_dir, f"{file_base}_kw.md")

        with open(docs_file, 'w', encoding='utf-8') as f:
            f.write(docs_content)

        with open(kw_file, 'w', encoding='utf-8') as f:
            f.write(kw_content)

        # Log progress
        progress_entry = {
            'file': rel_path,
            'docs_file': docs_file,
            'kw_file': kw_file,
            'size': file_info['size'],
            'status': 'success',
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        }
        progress_log.append(progress_entry)

        return True, len(docs_content) + len(kw_content)

    except Exception as e:
        progress_entry = {
            'file': rel_path,
            'status': 'error',
            'error': str(e),
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        }
        progress_log.append(progress_entry)
        return False, 0

def process_binary_file(file_info, repo_path, docs_path, progress_log):
    """Generate minimal documentation for binary files"""

    file_path = file_info['absolute_path']
    rel_path = file_info['path']

    try:
        file_name = os.path.basename(file_path)
        file_ext = os.path.splitext(file_name)[1]
        file_size = file_info['size']

        # Simple binary file documentation
        doc = []
        doc.append(f"# Binary File: {file_name}\n\n")
        doc.append(f"**Path:** `{rel_path}`\n")
        doc.append(f"**Type:** Binary\n")
        doc.append(f"**Extension:** `{file_ext}`\n")
        doc.append(f"**Size:** {file_size:,} bytes ({file_size / 1024:.2f} KB)\n")
        doc.append(f"**Generated:** {datetime.utcnow().isoformat()}Z\n\n")
        doc.append("---\n\n")
        doc.append("## Description\n\n")

        # Determine file type
        if file_ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico']:
            doc.append("This is an image file.\n")
        elif file_ext in ['.woff', '.woff2', '.ttf', '.eot', '.otf']:
            doc.append("This is a font file.\n")
        elif file_ext in ['.pdf']:
            doc.append("This is a PDF document.\n")
        elif file_ext in ['.zip', '.tar', '.gz', '.bz2']:
            doc.append("This is a compressed archive.\n")
        else:
            doc.append("This is a binary file.\n")

        doc.append("\n*Binary files are not analyzed for code content.*\n")

        # Create output directory
        file_dir = os.path.dirname(rel_path)
        docs_dir = os.path.join(docs_path, file_dir) if file_dir else docs_path
        os.makedirs(docs_dir, exist_ok=True)

        # Write documentation file
        docs_file = os.path.join(docs_dir, f"{file_name}_docs.md")

        with open(docs_file, 'w', encoding='utf-8') as f:
            f.write(''.join(doc))

        progress_entry = {
            'file': rel_path,
            'docs_file': docs_file,
            'type': 'binary',
            'size': file_size,
            'status': 'success',
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        }
        progress_log.append(progress_entry)

        return True, len(''.join(doc))

    except Exception as e:
        progress_entry = {
            'file': rel_path,
            'status': 'error',
            'error': str(e),
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        }
        progress_log.append(progress_entry)
        return False, 0

def main():
    repo_path = '.'
    docs_path = './docs'

    # Load manifest
    manifest_path = os.path.join(docs_path, 'manifest.json')
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)

    print(f"Processing {manifest['file_counts']['text']} text files...")
    print(f"Processing {manifest['file_counts']['binary']} binary files...")

    progress_log = []
    total_bytes_written = 0
    files_processed = 0
    files_errored = 0

    # Process text files
    for i, file_info in enumerate(manifest['file_inventory']['text'], 1):
        success, bytes_written = process_file(file_info, repo_path, docs_path, progress_log)
        if success:
            files_processed += 1
            total_bytes_written += bytes_written
        else:
            files_errored += 1

        if i % 50 == 0:
            print(f"Processed {i}/{manifest['file_counts']['text']} text files...")

    print(f"Completed text files: {files_processed}/{manifest['file_counts']['text']}")

    # Process binary files
    for i, file_info in enumerate(manifest['file_inventory']['binary'], 1):
        success, bytes_written = process_binary_file(file_info, repo_path, docs_path, progress_log)
        if success:
            files_processed += 1
            total_bytes_written += bytes_written
        else:
            files_errored += 1

        if i % 50 == 0:
            print(f"Processed {i}/{manifest['file_counts']['binary']} binary files...")

    print(f"Completed binary files")

    # Update manifest
    manifest['docs_generation'] = {
        'files_processed': files_processed,
        'files_errored': files_errored,
        'bytes_written': total_bytes_written,
        'generation_timestamp': datetime.utcnow().isoformat() + 'Z'
    }

    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    # Save progress log
    progress_path = os.path.join(docs_path, '.progress.log')
    with open(progress_path, 'w', encoding='utf-8') as f:
        json.dump(progress_log, f, indent=2, ensure_ascii=False)

    print(f"\n=== Generation Complete ===")
    print(f"Files processed: {files_processed}")
    print(f"Files errored: {files_errored}")
    print(f"Bytes written: {total_bytes_written:,} ({total_bytes_written / (1024*1024):.2f} MB)")
    print(f"Progress log saved to: {progress_path}")

if __name__ == '__main__':
    main()
