import os
import uuid

def rename_webp_files(folder):
    # Check if the folder exists
    if not os.path.exists(folder):
        print(f"Folder '{folder}' does not exist.")
        return

    # Get all .webp files in the folder
    webp_files = [f for f in os.listdir(folder) if f.endswith('.webp')]
    if not webp_files:
        print(f"No WebP files found in '{folder}'.")
        return

    for filename in webp_files:
        # Generate a new name with a random identifier
        new_name = f"TriBoi_AI_{uuid.uuid4().hex[:8]}.webp"
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed {filename} to {new_name}")

if __name__ == "__main__":
    folder = "webp_files"  # Update this to the folder containing your WebP files
    rename_webp_files(folder)