from pathlib import Path


# # declaring file types
    # png_files = list(downloads_folder.glob("*.png"))
    # jpg_files = list(downloads_folder.glob("*.jpg"))
    # zip_files = list(downloads_folder.glob("*.zip"))
    # mp3_files = list(downloads_folder.glob("*.mp3"))
    # mp4_files = list(downloads_folder.glob("*.mp4"))

class FileSorter:

    def __init__(self):
        self.__base_path = Path.home() / "Downloads"

    def sort_files(self):

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
