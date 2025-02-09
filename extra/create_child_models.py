import os
import json
from xml.etree.ElementTree import QName


texture_dir = 'C:/Users/wengl/AppData/Roaming/.minecraft/resourcepacks/terminacraft/assets/minecraft/textures/mm/gui/action'
model_dir = 'C:/Users/wengl/AppData/Roaming/.minecraft/resourcepacks/terminacraft/assets/minecraft/models/mm/gui/action'

parent = 'mm/gui/action/action_base'

# FIXME: this could be done better using the discrete path
texture_path = 'mm/gui/action/'
textures = os.listdir(texture_dir)

for file in textures:
    dictionary = {"parent": parent, "textures": {		"0": texture_path + file.replace('.png',''),
		"particle": texture_path + file.replace('.png','')}} 

    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    # Writing to sample.json
    with open(model_dir  + '/' + file.replace('png', 'json'), "w") as outfile:
        outfile.write(json_object)