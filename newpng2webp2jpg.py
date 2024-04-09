from PIL import Image
import os

def convert_images_to_jpeg():
    # Get the directory of the script
    directory = os.path.dirname(__file__)
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a PNG or WEBP image
        if filename.endswith(".png") or filename.endswith(".webp"):
            # Exclude files with the same .jpeg name as the .png name
            if filename[:-4] + ".jpeg" in os.listdir(directory):
                continue

            # Open the image
            image_path = os.path.join(directory, filename)
            with Image.open(image_path) as img:
                # Determine the output JPEG filename
                jpeg_image_path = os.path.join(directory, filename[:-4] + ".jpeg")
                
                # Convert and save the image as JPEG with highest quality (100)
                img.convert("RGB").save(jpeg_image_path, "JPEG", quality=100)
                print(f"Converted {filename} to JPEG with highest quality.")
                continue
                
# Example usage:
convert_images_to_jpeg()
