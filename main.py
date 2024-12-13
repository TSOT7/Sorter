from folder_manager import FileSorter

if __name__ == "__main__":
    file_sorter = FileSorter()
    file_sorter.folder_manager.create_folders()
    file_sorter.sort_files_by_type()
