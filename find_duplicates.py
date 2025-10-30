import os
import hashlib

def compute_hash(file_path):
    """Compute SHA-256 hash of a file."""
    hash_func = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception:
        return None


def collect_files(root_dir):
    """Collect all files (recursively) in a directory."""
    file_list = []
    for root, _, files in os.walk(root_dir):
        for name in files:
            file_list.append(os.path.join(root, name))
    return file_list


def find_duplicates(dir1, dir2=None, output_file="duplicate_files.txt"):
    """Find duplicate files within one or between two directories."""
    print("Scanning directories...")

    # Gather files from one or two directories
    files = collect_files(dir1)
    if dir2:
        files += collect_files(dir2)

    # Compute hashes and track duplicates
    hash_map = {}
    duplicates = []

    for file_path in files:
        file_hash = compute_hash(file_path)
        if not file_hash:
            continue
        if file_hash in hash_map:
            duplicates.append((hash_map[file_hash], file_path))
        else:
            hash_map[file_hash] = file_path

    # Save results
    with open(output_file, "w") as out:
        if duplicates:
            out.write("Duplicate files found:\n\n")
            for original, duplicate in duplicates:
                out.write(f"{original}\n{duplicate}\n\n")
        else:
            out.write("No duplicate files found.\n")

    print(f"Scan complete. Results saved to: {output_file}")


if __name__ == "__main__":
    dir1 = input("Enter the first directory: ").strip()
    dir2 = input("Enter the second directory (press Enter to skip): ").strip() or None
    find_duplicates(dir1, dir2)

