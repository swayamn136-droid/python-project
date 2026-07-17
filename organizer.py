import os
import shutil
from config import FILE_TYPES
from utils import create_folder


def organize_files(folder_path):
    files = os.listdir(folder_path)

    for file in files:
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            extension = os.path.splitext(file)[1].lower()
            moved = False

            for folder_name, extensions in FILE_TYPES.items():
                if extension in extensions:
                    destination = os.path.join(folder_path, folder_name)
                    create_folder(destination)
                    shutil.move(full_path, os.path.join(destination, file))
                    print(file + " moved to " + folder_name)
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                create_folder(other_folder)
                shutil.move(full_path, os.path.join(other_folder, file))
                print(file + " moved to Others")
