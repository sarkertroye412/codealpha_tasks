import os
import shutil

script_folder = os.path.dirname(os.path.abspath(__file__))
project_folder = os.path.dirname(script_folder)
source_folder = os.path.join(script_folder, "images")
destination_folder = os.path.join(project_folder, "jpg_files")

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

moved_files = 0

for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")
        moved_files += 1
        
print("\n================================")
print("       AUTOMATION COMPLETE")
print("================================")

print(f"Total JPG files moved: {moved_files}")
print(f"Files are now in: {destination_folder}")