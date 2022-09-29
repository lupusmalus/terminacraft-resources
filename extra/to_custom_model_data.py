import os


img_dir = 'C:/Users/wengl/AppData/Roaming/.minecraft/resourcepacks/terminacraft/assets/minecraft/textures/mm/gui/action'
files = [filename for filename in os.listdir(img_dir) if 'png' in filename]
custom_model_base = 1000004
base_dir = 'mm/gui/action/'

for i, file in enumerate(files):
    print(f'{{ "predicate": {{ "custom_model_data": {custom_model_base + i}}}, "model": "{base_dir + file.replace(".png", "")}"}},')