from PIL import Image, ImageEnhance

def decrease_transparency(image, factor):
    # Split the image into RGBA channels
    r, g, b, a = image.split()

    # Adjust the transparency (alpha channel) using ImageEnhance
    enhancer = ImageEnhance.Brightness(a)
    a = enhancer.enhance(factor)

    # Merge the channels back into an RGBA image
    result_image = Image.merge('RGBA', (r, g, b, a))

    return result_image

def main():
    # Open the original image
    original_image_path = 'heartpiece_three.png'  # Use an image with an alpha channel (PNG format)
    original_image = Image.open(original_image_path).convert('RGBA')

    # Number of times to decrease transparency
    num_repeats = 31

    # Create a list to store the images
    image_list = [original_image]

    # Decrease transparency and append to the list for the specified number of repeats
    for _ in range(num_repeats):
        transparent_image = decrease_transparency(image_list[-1], 0.98)  # You can adjust the transparency factor (0.7 in this case)
        image_list.append(transparent_image)

    # Concatenate the images vertically
    result_image = Image.new('RGBA', (original_image.width, original_image.height * (num_repeats + 1)))
    for i, img in enumerate(image_list):
        result_image.paste(img, (0, i * original_image.height))

    # Save the final result
    result_image.save('output_result.png')

if __name__ == "__main__":
    main()
