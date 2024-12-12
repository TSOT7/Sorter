from pathlib import Path
import os

# Define the Downloads folder path


# img_path = r"C:\Users\tommy\Downloads\Imgs"
# zip_path = r"C:\Users\tommy\Downloads\Zips"
# img_path = r"C:\Users\tommy\Downloads\Imgs"
# img_path = r"C:\Users\tommy\Downloads\Imgs"

# Creates Imgs Folder
# if not os.path.exists(img_path):
#     os.mkdir(img_path)
#     print(f"Folder '{img_path}' created successfully.")
# else:
#     print(f"Folder '{img_path}' already exists.")
class FolderManager:
    def __init__(self, base_path):
        self.__base_path = Path.home() / "Downloads"
        self.__folder_types = ["Images", "Zips", "Audio", "Video"]

    def create_folders(self): 
        """
        Create folders for the main types of files stored in the downloads folder IF they do not already exist
        """
        folder_path = self.__base_path
        folder_dict = {}

        for type in self.folder_types:
            merged_path = folder_path + type
            if not os.path.exists(folder_path + type):
                os.mkdir(merged_path)
                print(f"Folder {merged_path} created succesfully.")
            else:
                print(f"Folder {merged_path} already exists.")
        

    



