import os

folder_path = "Flags"  # Replace with the path to your folder

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):  # Filter only image files
        new_filename = filename.capitalize()  # Capitalize the filename
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)  # Rename the file

