from PIL import Image
import os
import math

def generate_tiles(image_path, output_dir, zoom_levels, tile_size=256):
    """
    Generate map tiles from an image for multiple zoom levels.

    Parameters:
    - image_path: Path to the original map image (PNG).
    - output_dir: Directory to save the generated tiles.
    - zoom_levels: Number of zoom levels to generate.
    - tile_size: Size of each tile in pixels (default is 256x256).
    """
    # Load the original image
    original_image = Image.open(image_path)
    original_width, original_height = original_image.size

    for zoom in range(zoom_levels):
        # Calculate the scaled width and height for this zoom level
        scale_factor = 2 ** zoom
        scaled_width = original_width * scale_factor
        scaled_height = original_height * scale_factor
        print(f"Ancho: ${scaled_width}, Alto: ${scaled_height}")
        # Resize the image for this zoom level
        scaled_image = original_image.resize((scaled_width, scaled_height), Image.ANTIALIAS)

        # Calculate the number of tiles in each dimension
        x_tiles = math.ceil(scaled_width / tile_size)
        y_tiles = math.ceil(scaled_height / tile_size)

        # Create directories for this zoom level
        zoom_dir = os.path.join(output_dir, str(zoom))
        os.makedirs(zoom_dir, exist_ok=True)

        # Generate tiles for this zoom level
        for x in range(x_tiles):
            for y in range(y_tiles):
                # Calculate the tile's position in the image
                left = x * tile_size
                upper = y * tile_size
                right = min((x + 1) * tile_size, scaled_width)
                lower = min((y + 1) * tile_size, scaled_height)

                # Crop the tile from the scaled image
                tile = scaled_image.crop((left, upper, right, lower))

                # Save the tile as a PNG file
                tile_path = os.path.join(zoom_dir, f"{x}_{y}.png")
                tile.save(tile_path)

                print(f"Saved tile: {tile_path}")

if __name__ == "__main__":
    # Example usage
    image_path = "pisos/floor-07-map.png"  # Path to your map image
    output_dir = "tiles"  # Output directory for tiles
    zoom_levels = 4  # Number of zoom levels to generate

    generate_tiles(image_path, output_dir, zoom_levels)
