from pathlib import Path
import os
import shutil

class FolderManager:
    def __init__(self):
        self.__base_path = Path.home() / "Downloads"
        self.__folder_types = ["Images", "Zips", "Audio", "Video"]

    def create_folders(self): 
        """
        Create folders for the main types of files stored in the downloads folder IF they do not already exist
        """
        folder_path = self.__base_path
        folder_dict = {}

        for type in self.___folder_types:
            merged_path = folder_path + type
            if not os.path.exists(merged_path):
                os.mkdir(merged_path)
                print(f"Folder {merged_path} created succesfully.")
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
        self.__base_path = Path.home() / "Downloads"

    
    def list_sorted_files(self):
        file_types = ["png", "jpg", "zip", "mp3", "mp4"]

        data_type_references = {}
        folder_path = self.__base_path
        for type in file_types:
            temp = list(folder_path.glob(f"*.{type}"))
            if type in data_type_references:
                data_type_references[type] = temp
            else:
                data_type_references[type] = list(folder_path.glob(f"*.{type}"))

        for file_types, files in data_type_references.items():
            print(f"\n{file_types.upper()} FILES:")
            if files:
                for file in files:
                    print(file)
            else:
                print("  No files found.")

        for file_types, files in data_type_references.items():
            destination_path = self.__base_path / file


