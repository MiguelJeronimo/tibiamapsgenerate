import os
from PIL import Image

def generate_tiles(image_path, output_dir, level_count=6, tile_size=256):
    # Cargar la imagen ajustada
    image = Image.open(image_path)
    width, height = image.size

    # Verificar que la imagen es cuadrada
    if width != height:
        raise ValueError("La imagen debe ser cuadrada (ej. 4096x4096).")

    # Iterar sobre los niveles de zoom
    for level in range(level_count):
        scale = 2 ** level
        level_width = width // scale
        level_height = height // scale
        resized_image = image.resize((level_width, level_height), Image.ANTIALIAS)

        # Crear la carpeta para el nivel de zoom
        level_dir = os.path.join(output_dir, str(level))
        os.makedirs(level_dir, exist_ok=True)

        # Dividir en tiles
        for x in range(0, level_width, tile_size):
            for y in range(0, level_height, tile_size):
                tile = resized_image.crop((x, y, x + tile_size, y + tile_size))
                tile_dir = os.path.join(level_dir, str(x // tile_size))
                os.makedirs(tile_dir, exist_ok=True)

                tile_path = os.path.join(tile_dir, f"{y // tile_size}.png")
                tile.save(tile_path)

    print("Tiles generados correctamente.")

if __name__ == '__main__':
    # Rutas
    image_path = 'floor-07-map-padded.png'
    output_dir = 'tiles3'

    # Generar los tiles con nivel de zoom hasta 6
    generate_tiles(image_path, output_dir, level_count=8, tile_size=256)
