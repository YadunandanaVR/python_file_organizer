import os
import shutil

# Define file type categories and corresponding folders
file_categories = {
    'Images': ['jpg', 'png', 'jpeg', 'gif'],
    'Videos': ['mp4', 'avi', 'mkv', 'webm'],
    'Audios': ['mp3', 'wav'],
    'Documents': ['pdf', 'docx', 'txt'],
    'Zips': ['zip'],
    'Applications': ['exe']
}

# Get the directory where the script is executed
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create category folders if they don't exist
for folder in file_categories.keys():
    folder_path = os.path.join(script_dir, folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

# Organize files into corresponding folders
for folder, sub_folders, files in os.walk(script_dir):
    # Skip the folders we created to avoid moving them
    if os.path.basename(folder) in file_categories.keys():
        continue

    for file in files:
        file_path = os.path.join(folder, file)
        extension = file.split('.')[-1].lower()

        for category, extensions in file_categories.items():
            if extension in extensions:
                target_folder = os.path.join(script_dir, category)
                shutil.move(file_path, os.path.join(target_folder, file))
                break  # Move to next file after finding the category
