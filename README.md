# Duplicate Finder

A lightweight Python tool to identify duplicate files using SHA-256 hashing.  
It can scan one directory (and all subdirectories) or compare two directories to locate identical files, even when filenames differ.

## Features
- Scans directories recursively
- Compares files by content, not filename
- Supports single or dual directory comparison
- Exports results to a text file (`duplicate_files.txt`)

## Usage
```bash
python find_duplicates.py
