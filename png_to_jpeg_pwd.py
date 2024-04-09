from PIL import Image
import os

def convert_png_to_jpeg():
    # Get the directory of the script
    directory = os.path.dirname(__file__)
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a PNG image
        if filename.endswith(".png"):
            # Open the PNG image
            png_image_path = os.path.join(directory, filename)
            with Image.open(png_image_path) as img:
                # Create the output JPEG filename by replacing .png with .jpeg
                jpeg_image_path = os.path.join(directory, filename.replace(".png", ".jpeg"))
                # Convert and save the image as JPEG with highest quality (100)
                img.convert("RGB").save(jpeg_image_path, "JPEG", quality=100)
                print(f"Converted {filename} to JPEG with highest quality.")

# Example usage:
convert_png_to_jpeg()
