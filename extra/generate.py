


string = '''{
    "parent": "minecraft:item/generated",
    "textures": {
      "layer0": "mm/items/ITEM_NAME"
    }
  }'''




    # { "predicate": { "custom_model_data": 8000017}, "model": "mm/items/bomb_none"},
    # { "predicate": { "custom_model_data": 8000018}, "model": "mm/items/bombchu_none"},
    # { "predicate": { "custom_model_data": 8000019}, "model": "mm/items/deku_stick_none"},
    # { "predicate": { "custom_model_data": 8000020}, "model": "mm/items/deku_nut_none"},
    # { "predicate": { "custom_model_data": 8000021}, "model": "mm/items/magic_beans_none"},
    # { "predicate": { "custom_model_data": 8000022}, "model": "mm/items/powder_keg_none"},


item_names = ['bomb_none', 'deku_nut_none', 'powder_keg_none', 'deku_stick_none', 'magic_beans_none', 'bombchu_none']ls

for item_name in item_names:
    f = open(item_name + '.json', 'w')
    f.write(string.replace('ITEM_NAME', item_name))
    f.close()

