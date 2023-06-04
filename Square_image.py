from PIL import Image

def make_square(image_path):
    """
    Resize an image to a square by adding black bars around it.
    """
    with Image.open(image_path) as image:
        width, height = image.size
        size = max(width, height)
        new_image = Image.new('RGB', (size, size), (0, 0, 0))
        new_image.paste(image, ((size - width) // 2, (size - height) // 2))
        return new_image
    
