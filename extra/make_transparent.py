

texture = 'powder_keg'

src_path = 'C:\\Users\\ErikWengleBINTGmbH\\AppData\\Roaming\\.minecraft\\resourcepacks\\terminacraft-resources\\assets\\minecraft\\textures\\mm\\items\\' + texture + '.png'
dest_path = 'C:\\Users\\ErikWengleBINTGmbH\\AppData\\Roaming\\.minecraft\\resourcepacks\\terminacraft-resources\\assets\\minecraft\\textures\\mm\\items\\' + texture + '_none.png'



# read image and put opacity to 0.4:
from PIL import Image

# Open the image
img = Image.open(src_path).convert("RGBA")  # Ensure the image is in RGBA mode

# Adjust the opacity
alpha = img.getchannel("A")
alpha = alpha.point(lambda p: p * 0.4)  # Reduce opacity to 40%
img.putalpha(alpha)

# Save the new image
img.save(dest_path)
