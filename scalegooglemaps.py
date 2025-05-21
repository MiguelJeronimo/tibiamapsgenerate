from PIL import Image
import os
import math

def generate_tiles(image_path, output_dir, level_count=8, tile_size=256):
    # Load the base image
    base_image = Image.open(image_path)

    # Calculate the dimensions for each zoom level
    width, height = base_image.size
    max_dimension = max(width, height)

    for level in range(level_count):
        scale = 2 ** level
        zoom_width = math.ceil(width / scale)
        zoom_height = math.ceil(height / scale)

        # Resize the image for the current zoom level
        resized_image = base_image.resize((zoom_width, zoom_height), Image.ANTIALIAS)

        # Create the directory structure for the zoom level
        level_dir = os.path.join(output_dir, str(level))
        os.makedirs(level_dir, exist_ok=True)

        # Slice the image into tiles
        for x in range(0, zoom_width, tile_size):
            for y in range(0, zoom_height, tile_size):
                # Define the tile box
                tile_box = (x, y, min(x + tile_size, zoom_width), min(y + tile_size, zoom_height))
                tile = resized_image.crop(tile_box)

                # Save the tile
                tile_x = x // tile_size
                tile_y = y // tile_size
                tile_path = os.path.join(level_dir, f"{tile_x}_{tile_y}.png")
                tile.save(tile_path)

    print(f"Tiles generated in {output_dir}")

if __name__ == '__main__':
    # Example usage
    image_path = "floor-07-map-padded.png"
    output_dir = "google2"
    generate_tiles(image_path, output_dir, level_count=8, tile_size=1024)
