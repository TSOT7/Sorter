from pathlib import Path
import os
import shutil

class FolderManager:
    def __init__(self):
        self.__base_path = Path.home() / "Downloads"
        self.__folder_types = {
            "img": "Images",
            "zip": "Archives",
            "audio": "Audio",
            "vid": "Video",
            "media" : "Media"
        }

    def get_folder_types(self):
        return self.__folder_types

    def create_folders(self):
        """
        Create folders for the main types of files stored in the downloads folder IF they do not already exist
        """
        folder_path = self.__base_path

        for folder_name in self.__folder_types.values():
            merged_path = folder_path / folder_name
            if not os.path.exists(merged_path):
                os.mkdir(merged_path)
                print(f"Folder {merged_path} created successfully.")
            else:
                print(f"Folder {merged_path} already exists.")

    def get_folder_path(self, folder_name):
        folder_path = self.__base_path / folder_name
        if folder_path.exists():
            return folder_path
        else:
            raise FileNotFoundError(f"Folder '{folder_name}' does not exist.")


class FileSorter:
    def __init__(self):
        self.folder_manager = FolderManager()
        self.__base_path = Path.home() / "Downloads"
        self.__folder_types = self.folder_manager.get_folder_types()

    def sort_files_by_type(self):
        file_types = ["png", "jpg", "gif", "zip", "mp3", "mp4", "7z", "rar", "exe", "epub", "pdf"]
        file_type_to_folder_key = {
            "png": "img",
            "jpg": "img",
            "zip": "zip",
            "7z" : "zip",
            "rar" : "zip",
            "exe" : "zip",
            "mp3": "audio",
            "mp4": "vid",
            "gif" : "vid",
            "epub" : "media",
            "pdf" : "media"
        }

        # Collect files by type
        data_type_references = {}
        for file_type in file_types:
            files = list(self.__base_path.glob(f"*.{file_type}"))
            data_type_references[file_type] = files

        # Iterate over files and move them to the appropriate folder
        for file_type, files in data_type_references.items():
            if not files:
                print(f"No {file_type} files found.")
                continue

            for file in files:
                if file.is_file():
                    folder_key = file_type_to_folder_key.get(file_type)
                    destination_folder = self.__base_path / self.__folder_types[folder_key]

                    shutil.move(str(file), str(destination_folder / file.name))
                    print(f"Moved {file} to {destination_folder}")


