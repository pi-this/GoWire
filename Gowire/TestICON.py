import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
import os

def create_text_image(text, font_size=20):
    # Create an image with white background
    image = Image.new('RGBA', (100, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # Get text size and position
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (image.width - text_width) // 2
    text_y = (image.height - text_height) // 2

    # Draw the text onto the image
    draw.text((text_x, text_y), text, fill="black", font=font)

    return image

def main():
    # Create the main window
    root = tk.T
    
    
main()
create_text_image(⚙️)