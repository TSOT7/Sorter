from pathlib import Path
import os

# Define the Downloads folder path
downloads_folder = Path.home() / "Downloads"

img_path = r"C:\Users\tommy\Downloads\Imgs"

# Creates Imgs Folder
if not os.path.exists(img_path):
    os.mkdir(img_path)
    print(f"Folder '{img_path}' created successfully.")
else:
    print(f"Folder '{img_path}' already exists.")

# # declaring file types
# png_files = list(downloads_folder.glob("*.png"))
# jpg_files = list(downloads_folder.glob("*.jpg"))
# zip_files = list(downloads_folder.glob("*.zip"))
# mp3_files = list(downloads_folder.glob("*.mp3"))
# mp4_files = list(downloads_folder.glob("*.mp4"))

file_types = ["png", "jpg", "zip", "mp3", "mp4"]

data_type_references = {}

for type in file_types:
    data_type_references[f"{type}_files"] = list(downloads_folder.glob(f"*.{type}"))

for types in data_type_references:
    print(types)
    
