import zipfile
import os

def compress_directory(directory):
    base_name = os.path.basename(directory)
    zip_name = f"{base_name}.zip"

    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory))

    print(f"Compression successful. File saved as {zip_name}.")

def decompress_archive(archive_path):
    with zipfile.ZipFile(archive_path, "r") as zipf:
        zipf.extractall()

    print(f"Decompression successful. Files extracted to current directory.")

# Example usage
compress_directory("/path/to/directory")
decompress_archive("/path/to/archive.zip")
