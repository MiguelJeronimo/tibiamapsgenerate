import os
from PIL import Image

def generate_tiles(image_path, output_dir, tile_size=256, full_width=2560, full_height=2048):
    """
    Generate map tiles for a single zoom level.

    Args:
        image_path (str): Path to the full map image.
        output_dir (str): Directory to save the tiles.
        tile_size (int): Size of each tile in pixels (default is 256).
        full_width (int): Width of the full map image.
        full_height (int): Height of the full map image.
    """
    # Load the full map image
    image = Image.open(image_path)
    image = image.resize((full_width, full_height), Image.ANTIALIAS)

    # Calculate the number of tiles
    tiles_x = full_width // tile_size
    tiles_y = full_height // tile_size

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate tiles
    for x in range(tiles_x):
        for y in range(tiles_y):
            # Calculate the bounding box for the tile
            left = x * tile_size
            upper = y * tile_size
            right = left + tile_size
            lower = upper + tile_size

            # Crop the tile from the full image
            tile = image.crop((left, upper, right, lower))

            # Save the tile
            tile_dir = os.path.join(output_dir, "0", str(x))
            os.makedirs(tile_dir, exist_ok=True)
            tile_path = os.path.join(tile_dir, f"{y}.png")
            tile.save(tile_path)

            print(f"Saved tile: {tile_path}")
if __name__ == '__main__':
    # Example usage
    floors = ["00", "01", "02","03", "04", "05","06", "07", "08", "09", "10","11", "12", "13", "14", "15"]
    for floor in floors:
        print(f"Image name: floor-{floor}-map.png")
        image_path = f"pisos/floor-{floor}-map.png"  # Input map image
        output_dir = f"tibiamaps/{int(floor)}"  # Output directory for tiles
        generate_tiles(image_path, output_dir)
        print(f"PISO: {floor} terminado....")
