import numpy as np
from PIL import Image
from plot_rgb_black import plot


def open_image():
    # Input path to your image here
    image_path = "path/to/your/image"
    image = Image.open(image_path)

    image_array = np.array(image)
    height, width, channels = image_array.shape

    downsampling_factor = 25

    rgb_values = np.zeros(((height // downsampling_factor) + 1, (width // downsampling_factor) + 1, 3))
    height_cor = [-value for value in range(0, height, downsampling_factor)]
    width_cor = [value for value in range(0, width, downsampling_factor)]

    for i in range(0, height, downsampling_factor):
        for j in range(0, width, downsampling_factor):
            if channels == 4:  # RGB + Alpha
                r, g, b, _ = image_array[i, j] / 255.0
            else:  # RGB without Alpha
                r, g, b = image_array[i, j, :3] / 255.0
            rgb_values[i // downsampling_factor, j // downsampling_factor] = np.array([r, g, b])

    return height_cor, width_cor, rgb_values, height, width


height, width, colors, h, w = open_image()
plot(height, width, colors, h, w)
