import os
import shutil
from datetime import datetime

path = r"C:/Users/Pratibha Rai/Desktop/imp docs/"

folder_names = ['docs files', 'image files', 'video files', 'excel files', 'audio files', 'pdf files', 'csv files']

file_name = os.listdir(path)
files_moved = []  # store moved files for logging

# Create folders if they don't exist
for folder in folder_names:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files based on extension
for file in file_name:
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        if file.endswith(".docx") and not os.path.exists(path + "docs files/" + file):
            shutil.move(file_path, path + "docs files/" + file)
            files_moved.append(file)
        elif (file.endswith(".jpg") or file.endswith('.png')) and not os.path.exists(path + "image files/" + file):
            shutil.move(file_path, path + "image files/" + file)
            files_moved.append(file)
        elif file.endswith(".mp4") and not os.path.exists(path + "video files/" + file):
            shutil.move(file_path, path + "video files/" + file)
            files_moved.append(file)
        elif file.endswith(".xlsx") and not os.path.exists(path + "excel files/" + file):
            shutil.move(file_path, path + "excel files/" + file)
            files_moved.append(file)
        elif file.endswith(".mp3") and not os.path.exists(path + "audio files/" + file):
            shutil.move(file_path, path + "audio files/" + file)
            files_moved.append(file)
        elif file.endswith(".pdf") and not os.path.exists(path + "pdf files/" + file):
            shutil.move(file_path, path + "pdf files/" + file)
            files_moved.append(file)
        elif file.endswith(".csv") and not os.path.exists(path + "csv files/" + file):
            shutil.move(file_path, path + "csv files/" + file)
            files_moved.append(file)

# Log only if files were moved
if files_moved:
    with open(os.path.join(path, "sorter_log.txt"), "a") as log_file:
        log_file.write(f"\n[{datetime.now()}] Moved {len(files_moved)} file(s):\n")
        for moved_file in files_moved:
            log_file.write(f" - {moved_file}\n")















