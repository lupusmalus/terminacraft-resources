from PIL import Image, ImageEnhance

def apply_tint(image, tint_color, intensity):
    # Create a solid color image of the same size as the input image
    tint = Image.new('RGBA', image.size, tint_color)

    # Enhance the color of the original image with the tint color
    enhancer = ImageEnhance.Color(image)
    tinted_image = enhancer.enhance(intensity)

    # Split the tinted image into RGB channels
    r, g, b, a = tinted_image.split()

    # Create a mask based on the alpha channel of the tint image
    mask = a.point(lambda x: x * 0.02)  # Adjust transparency factor if needed

    # Paste the tint image onto the original image using the mask
    tinted_image.paste(tint, (0, 0), mask)

    return tinted_image

def main():
    # Open the original image
    original_image_path = 'twinmold.png'  # Use an image with an alpha channel (PNG format)
    original_image = Image.open(original_image_path).convert('RGBA')

    # Define the tint color (light green in this case)
    tint_color = (255, 165, 77, 255)  # RGBA values for light red



    # Number of times to repeat the process
    num_repeats = 31

    # Create a list to store the images
    image_list = [original_image]

    # Apply the tint and append to the list for the specified number of repeats
    for _ in range(num_repeats):
        tinted_image = apply_tint(image_list[-1], tint_color, 1)  # You can adjust the intensity (1.3 in this case)
        image_list.append(tinted_image)

    # Create a reversed list of tinted images
    reversed_image_list = list(reversed(image_list))

    # Concatenate the images vertically
    result_image = Image.new('RGBA', (original_image.width, original_image.height * (2 * (num_repeats + 1))))
    for i, img in enumerate(image_list + reversed_image_list):
        result_image.paste(img, (0, i * original_image.height))

    # Save the final result
    result_image.save('output_result.png')

if __name__ == "__main__":
    main()
