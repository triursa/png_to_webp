from PIL import Image
import os
import shutil
from datetime import datetime

def convert_png_to_webp(input_folder, output_folder):
    # Ensure output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input directory
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            # Construct the full file path
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")

            # Open the PNG file
            with Image.open(input_path) as img:
                # Convert to WebP and save
                img.save(output_path, 'webp')
                print(f"Converted {filename} to {os.path.basename(output_path)}")

def move_converted_files(input_folder):
    # Get the current time for the new folder name
    timestamp = datetime.now().strftime("%m-%d-%H%M%S")
    converted_folder = f"converted_images_{timestamp}"
    os.makedirs(converted_folder, exist_ok=True)

    # Move the original PNG files to the new folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            shutil.move(os.path.join(input_folder, filename), os.path.join(converted_folder, filename))
            print(f"Moved {filename} to {converted_folder}")

if __name__ == "__main__":
    input_folder = "png_files"
    output_folder = "webp_files"

    # Convert PNG files to WebP
    convert_png_to_webp(input_folder, output_folder)

    # Move original PNG files to the new folder
    move_converted_files(input_folder)
