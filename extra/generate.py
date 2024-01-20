


string = '''{
    "parent": "minecraft:item/generated",
    "textures": {
      "layer0": "mm/items/event/ITEM_NAME"
    }
  }'''


    # { "predicate": { "custom_model_data": 3000100}, "model": "mm/items/event/express_mail"},
    # { "predicate": { "custom_model_data": 3000101}, "model": "mm/items/event/kafei_letter"},
    # { "predicate": { "custom_model_data": 3000102}, "model": "mm/items/event/land_td"},
    # { "predicate": { "custom_model_data": 3000103}, "model": "mm/items/event/moons_tear"},
    # { "predicate": { "custom_model_data": 3000104}, "model": "mm/items/event/mountain_td"},
    # { "predicate": { "custom_model_data": 3000105}, "model": "mm/items/event/ocean_td"},
    # { "predicate": { "custom_model_data": 3000106}, "model": "mm/items/event/pendant"},
    # { "predicate": { "custom_model_data": 3000107}, "model": "mm/items/event/room_key"},
    # { "predicate": { "custom_model_data": 3000108}, "model": "mm/items/event/swamp_td"},


item_names = ['express_mail', 'kafei_letter', 'land_td', 'moons_tear', 'mountain_td', 'ocean_td', 'pendant', 'room_key', 'swamp_td']

for item_name in item_names:
    f = open(item_name + '.json', 'w')
    f.write(string.replace('ITEM_NAME', item_name))
    f.close()

