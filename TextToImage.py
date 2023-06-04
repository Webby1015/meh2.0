from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def draw_text_on_image(text):
    if not os.path.exists('jokes'):
        os.makedirs('jokes')
    img = Image.new('RGB', (500, 500), color = (0, 0, 0))
    d = ImageDraw.Draw(img)
    fontsize = 20
    font = ImageFont.truetype("arial.ttf", fontsize)
    textwidth, textheight = d.textsize(text, font)

    if textwidth > img.width:
        lines = textwrap.wrap(text, width=20)
        y_text = (img.height - textheight * len(lines)) / 2
        for line in lines:
            width, height = font.getsize(line)
            d.text(((img.width - width) / 2, y_text), line, fill=(255,255,255), font=font)
            y_text += height
    else:
        d.text(((img.width - textwidth) / 2, (img.height - textheight) / 2), text, fill=(255,255,255), font=font)

    img.save("jokes/joke.jpg")

