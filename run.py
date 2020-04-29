import os
import sys
import shutil
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import subprocess

root = tk.Tk()
root.withdraw()


def singleUpload():
    file_path = filedialog.askopenfilename()
    im = Image.open(file_path)
    width, height = im.size
    if width / height != 0.5625:
        print(
            "Warning: The image you're uploading is not 16:9 (1920x1080 / 1600x900 / 1280x720).\nThis could cause image cliping in Microsoft Teams.")

        def rerunImage():
            imagewarningInput = input("Are you sure you want to continue? y/n: ")
            if imagewarningInput.lower() == "y":
                pass
            elif imagewarningInput.lower() == "n":
                main()
            else:
                print("Error: Invalid input")
                rerunImage()

        rerunImage()

    dir_path = f"{os.getenv('APPDATA')}\\Microsoft\\Teams\\Backgrounds\\Uploads"
    isdir = os.path.isdir(dir_path)
    if not isdir:
        print(
            "Error: Couldn't find the the Microsoft Teams directory. Please specify the folder in appdata, roaming, microsoft, teams, backgrounds, uploads")
        dir_path = filedialog.askdirectory()

    shutil.copy(file_path, dir_path)
    print("Copied:", im.filename)
    input("Press enter to continue")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    main()


def folderUpload():
    print("Warning: This method will copy ALL files and folders from the selected directory.")

    def rerunImage():
        imagewarningInput = input("Are you sure you want to continue? y/n: ")
        if imagewarningInput.lower() == "y":
            pass
        elif imagewarningInput.lower() == "n":
            main()
        else:
            print("Error: Invalid input")
            rerunImage()

    file_path = filedialog.askdirectory()

    dir_path = f"{os.getenv('APPDATA')}\\Microsoft\\Teams\\Backgrounds\\Uploads"
    isdir = os.path.isdir(dir_path)
    if not isdir:
        print(
            "Error: Couldn't find the the Microsoft Teams directory. Please specify the folder in appdata, roaming, microsoft, teams, backgrounds, uploads")
        dir_path = filedialog.askdirectory()

    files = os.listdir(file_path)
    for f in files:
        impath = f"{file_path}/{f}"
        shutil.copy(impath, dir_path)
    print("Copied:", im.filename)
    input("Press enter to continue")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    main()


def openFolder():
    dir_path = f"{os.getenv('APPDATA')}\\Microsoft\\Teams\\Backgrounds\\Uploads"
    isdir = os.path.isdir(dir_path)
    if not isdir:
        print(
            "Error: Couldn't find the the Microsoft Teams directory. Please specify the folder in appdata, roaming, microsoft, teams, backgrounds, uploads")
        dir_path = filedialog.askdirectory()

    subproDir = f'explorer /select,"{dir_path}"'

    subprocess.Popen(subproDir)


def main():
    print("a) Single image uploader\nb) Folder uploader\nc) View folder")

    def rerun():
        rerunInput = input("Selection: ")
        if rerunInput.lower() == "a":
            singleUpload()
        elif rerunInput.lower() == "b":
            folderUpload()
        elif rerunInput.lower() == "c":
            openFolder()
        else:
            rerun()

    rerun()


main()
