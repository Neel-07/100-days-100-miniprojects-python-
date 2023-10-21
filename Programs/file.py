import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split(".")[-1]
            destination_folder = get_destination_folder(file_extension)
            if destination_folder:
                destination_path = os.path.join(folder_path, destination_folder)
                if not os.path.exists(destination_path):
                    os.mkdir(destination_path)
                shutil.move(file_path, os.path.join(destination_path, filename))

def get_destination_folder(file_extension):
    extensions = {
        'pdf': 'Documents',
        'docx': 'Documents',
        'jpg': 'Images',
        'mp4': 'Videos',
        # Add more file extensions and folders as needed
    }
    return extensions.get(file_extension, 'Other')

if __name__ == "__main__":
    folder_to_organize = "path/to/your/folder"
    organize_files(folder_to_organize)
