


string = '''{
    "parent": "minecraft:item/generated",
    "textures": {
      "layer0": "mm/items/event/ITEM_NAME"
    }
  }'''



item_names = ['express_mail', 'kafei_letter', 'land_td', 'moons_tear', 'mountain_td', 'ocean_td', 'pendant', 'room_key', 'swamp_td']

for item_name in item_names:
    f = open(item_name + '.json', 'w')
    f.write(string.replace('ITEM_NAME', item_name))
    f.close()

