import os
from PIL import Image

# Configure your input and output folders
INPUT_FOLDER = "C:\\Users\\ErikWengleBINTGmbH\\AppData\\Roaming\\.minecraft\\resourcepacks\\terminacraft-resources\\assets\\minecraft\\textures\\mm\\items\\bottle"
OUTPUT_FOLDER = "C:\\Users\\ErikWengleBINTGmbH\\AppData\\Roaming\\.minecraft\\resourcepacks\\terminacraft-resources\\assets\\minecraft\\textures\\mm\\items\\bottle\\scaled"
SIZE = (64, 64)  # Target size

def batch_resize(input_folder, output_folder, size):
    """Resizes all images in a folder to the specified size."""
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create the output folder if it doesn't exist

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # Check valid image types
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                with Image.open(input_path) as img:
                    img = img.resize(size, Image.BILINEAR)  # Linear interpolation
                    img.save(output_path)  # Save in the same format

                print(f"Resized: {filename} → {output_path}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print("✅ Batch resizing complete!")

if __name__ == "__main__":
    batch_resize(INPUT_FOLDER, OUTPUT_FOLDER, SIZE)
