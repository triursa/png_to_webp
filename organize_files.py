import os
import shutil

def clear_png_folder(png_folder):
    # Check if the folder exists
    if not os.path.exists(png_folder):
        print(f"Folder '{png_folder}' does not exist.")
        return

    # Remove all files in the folder
    png_files = [f for f in os.listdir(png_folder) if f.endswith('.png')]
    if not png_files:
        print(f"No PNG files found in '{png_folder}'.")
        return

    for filename in png_files:
        file_path = os.path.join(png_folder, filename)
        os.remove(file_path)
        print(f"Deleted {filename} from {png_folder}")

def move_webp_files(webp_folder, finished_folder):
    # Check if the webp folder exists
    if not os.path.exists(webp_folder):
        print(f"Folder '{webp_folder}' does not exist.")
        return

    # Ensure the finished folder exists
    os.makedirs(finished_folder, exist_ok=True)

    # Move all .webp files to the finished folder
    webp_files = [f for f in os.listdir(webp_folder) if f.endswith('.webp')]
    if not webp_files:
        print(f"No WebP files found in '{webp_folder}'.")
        return

    for filename in webp_files:
        old_path = os.path.join(webp_folder, filename)
        new_path = os.path.join(finished_folder, filename)
        shutil.move(old_path, new_path)
        print(f"Moved {filename} to {finished_folder}")

if __name__ == "__main__":
    png_folder = "png_files"  # Folder containing PNG files
    webp_folder = "webp_files"  # Folder containing WebP files
    finished_folder = "finished_files"  # Destination folder for WebP files

    # Clear PNG files
    clear_png_folder(png_folder)

    # Move WebP files to finished folder
    move_webp_files(webp_folder, finished_folder)