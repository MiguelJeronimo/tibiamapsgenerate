from PIL import Image, ImageOps

if __name__ == '__main__':
    # Cargar la imagen original
    image = Image.open('pisos/floor-07-map.png')

    # Agregar bordes para hacer la imagen cuadrada de 4096x4096 píxeles
    new_size = (4096, 4096)
    padded_image = ImageOps.pad(image, new_size, color=(0, 0, 0))

    # Guardar la imagen con bordes
    padded_image.save('floor-07-map-padded.png')

    print("Imagen con bordes guardada.")
