import os
import shutil
"""
Moves all .RW2 and .RAF raw photo files
to there own folder located in the RAW folder
"""
source_folder = "Camera/Sort"
raw_gx80_folder = "Camera/RAW/GX_80"
raw_xpro1_folder = "Camera/RAW/X-pro_1"

# Ensure the target folders exist
os.makedirs(raw_gx80_folder, exist_ok=True)
os.makedirs(raw_xpro1_folder, exist_ok=True)

# Get the list of files in the source folder
files = os.listdir(source_folder)

for file_name in files:
    # Construct the full path of the file
    file_path = os.path.join(source_folder, file_name)

    # Check the file extension
    if file_name.endswith(".RW2"):
        # Move the file to the GX_80 folder
        destination_path = os.path.join(raw_gx80_folder, file_name)
        shutil.move(file_path, destination_path)
        print(f"Moved {file_name} to {raw_gx80_folder}")
    elif file_name.endswith(".RAF"):
        # Move the file to the X-pro_1 folder
        destination_path = os.path.join(raw_xpro1_folder, file_name)
        shutil.move(file_path, destination_path)
        print(f"Moved {file_name} to {raw_xpro1_folder}")
    else:
        print(f"Skipped {file_name} (unsupported file extension)")

print("Sorting complete.")
