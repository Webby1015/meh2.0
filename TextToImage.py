import os
from PIL import Image, ImageDraw, ImageFont

def create_text_image(text):
    width, height = 500, 500
    background_color = (0, 0, 0)  # Black color for the background
    border_color = (255, 255, 255)  # White color for the border

    # Create the image with a black background
    img = Image.new('RGB', (width, height), background_color)

    # Create a bordered image with a 2-pixel wider and taller size
    bordered_width = width + 4
    bordered_height = height + 4
    bordered_img = Image.new('RGB', (bordered_width, bordered_height), background_color)

    # Paste the original image onto the bordered image with an offset of (2, 2)
    bordered_img.paste(img, (2, 2))

    # Create a drawing object
    draw = ImageDraw.Draw(bordered_img)

    font_size = 35
    reduced_font_size = int(font_size * 0.7)  # Decrease the font size by 30%
    font = ImageFont.truetype("arial.ttf", reduced_font_size)

    # Calculate the maximum text width and height based on the image size
    max_text_width = bordered_width - 20  # Leave some padding on each side
    max_text_height = bordered_height - 20  # Leave some padding on each side

    # Split the text into multiple lines if it exceeds the maximum width
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        text_width, _ = draw.textsize(test_line, font=font)
        if text_width <= max_text_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())

    # Calculate the total text height and starting position
    line_count = len(lines)
    total_text_height = line_count * font_size
    text_start_y = (bordered_height - total_text_height) // 2

    # Draw each line of text
    text_color = (255, 255, 255)  # White color for the text
    for line in lines:
        text_width, _ = draw.textsize(line, font=font)
        text_position = ((bordered_width - text_width) // 2, text_start_y)
        draw.text(text_position, line, fill=text_color, font=font)
        text_start_y += font_size

    # Draw a border around the image
    border_width = 2
    border_rectangle = [(0, 0), (bordered_width - 1, bordered_height - 1)]
    draw.rectangle(border_rectangle, outline=border_color, width=border_width)

    # Create the "image/photos" directory if it does not exist
    if not os.path.exists('images/photos'):
        os.makedirs('images/photos')

    # Save the image in the "image/photos" directory
    image_path = os.path.join('images/photos', 'text_image.jpg')
    bordered_img.save(image_path)

# Example usage:
text_to_display = "Hello, 234World! This is a long text that needs to be divided into multiple lines if it exceeds the width of the image."
create_text_image(text_to_display)
