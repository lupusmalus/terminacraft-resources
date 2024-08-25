import json
from PIL import Image, ImageEnhance
import os

# Load JSON data
json_template = {
    "credit": "Made with Blockbench",
    "texture_size": [256, 256],
    "textures": {
        "1": "entity/chest/animated/big/0",
        "particle": "entity/chest/animated/big/0"
    },
    "elements": [
        {
            "from": [1, 0, 1],
            "to": [15, 8, 15],
            "faces": {
                "north": {"uv": [1.6875, 8.25, 5.59375, 10.75], "texture": "#1"},
                "east": {"uv": [0, 8.25, 1.75, 10.75], "texture": "#1"},
                "south": {"uv": [5.4375, 8.25, 9.15625, 10.75], "texture": "#1"},
                "west": {"uv": [0, 8.25, 1.78125, 10.75], "texture": "#1"},
                "up": {"uv": [1.75, 4.78125, 5.46875, 8.25], "texture": "#1"},
                "down": {"uv": [5.53125, 4.78125, 9.21875, 8.28125], "texture": "#1"}
            }
        },
        {
            "from": [1, 8, 1],
            "to": [15, 13, 15],
            "rotation": {"angle": 0, "axis": "x", "origin": [1, 8, 15]},
            "faces": {
                "north": {"uv": [1.6875, 3.5, 5.59375, 4.75], "texture": "#1"},
                "east": {"uv": [9.125, 3.5, 11, 4.71875], "texture": "#1"},
                "south": {"uv": [5.4375, 3.5625, 9.15625, 4.8125], "texture": "#1"},
                "west": {"uv": [0, 3.5, 1.78125, 4.75], "texture": "#1"},
                "up": {"uv": [5.4375, 4.8125, 9.25, 8.1875], "texture": "#1"},
                "down": {"uv": [5.53125, 0, 9.21875, 3.5], "texture": "#1"}
            }
        }
    ],
    "display": {
        "head": {
            "translation": [0, -31.25, 0],
            "scale": [1.5, 1.5, 1.5]
        }
    }
}

# Load image
image_path = 'C:\\Users\\wengl\\AppData\\Roaming\\.minecraft\\resourcepacks\\terminacraft\\assets\\minecraft\\textures\\entity\\chest\\animated\\big\\orig.png'  # Replace with your image path
image = Image.open(image_path).convert("RGBA")

# Create output directory
output_dir = 'output_images'
os.makedirs(output_dir, exist_ok=True)

# Process images
for i in range(60):
    # Calculate opacity
    opacity = i / 59  # Scale from 0 to 1

    # Adjust image opacity
    alpha = image.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    img_with_opacity = image.copy()
    img_with_opacity.putalpha(alpha)

    # Save image
    img_save_path = os.path.join(output_dir, f'{i}.png')
    img_with_opacity.save(img_save_path)

    # Update JSON
    json_data = json_template.copy()
    json_data["textures"]["1"] = json_data["textures"]["1"] = "entity/chest/animated/big/" + str(i)

    # Save JSON
    json_save_path = os.path.join(output_dir, f'{i}.json')
    with open(json_save_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

print("Processing complete!")
