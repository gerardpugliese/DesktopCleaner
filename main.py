'''
~ Desktop Cleaner ~

1. What should this program do?
    This program should automatically sort the files on your Desktop into predetermined folders.
2. How will it achieve this?
    To start, we will create folders for a defined list of file extensions. Then we will loop through the
    files on our desktop and put them into their designated folder.
3. How can we expand on this?
    * Add a GUI 
    * Allow for folders to be sorted as well as files
    * Create custom sorting conditions beyond file extensions

'''
import shutil
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

PATH_TO_DESKTOP = os.getenv("PATH_TO_DESKTOP")

def main():
    print("-----Start of Sorting Script-----")
    # Define list of folders that we'll be sorting into
    folders = ["Images", "Audio", "Docs"]
    img_exts = ["jpg", "png", "jfif"]
    audio_exts = ["mp3", "wav"]
    doc_exts = ["docx"]

    # Loop through and create a file for each extension (if one doesn't exist already)
    for folder in folders:
        folder_to_make = PATH_TO_DESKTOP + folder
        if not os.path.exists(folder_to_make):
            print("Making folder for: ", folder)
            os.makedirs(folder_to_make)
        else:
            print(folder_to_make + " exists!")

    # Loop through files on desktop and put them into their respective folders
    desktop_files = os.listdir(PATH_TO_DESKTOP)
    for file in desktop_files:
        split_file = file.split(".")
        if len(split_file) == 1: # This is a directory not a file
            continue
        else: # Check extension and move to appropriate folder
            extension = split_file[1]
            file_dir = PATH_TO_DESKTOP + file
            if extension in img_exts:
                shutil.move(file_dir, PATH_TO_DESKTOP+folders[0])
            elif extension  in audio_exts:
                shutil.move(file_dir, PATH_TO_DESKTOP+folders[1])
            elif extension in doc_exts:
                shutil.move(file_dir, PATH_TO_DESKTOP+folders[2])
            else:
                print(f"unsupported extension type: {extension}")

if __name__ == "__main__":
    main() 