#!/usr/bin/env python3
import argparse
from PIL import Image, ImageDraw, ImageFont
import os

COLORS = {
    "black": "#000000",
    "white": "#FFFFFF",
    "dark_blue_gray": "#2C3E50",
    "charcoal_gray": "#34495E",
    "light_gray": "#95A5A6",
    "sun_yellow": "#F1C40F",
    "dark_orange": "#F39C12",
    "red_orange": "#E74C3C",
    "dark_red": "#C0392B",
    "emerald_green": "#2ECC71",
    "bright_blue": "#3498DB",
    "steel_blue": "#2980B9",
    "light_silver": "#ECF0F1",
    "silver_gray": "#BDC3C7",
    "amethyst_purple": "#9B59B6",
}

SCALE_FACTOR = 4
BASE_SIZE = 64
RENDER_SIZE = BASE_SIZE * SCALE_FACTOR

def create_icon_base():
    """Creates a new 256x256 RGBA image with a transparent background."""
    img = Image.new('RGBA', (RENDER_SIZE, RENDER_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    return img, draw

def scale_coords(coords):
    """Scale coordinates by SCALE_FACTOR."""
    if isinstance(coords, (list, tuple)):
        # Check if this is a coordinate pair (x, y) or a list of coordinate pairs
        if len(coords) == 2 and not isinstance(coords[0], (list, tuple)):
            # Single coordinate pair (x, y)
            return (coords[0] * SCALE_FACTOR, coords[1] * SCALE_FACTOR)
        else:
            # List of coordinate pairs [(x1, y1), (x2, y2), ...]
            return [scale_coords(c) for c in coords]
    return coords * SCALE_FACTOR

def save_icon(img, app_name, output_base_dir=""):
    """Saves the generated icon to the specified path within the app's directory structure."""
    # Resize down to final size with high-quality resampling
    img_final = img.resize((BASE_SIZE, BASE_SIZE), Image.LANCZOS)
    
    output_dir = os.path.join(output_base_dir, app_name)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'icon_64x64.png')
    img_final.save(output_path, 'PNG', optimize=True)
    print(f"Icon saved for {app_name}: {output_path}")

def generate_quasi_bird_icon():
    img, draw = create_icon_base()
    # Draw bird body (yellow circle) - scaled up and centered
    draw.ellipse(scale_coords([(10, 15), (50, 55)]), fill=COLORS["sun_yellow"], outline=COLORS["dark_orange"], width=12)
    # Draw wing - adjusted for new body size and position
    draw.ellipse(scale_coords([(15, 35), (40, 50)]), fill=COLORS["dark_orange"], outline=COLORS["red_orange"], width=8)
    # Draw eye - adjusted for new body size and position
    draw.ellipse(scale_coords([(32, 22), (42, 32)]), fill=COLORS["white"], outline=COLORS["black"], width=8)
    draw.ellipse(scale_coords([(35, 25), (39, 29)]), fill=COLORS["black"])
    # Draw beak - adjusted for new body size and position
    beak = scale_coords([(44, 34), (56, 34), (49, 40)])
    draw.polygon(beak, fill=COLORS["dark_orange"], outline=COLORS["red_orange"], width=4)
    beak = scale_coords([(44, 34), (56, 34), (49, 28)])
    draw.polygon(beak, fill=COLORS["dark_orange"], outline=COLORS["red_orange"], width=4)
    return img

def generate_quasi_calculator_icon():
    img, draw = create_icon_base()
    # Draw calculator body (rounded rectangle)
    draw.rounded_rectangle(scale_coords([(8, 8), (56, 56)]), radius=16, fill=COLORS["dark_blue_gray"], outline=COLORS["charcoal_gray"], width=8)
    # Draw display area (smaller rounded rectangle at top)
    draw.rounded_rectangle(scale_coords([(12, 12), (52, 22)]), radius=8, fill=COLORS["light_gray"])
    # Draw calculator buttons (grid)
    button_positions = [
        (14, 26), (26, 26), (38, 26),
        (14, 34), (26, 34), (38, 34),
        (14, 42), (26, 42), (38, 42),
    ]
    for x, y in button_positions:
        draw.rectangle(scale_coords([(x, y), (x+8, y+6)]), fill=COLORS["light_gray"], outline=COLORS["silver_gray"], width=4)
    return img

def generate_quasi_nametag_icon():
    img, draw = create_icon_base()
    # Draw nametag body (rounded rectangle badge shape)
    draw.rounded_rectangle(scale_coords([(6, 14), (58, 50)]), radius=24, fill=COLORS["red_orange"], outline=COLORS["dark_red"], width=8)
    # Draw pin/clip at top
    draw.ellipse(scale_coords([(28, 8), (36, 16)]), fill=COLORS["light_gray"], outline=COLORS["silver_gray"], width=4)
    draw.rectangle(scale_coords([(30, 12), (34, 18)]), fill=COLORS["light_gray"])
    # Draw name lines (simulating text)
    draw.rectangle(scale_coords([(12, 22), (52, 26)]), fill=COLORS["white"])
    draw.rectangle(scale_coords([(12, 30), (45, 34)]), fill=COLORS["white"])
    draw.rectangle(scale_coords([(12, 38), (42, 42)]), fill=COLORS["white"])
    return img

def generate_quasi_doodle_icon():
    img, draw = create_icon_base()
    # Draw canvas frame (white canvas with border)
    draw.rounded_rectangle(scale_coords([(4, 4), (60, 60)]), radius=16, fill=COLORS["white"], outline=COLORS["light_gray"], width=8)
    # Draw inner canvas area
    draw.rounded_rectangle(scale_coords([(8, 8), (56, 56)]), radius=8, fill=COLORS["light_silver"])
    # Draw colorful doodles/squiggles on the canvas
    draw.ellipse(scale_coords([(14, 16), (26, 28)]), fill=COLORS["red_orange"])
    draw.ellipse(scale_coords([(18, 22), (30, 34)]), fill=COLORS["red_orange"])
    draw.ellipse(scale_coords([(22, 28), (34, 40)]), fill=COLORS["red_orange"])
    # Blue doodle
    draw.ellipse(scale_coords([(32, 14), (44, 26)]), fill=COLORS["bright_blue"])
    draw.ellipse(scale_coords([(36, 20), (48, 32)]), fill=COLORS["bright_blue"])
    # Yellow/Orange doodle
    draw.ellipse(scale_coords([(16, 36), (28, 48)]), fill=COLORS["dark_orange"])
    draw.ellipse(scale_coords([(20, 42), (32, 54)]), fill=COLORS["dark_orange"])
    # Purple accent
    draw.ellipse(scale_coords([(38, 34), (48, 44)]), fill=COLORS["amethyst_purple"])
    # Draw cursor crosshair (green to match app's CURSOR_COLOR)
    cursor_x, cursor_y = 46 * SCALE_FACTOR, 18 * SCALE_FACTOR
    cursor_size = 6 * SCALE_FACTOR
    draw.ellipse([(cursor_x - cursor_size, cursor_y - cursor_size),
                  (cursor_x + cursor_size, cursor_y + cursor_size)],
                 outline=COLORS["white"], width=8)
    draw.ellipse([(cursor_x - cursor_size + SCALE_FACTOR, cursor_y - cursor_size + SCALE_FACTOR),
                  (cursor_x + cursor_size - SCALE_FACTOR, cursor_y + cursor_size - SCALE_FACTOR)],
                 fill=COLORS["emerald_green"], outline=COLORS["emerald_green"], width=4)
    return img

def generate_camera_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60,60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    # Camera body - shifted up and slightly larger
    draw.rounded_rectangle(scale_coords([(4, 14), (60, 50)]), radius=24, fill=COLORS["charcoal_gray"], outline=COLORS["dark_blue_gray"], width=8)
    # draw.rounded_rectangle(scale_coords([(4, 14), (60, 50)]), radius=24, fill=COLORS["charcoal_gray"], outline=COLORS["silver_gray"], width=8)
    # Lens - shifted up and slightly larger
    draw.ellipse(scale_coords([(20,20), (44, 44)]), fill=COLORS["light_gray"], outline=COLORS["silver_gray"], width=8)
    draw.ellipse(scale_coords([(26, 26), (38, 38)]), fill=COLORS["dark_blue_gray"])
    # Flash
    draw.rectangle(scale_coords([(48, 18), (56, 24)]), fill=COLORS["sun_yellow"], outline=COLORS["dark_orange"], width=4)
    # Shutter button
    draw.ellipse(scale_coords([(50, 12), (54, 16)]), fill=COLORS["red_orange"], outline=COLORS["dark_red"], width=4)
    return img

def generate_confetti_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60,60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    colors = [COLORS["red_orange"], COLORS["sun_yellow"], COLORS["emerald_green"], COLORS["bright_blue"], COLORS["amethyst_purple"]]
    
    import random
    random.seed(44)  # Fixed seed for consistency
    for _ in range(50):
        x = random.randint(20, 54) * SCALE_FACTOR
        y = random.randint(5, 34) * SCALE_FACTOR
        size = random.randint(3, 6) * SCALE_FACTOR
        color = random.choice(colors)
        draw.rectangle([(x, y), (x + size, y + size)], fill=color)
    draw.polygon(scale_coords([(20, 25), (45, 38), (10, 59)]), fill=COLORS["red_orange"], outline=COLORS["dark_red"], width=4)
    return img

def generate_connect4_icon():
    img, draw = create_icon_base()
    # Background color
    # draw.rectangle([(0, 0), (RENDER_SIZE, RENDER_SIZE)], fill=(52, 73, 94))
    
    # Draw blue board
    # draw.rectangle(scale_coords([(4, 4), (60, 60)]), fill=COLORS["bright_blue"]))
    draw.rounded_rectangle(scale_coords([(4, 4), (60, 60)]), radius=16, fill=COLORS["bright_blue"])
    
    # Colors for pieces
    colors = [
        COLORS["red_orange"],  # Red
        COLORS["sun_yellow"],  # Yellow
        COLORS["light_silver"]  # Empty
    ]
    
    # Predefined pattern (without last column)
    pattern = [
        [2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2],
        [2, 2, 0, 0, 2, 2],
        [2, 0, 0, 1, 2, 2],
        [0, 1, 0, 1, 0, 2],
        [0, 1, 1, 0, 0, 1],
    ]
    
    cell_size = 8 * SCALE_FACTOR
    start_x = 9 * SCALE_FACTOR
    start_y = 9 * SCALE_FACTOR
    
    for row in range(6):
        for col in range(6):  # Reduced to 6 columns
            x = start_x + col * cell_size
            y = start_y + row * cell_size
            draw.ellipse([(x, y), (x + 6 * SCALE_FACTOR, y + 6 * SCALE_FACTOR)],
                         fill=colors[pattern[row][col]])
    
    return img



def generate_draw_icon():
    img, draw = create_icon_base()

    pencil_point_x=26
    pencil_point_y=40
    pencil_outline_color = COLORS["dark_orange"]
    pencil_color = COLORS["sun_yellow"]
    pencil_line_color = COLORS["bright_blue"]
    x_offset = -5
    # Circle background
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    
    draw.line(scale_coords([(25+x_offset, 45), (55, 45)]), fill=pencil_line_color, width=12)
    # draw.polygon(scale_coords([(20, 45), (25, 30), (35, 35)]), fill=pencil_line_color, outline=pencil_outline_color, width=0)
    draw.polygon(scale_coords([(25+x_offset, 43), (29+x_offset, 31), (36+x_offset, 37)]), fill=pencil_line_color, outline=pencil_outline_color, width=0)
    # Cover edge
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), outline=COLORS["light_gray"], width=8)
    # PENCIL BODY
    draw.polygon(scale_coords([ (30+x_offset, 30), (37+x_offset, 36), (60+x_offset,10), (54+x_offset,4)]), fill=pencil_line_color, outline=pencil_outline_color, width=0)
    # pencil_x = 45
    # pencil_y = 4
    # pencil_width = 15
    # pencil_height = 35
    # pencil_offset = 15
    # # draw.polygon(scale_coords([(pencil_x, pencil_y), (pencil_x+pencil_width, pencil_y), (pencil_x+pencil_width-pencil_offset, pencil_y+pencil_height), (pencil_x-pencil_offset, pencil_y+pencil_height)]), fill=pencil_color, outline=pencil_outline_color, width=10)
    # draw.polygon(scale_coords([(pencil_point_x, pencil_point_y+1), (25, 30), (40, 38)]), fill=pencil_color, outline=pencil_outline_color, width=0)
    # draw.polygon(scale_coords([(45, 2), (60,12),  (45, 30), (30, 20)]), fill=pencil_color, outline=pencil_outline_color, width=1)
    # draw.polygon(scale_coords([(32, y_pos-40), (54, y_pos), (10, y_pos)]), fill=COLORS["sun_yellow"], outline=COLORS["dark_orange"], width=10)

    return img

def generate_errortest_icon():
    img, draw = create_icon_base()
    y_pos= 46
    draw.ellipse(scale_coords([(4, 4), (60,60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    
    # Warning triangle
    draw.polygon(scale_coords([(32, y_pos-40), (54, y_pos), (10, y_pos)]), fill=COLORS["sun_yellow"], outline=COLORS["dark_orange"], width=10)
    # Exclamation mark
    draw.rectangle(scale_coords([(30, y_pos-28), (34, y_pos-12)]), fill=COLORS["dark_blue_gray"])
    draw.ellipse(scale_coords([(30, y_pos-8), (34, y_pos-4)]), fill=COLORS["dark_blue_gray"])
    return img

def generate_filemanager_icon():
    img, draw = create_icon_base()
    # Circle background
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    folder_top = 14
    folder_height = 34
    folder_x = 10
    folder_width = 44
    content_y_offset = -4
    front_offset_x = 7
    front_offset_y = -8

    # Define points for the folder shapes
    # Folder back shape points
    folder_back_points = [
        (folder_x, folder_top), (28, folder_top), (32, folder_top-4), (folder_x+folder_width, folder_top-4), (folder_x+folder_width, folder_top+folder_height), (folder_x, folder_top+folder_height)
    ]
    # Folder content shape points (slightly smaller and offset)
    folder_content_points = [
        (12, folder_top-content_y_offset), (52, folder_top-content_y_offset), (52, folder_top+folder_height), (12, folder_top+folder_height)
    ]
    # Folder front shape points
    folder_front_points = [
        (folder_x-front_offset_x, folder_top-front_offset_y), (folder_x+folder_width-front_offset_x, folder_top-front_offset_y), (folder_x+folder_width, folder_top+folder_height), (folder_x, folder_top+folder_height)
    ]

    # Folder icon back shape
    draw.polygon(scale_coords(folder_back_points), fill=COLORS["bright_blue"], outline=COLORS["steel_blue"], width=8)
    # Folder content shape
    draw.polygon(scale_coords(folder_content_points), fill=COLORS["silver_gray"],outline=COLORS["light_gray"], width=8)
    # Folder front shape
    draw.polygon(scale_coords(folder_front_points), fill=COLORS["bright_blue"], outline=COLORS["steel_blue"], width=8)

    return img

def generate_helloworld_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    # Speech bubble
    draw.rounded_rectangle(scale_coords([(3, 12), (61, 52)]), radius=32, fill=COLORS["steel_blue"], outline=COLORS["bright_blue"], width=16)
    # draw.polygon(scale_coords([(20, 50), (28, 62), (30, 50)]), fill=COLORS["steel_blue"], outline=COLORS["bright_blue"], width=16)
    # Text "Hello!" using font
    try:
        font = ImageFont.truetype("assets/Archivo-Bold.ttf", scale_coords(15))
        draw.text(scale_coords((12, 16)), "Hello", font=font, fill=COLORS["white"])
        draw.text(scale_coords((12, 31)), "World", font=font, fill=COLORS["white"])
    except:
        # Fallback if font not available
        draw.text(scale_coords((12, 25)), "Hello!", fill=COLORS["white"])
    return img

def generate_imageview_icon():
    img, draw = create_icon_base()
    # Mountain landscape
    draw.rounded_rectangle([scale_coords((4, 4)), scale_coords((60, 60))], fill=COLORS["bright_blue"], radius=scale_coords(4))
    # draw.rectangle([(0, 0), (RENDER_SIZE, RENDER_SIZE)], fill=COLORS["bright_blue"]))
    # draw.polygon(scale_coords([(6, 40), (32, 15), (58, 40), (58, 58), (6, 58)]), fill=COLORS["emerald_green"]))
    draw.rounded_rectangle([scale_coords((4, 40)), scale_coords((60, 60))], fill=COLORS["emerald_green"], radius=scale_coords(4))
    # house
    # draw.polygon(scale_coords([(14, 35), (24, 25), (34, 35), (34, 48), (14, 48)]), fill=COLORS["dark_blue_gray"]))
    # landscape
    draw.polygon(scale_coords([(6, 40), (32, 26), (58, 40), (58, 58), (6, 58)]), fill=COLORS["emerald_green"])
    # Sun
    draw.ellipse(scale_coords([(39, 12), (53, 27)]), fill=COLORS["sun_yellow"])
    return img

def generate_imu_icon():
    img, draw = create_icon_base()
    x_color = COLORS["bright_blue"] 
    y_color = COLORS["dark_red"]
    z_color = COLORS["emerald_green"]
    width = 2

    # Draw background circle
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)

    # Draw x_color ellipse directly (no rotation)
    draw.ellipse(scale_coords([(20, 10), (44, 54)]), outline=x_color, width=scale_coords(width))

    # Create temporary image for y_color ellipse, rotate, and paste
    y_ellipse_img = Image.new('RGBA', (RENDER_SIZE, RENDER_SIZE), (0, 0, 0, 0))
    y_ellipse_draw = ImageDraw.Draw(y_ellipse_img)
    y_ellipse_draw.ellipse(scale_coords([(12, 22), (52, 42)]), outline=y_color, width=scale_coords(width))
    # y_ellipse_draw.arc(scale_coords([(12, 22), (52, 42)]),start=-140, end=0, fill=y_color, width=scale_coords(width))
    y_ellipse_rotated = y_ellipse_img.rotate(30, center=(RENDER_SIZE/2, RENDER_SIZE/2), expand=False)
    img.paste(y_ellipse_rotated, (0, 0), y_ellipse_rotated)

    # Create temporary image for z_color ellipse, rotate, and paste
    z_ellipse_img = Image.new('RGBA', (RENDER_SIZE, RENDER_SIZE), (0, 0, 0, 0))
    z_ellipse_draw = ImageDraw.Draw(z_ellipse_img)
    z_ellipse_draw.ellipse(scale_coords([(14, 22), (50, 42)]), outline=z_color, width=scale_coords(width))
    z_ellipse_rotated = z_ellipse_img.rotate(-30, center=(RENDER_SIZE/2, RENDER_SIZE/2), expand=False)
    img.paste(z_ellipse_rotated, (0, 0), z_ellipse_rotated)
    
    # Create temporary image for y_color ellipse, rotate, and paste
    y_ellipse_img = Image.new('RGBA', (RENDER_SIZE, RENDER_SIZE), (0, 0, 0, 0))
    y_ellipse_draw = ImageDraw.Draw(y_ellipse_img)
    # y_ellipse_draw.ellipse(scale_coords([(12, 22), (52, 42)]), outline=y_color, width=scale_coords(width))
    y_ellipse_draw.arc(scale_coords([(12, 22), (52, 42)]),start=-140, end=0, fill=y_color, width=scale_coords(width))
    y_ellipse_rotated = y_ellipse_img.rotate(30, center=(RENDER_SIZE/2, RENDER_SIZE/2), expand=False)
    img.paste(y_ellipse_rotated, (0, 0), y_ellipse_rotated)
    
    draw.arc(scale_coords([(20, 10), (44, 54)]),start=-50, end=44, fill=x_color, width=scale_coords(width))
    return img

def generate_musicplayer_icon():
    img, draw = create_icon_base()
    note_y = 42
    note_x = 25
    note_size = 11
    note_thick = 3
    second_note_x_offset = 18
    second_note_y_offset = -3
    note_height = 20
    note_color = COLORS["dark_red"]
    # Background
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    note_shape = scale_coords([(note_x, note_y), (note_x, note_height), (note_x+second_note_x_offset, note_height + second_note_y_offset),(note_x+second_note_x_offset, note_y + second_note_y_offset)])
    # Note line all in one
    draw.polygon(note_shape,  outline=note_color, width=scale_coords(note_thick))
    # Erase bottom part
    draw.rectangle(scale_coords([(note_x+note_thick, note_y+second_note_y_offset-note_thick), (note_x+second_note_x_offset-note_thick, note_y)]), fill=COLORS["silver_gray"])
    

    # Main music note shape
    draw.ellipse(scale_coords([(note_x-note_size+note_thick, note_y-note_size+(note_size/2)), (note_x+note_thick, note_y+(note_size/2))]), fill=note_color)
    # draw.rectangle(scale_coords([(note_x+note_size-note_thick, note_height), (note_x+note_size, note_y-(note_size/2))]), fill=COLORS["red_orange"]))
    # Second note
    draw.ellipse(scale_coords([(note_x-note_size + second_note_x_offset, note_y-note_size+second_note_y_offset+(note_size/2)), (note_x+ second_note_x_offset, note_y+second_note_y_offset+(note_size/2))]), fill=note_color)
    # draw.rectangle(scale_coords([(note_x+note_size-note_thick+ second_note_x_offset, note_height+second_note_y_offset), (note_x+note_size+ second_note_x_offset, note_y-(note_size/2)+second_note_y_offset)]), fill=COLORS["red_orange"]))
    # Connection
    # draw.line(([scale_coords((note_x+note_size-note_thick+ second_note_x_offset+3, note_height+second_note_y_offset)),scale_coords((note_x+note_size-3, note_height))]), fill=COLORS["red_orange"], width=scale_coords(3) ))



    # draw.arc(scale_coords([(35, 13), (48, 28)]), start=270, end=90, fill=COLORS["red_orange"], width=2))
    
    # Play button triangle (integrated)
    # draw.polygon(scale_coords([(25, 25), (40, 32), (25, 39)]), fill=COLORS["white"]))
    return img

def generate_nostr_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    # Speech bubble
    draw.rounded_rectangle(scale_coords([(5, 14), (59, 50)]), radius=32, fill=COLORS["steel_blue"], outline=COLORS["bright_blue"], width=16)
    draw.polygon(scale_coords([(20, 50), (28, 62), (30, 50)]), fill=COLORS["steel_blue"], outline=COLORS["bright_blue"], width=16)
    # Text "Hello!" using font
    try:
        font = ImageFont.truetype("assets/Archivo-Bold.ttf", scale_coords(15))
        draw.text(scale_coords((12, 25)), "nostr", font=font, fill=COLORS["white"])
    except:
        # Fallback if font not available
        draw.text(scale_coords((12, 25)), "nostr", fill=COLORS["white"])
    return img

def generate_chat_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    # Speech bubble
    draw.rounded_rectangle(scale_coords([(5, 14), (59, 50)]), radius=32, fill=COLORS["steel_blue"], outline=COLORS["bright_blue"], width=16)
    draw.polygon(scale_coords([(20, 50), (28, 62), (30, 50)]), fill=COLORS["steel_blue"], outline=COLORS["bright_blue"], width=16)
    # Text "Hello!" using font
    try:
        font = ImageFont.truetype("assets/Archivo-Bold.ttf", scale_coords(15))
        draw.text(scale_coords((12, 25)), "Hello!", font=font, fill=COLORS["white"])
    except:
        # Fallback if font not available
        draw.text(scale_coords((12, 25)), "Hello!", fill=COLORS["white"])
    return img

def generate_showbattery_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    # draw.ellipse(scale_coords([(4, 4), (60,60)]), fill=COLORS["light_gray"], outline=COLORS["silver_gray"], width=8)
    # Battery body
    draw.rounded_rectangle(scale_coords([(15, 20), (49, 44)]), radius=16, outline=COLORS["dark_blue_gray"], width=8)
    draw.rectangle(scale_coords([(49, 28), (52, 36)]), fill=COLORS["dark_blue_gray"])
    # Battery level (green)
    draw.rounded_rectangle(scale_coords([(17, 22), (47, 42)]), fill=COLORS["emerald_green"],radius=16)
    return img

def generate_showfonts_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    # draw.ellipse(scale_coords([(4, 4), (60,60)]), fill=COLORS["light_gray"], outline=COLORS["silver_gray"], width=8)
    font = ImageFont.truetype("assets/Archivo-Bold.ttf", scale_coords(28))
    draw.text(scale_coords((14, 16)), "Aa", font=font, fill=COLORS["steel_blue"])
    return img

def generate_soundrecorder_icon():
    img, draw = create_icon_base()

    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    # Colors
    mic_color = COLORS["charcoal_gray"] # Red microphone
    mic_dark = COLORS["black"]   # Darker red for shading
    stand_color = COLORS["dark_blue_gray"]   # Darker red for shading
    highlight = COLORS["light_gray"]   # Darker red for shading
    # stand_color = (80, 80, 80, 255)  # Gray stand
    # highlight = (255, 100, 100, 255)  # Light red highlight
    
    # Microphone head (rounded rectangle / ellipse)
    mic_top = 8
    mic_bottom = 36
    mic_left = 20
    mic_right = 44
    
    # Draw microphone body (rounded top)
    draw.ellipse(scale_coords([mic_left, mic_top, mic_right, mic_top + 16]), fill=mic_color)
    draw.rectangle(scale_coords([mic_left, mic_top + 8, mic_right, mic_bottom]), fill=mic_color)
    draw.ellipse(scale_coords([mic_left, mic_bottom - 8, mic_right, mic_bottom + 8]), fill=mic_color)
    
    # Microphone grille lines (horizontal lines on mic head)
    for y in range(mic_top + 6, mic_bottom - 4, 4):
        draw.line(scale_coords([(mic_left + 4, y), (mic_right - 4, y)]), fill=mic_dark, width=scale_coords(1))
    
    # Highlight on left side of mic
    draw.arc(scale_coords([mic_left + 2, mic_top + 2, mic_left + 10, mic_top + 18]),
             start=120, end=240, fill=highlight, width=scale_coords(2))
    
    # Microphone stand (curved arc under the mic)
    stand_top = mic_bottom + 4
    
    # Vertical stem from mic
    stem_x = BASE_SIZE // 2
    # draw.rectangle(scale_coords([stem_x - 2, mic_bottom, stem_x + 2, stand_top + 8]), fill=stand_color)
    
    # Curved holder around mic bottom
    draw.arc(scale_coords([mic_left - 4, mic_bottom - 8, mic_right + 4, mic_bottom + 16]),
             start=0, end=180, fill=stand_color, width=scale_coords(3))
    
    # Stand base
    base_y = 54
    draw.rectangle(scale_coords([stem_x - 2, stand_top + 4, stem_x + 2, base_y]), fill=stand_color)
    draw.ellipse(scale_coords([stem_x - 12, base_y - 2, stem_x + 12, base_y + 6]), fill=stand_color)
    
    # OVERWRITE EDGE
    draw.ellipse(scale_coords([(4, 4), (60, 60)]),  outline=COLORS["light_gray"], width=8)
    
    # Recording indicator (red dot with glow effect)
    dot_x, dot_y = 52, 12
    dot_radius = 5
    
    # Glow effect
    # for r in range(dot_radius + 3, dot_radius, -1):
    #     alpha = int(100 * (dot_radius + 3 - r) / 3)
    #     glow_color = (255, 0, 0, alpha)
    #     draw.ellipse(scale_coords([dot_x - r, dot_y - r, dot_x + r, dot_y + r]), fill=glow_color)
    
    # Solid red dot
    draw.ellipse(scale_coords([dot_x - dot_radius, dot_y - dot_radius,
                  dot_x + dot_radius, dot_y + dot_radius]),
                 fill=COLORS["red_orange"])
    
    # White highlight on dot
    draw.ellipse(scale_coords([dot_x - 2, dot_y - 2, dot_x, dot_y]), fill=(255, 200, 200, 255))
    return img

def generate_about_icon():
    img, draw = create_icon_base()
    # draw.rounded_rectangle(scale_coords([(5, 5), (59, 59)]), radius=32, fill=COLORS["white"]))
    draw.ellipse(scale_coords([(4, 4), (60,60)]), fill=COLORS["bright_blue"], outline=COLORS["silver_gray"], width=8)
    # Load the MicroPythonOS logo symbol
    try:
        logo = Image.open("assets/MicroPythonOS-logo-symbol-white(alpha)-short64.png").convert("RGBA")
        # Resize logo to fit within the icon
        logo = logo.resize((48 * SCALE_FACTOR, 48 * SCALE_FACTOR), Image.LANCZOS)
        # Calculate position to center the logo
        x = (RENDER_SIZE - logo.width) // 2
        y = (RENDER_SIZE - logo.height) // 2
        # Paste the logo onto the icon
        img.paste(logo, (x, y), logo)
        # font = ImageFont.truetype("assets/Archivo-Bold.ttf", 100)
        # draw.text(scale_coords((29, 19)), "i", font=font, fill=COLORS["white"]))
        draw.rectangle(scale_coords([(30, 29), (34, 41)]), fill=COLORS["white"])
        draw.ellipse(scale_coords([(30, 22), (34, 26)]), fill=COLORS["white"])
        
    except FileNotFoundError:
        print("Error: MicroPythonOS-logo-symbol-black-short64.png not found in assets directory.")
        draw.text(scale_coords((10, 20)), "About", fill=COLORS["black"])
    return img

def generate_appstore_icon():
    img, draw = create_icon_base()
    # draw.ellipse(scale_coords([(4, 4), (60,60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8))
    draw.ellipse(scale_coords([(4, 4), (60,60)]), fill=COLORS["charcoal_gray"], outline=COLORS["silver_gray"], width=8)
    # Draw a rounded rectangle as the base
    # draw.rounded_rectangle(scale_coords([(5, 5), (59, 59)]), radius=32, fill=COLORS["light_silver"], outline=COLORS["silver_gray"], width=8))
    # Draw four mini square items representing apps
    app_colors = [COLORS["bright_blue"], COLORS["emerald_green"], COLORS["sun_yellow"], COLORS["amethyst_purple"]]
    app_positions = [
        (18, 12), (34, 12),
        (18, 28), (34, 28),
    ]
    for i, (x, y) in enumerate(app_positions):
        draw.rectangle(scale_coords([(x, y), (x + 12, y + 12)]), fill=app_colors[i], outline=COLORS["charcoal_gray"], width=4)
    # Draw a download symbol (down arrow)
    draw.rectangle(scale_coords([(24, 35), (40, 52)]), fill=COLORS["red_orange"], outline=COLORS["charcoal_gray"])
    draw.polygon(scale_coords([(16, 48), (48, 48), (32, 62)]), fill=COLORS["red_orange"], outline=COLORS["charcoal_gray"])
    draw.rectangle(scale_coords([(26, 37), (38, 54)]), fill=COLORS["red_orange"])
    return img

def generate_osupdate_icon():
    img, draw = create_icon_base()
    background_color = COLORS["silver_gray"]
    # arrow_color = COLORS["white"]
    arrow_color = COLORS["bright_blue"]
    outline_width = 2
    arrow_bottom = 56
    arrow_head_width = 3
    arrow_width = 12
    draw.ellipse(scale_coords([(4, 4), (60,60)]), fill=background_color, outline=COLORS["light_gray"], width=8)
    try:
        logo = Image.open("assets/MicroPythonOS-logo-symbol-white(alpha)-short64.png").convert("RGBA")
        logo = logo.resize((48 * SCALE_FACTOR, 48 * SCALE_FACTOR), Image.LANCZOS)
        x = (RENDER_SIZE - logo.width) // 2
        y = (RENDER_SIZE - logo.height) // 2
        img.paste(logo, (x, y), logo)
    except FileNotFoundError:
        print("Error: MicroPythonOS-logo-symbol-white(alpha)-short64.png not found in assets directory.")
    # Draw an upload symbol (up arrow)
    draw.rectangle(scale_coords([(24, 35), (40, arrow_bottom)]), fill=arrow_color, outline=background_color, width= scale_coords(outline_width))
    draw.polygon(scale_coords([(19, 34), (45, 34), (32, 22)]), fill=arrow_color)
    draw.rectangle(scale_coords([(25, 33), (39, arrow_bottom-outline_width)]), fill=arrow_color)
    return img

def generate_launcher_icon():
    img, draw = create_icon_base()
    # Light gray circular background
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    # Draw logo
    # Load the MicroPythonOS logo symbol
    try:
        logo = Image.open("assets/MicroPythonOS-logo-symbol-white(alpha)-short64.png").convert("RGBA")
        # Resize logo to fit within the icon
        logo = logo.resize((48 * SCALE_FACTOR, 48 * SCALE_FACTOR), Image.LANCZOS)
        # Calculate position to center the logo
        x = (RENDER_SIZE - logo.width) // 2
        y = (RENDER_SIZE - logo.height) // 2
        # Paste the logo onto the icon
        img.paste(logo, (x, y), logo)
        # Text "app" in the middle
    
        font = ImageFont.truetype("assets/Archivo-Bold.ttf", scale_coords(20))
        text = "app"
        # Calculate text size to center it
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (RENDER_SIZE - text_width) // 2
        y= RENDER_SIZE //2 - text_height + (text_height//4)

        draw.text((x, y), text, font=font, fill=COLORS["light_gray"])
    except FileNotFoundError:
        print("Error: Archivo-Bold.ttf not found in assets directory. Using default font.")
        draw.text(scale_coords((18, 20)), "app", fill=COLORS["dark_blue_gray"])
    return img

def main():
    parser = argparse.ArgumentParser(description="Generate app icons.")
    parser.add_argument('--app', nargs='*', help='Specify app names to generate icons for (e.g., "QuasiBird" "QuasiCalculator"). If not specified, all icons will be generated.')
    args = parser.parse_args()

    apps = {
        "com.micropythonos.camera": generate_camera_icon,
        "com.micropythonos.confetti": generate_confetti_icon,
        "com.micropythonos.connect4": generate_connect4_icon,
        "com.micropythonos.draw": generate_draw_icon,
        "com.micropythonos.errortest": generate_errortest_icon,
        "com.micropythonos.filemanager": generate_filemanager_icon,
        "com.micropythonos.helloworld": generate_helloworld_icon,
        "com.micropythonos.imageview": generate_imageview_icon,
        "com.micropythonos.imu": generate_imu_icon,
        "com.micropythonos.musicplayer": generate_musicplayer_icon,
        "com.micropythonos.nostr": generate_nostr_icon,
        "generic_chat": generate_chat_icon,
        "com.micropythonos.showbattery": generate_showbattery_icon,
        "com.micropythonos.showfonts": generate_showfonts_icon,
        "com.micropythonos.soundrecorder": generate_soundrecorder_icon,
        "com.micropythonos.about": generate_about_icon,
        "com.micropythonos.appstore": generate_appstore_icon,
        "com.micropythonos.osupdate": generate_osupdate_icon,
        "com.micropythonos.launcher": generate_launcher_icon,
        "com.micropythonos.howto": generate_howto_icon,
        "com.micropythonos.settings": generate_settings_icon,
        "com.micropythonos.wifi": generate_wifi_icon,
        "com.micropythonos.manage_apps": generate_manage_apps_icon,
        "com.micropythonos.delete_apps": generate_delete_apps_icon,
        "com.micropythonos.update_apps": generate_update_apps_icon,
        "MPOS-QuasiBird": generate_quasi_bird_icon,
        "MPOS-QuasiCalculator": generate_quasi_calculator_icon,
        "MPOS-QuasiNametag": generate_quasi_nametag_icon,
        "MPOS-QuasiDoodle": generate_quasi_doodle_icon,
        "com.micropythonos.retrocore_launcher": generate_retrocore_launcher_icon,
        "com.micropythonos.space_invaders": generate_space_invaders_icon,
        "com.micropythonos.texteditor": generate_texteditor_icon,
        "com.micropythonos.breakout": generate_breakout_icon,
        "com.micropythonos.scan_bluetooth": generate_scan_bluetooth_icon,
        "cz.ucw.pavel.calendar": generate_calendar_icon,
        "cz.ucw.pavel.cellular": generate_cellular_icon,
        "cz.ucw.pavel.columns": generate_columns_icon,
        "cz.ucw.pavel.compass": generate_compass_icon,
        "cz.ucw.pavel.floodit": generate_floodit_icon,
        "cz.ucw.pavel.gyro": generate_gyro_icon,
        "cz.ucw.pavel.navstar": generate_navstar_icon,
        "cz.ucw.pavel.weather": generate_weather_icon,
        "com.micropythonos.dj_addon": generate_dj_addon_icon,
        "com.micropythonos.lights_out": generate_lights_out_icon,
        "com.micropythonos.memory": generate_memory_icon,
    }

    if args.app:
        apps_to_generate = {name: func for name, func in apps.items() if name in args.app}
        if not apps_to_generate:
            print(f"No valid apps found for: {', '.join(args.app)}. Available apps: {', '.join(apps.keys())}")
            return
    else:
        apps_to_generate = apps

    for app_name, generate_func in apps_to_generate.items():
        img = generate_func()
        save_icon(img, app_name, output_base_dir="")

def generate_settings_icon():
    import math
    
    img, draw = create_icon_base()

    background_color = COLORS["silver_gray"]
    background_outline_color = COLORS["light_gray"]
    gear_color = COLORS["dark_blue_gray"]
    gear_outline_color = COLORS["dark_blue_gray"]

    # Gear teeth (16 evenly spaced teeth)
    center_x, center_y = 32, 32  # Center of the 64x64 image
    radius = 14  # Radius of the gear
    inner_radius = 8  # Radius of the inner gear body
    hole_radius = 4
    tooth_width = 6  # Width of each tooth
    tooth_height = 7  # Height of each tooth
    teeth_amount = 9
    border_width = 1

    inner_radius = inner_radius * 2
    hole_radius = hole_radius * 2

    # Big gear with multiple teeth on a circle background
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=background_color, outline=background_outline_color, width=scale_coords(2))
    
    # Gear body (large)
    draw.ellipse(scale_coords([(center_x - inner_radius, center_y - inner_radius),
                               (center_x + inner_radius, center_y + inner_radius)]),
                 fill=gear_color, outline=gear_outline_color, width=2)
    
    # First pass: Draw border spokes
    for i in range(teeth_amount):
        # Calculate angle for each tooth (360 degrees / 16 teeth)
        angle = i * (360 / teeth_amount)
        
        # Convert angle to radians
        angle_rad = math.radians(angle)
        
        # Calculate the outer point of the tooth
        outer_x = center_x + radius * math.cos(angle_rad)
        outer_y = center_y + radius * math.sin(angle_rad)
        
        # Calculate perpendicular points for the tooth
        perp_angle = angle_rad + math.pi/2
        tooth_half_width = tooth_width / 2 + border_width
        
        # Calculate tooth points
        tooth_point1_x = outer_x + tooth_half_width * math.cos(perp_angle)
        tooth_point1_y = outer_y + tooth_half_width * math.sin(perp_angle)
        
        tooth_point2_x = outer_x - tooth_half_width * math.cos(perp_angle)
        tooth_point2_y = outer_y - tooth_half_width * math.sin(perp_angle)
        
        # Extend tooth outward
        tooth_outer_point1_x = tooth_point1_x + (tooth_height + border_width) * math.cos(angle_rad)
        tooth_outer_point1_y = tooth_point1_y + (tooth_height + border_width) * math.sin(angle_rad)
        
        tooth_outer_point2_x = tooth_point2_x + (tooth_height + border_width) * math.cos(angle_rad)
        tooth_outer_point2_y = tooth_point2_y + (tooth_height + border_width) * math.sin(angle_rad)
        
        # Draw border tooth
        draw.polygon(
            scale_coords([
                (tooth_point1_x, tooth_point1_y),
                (tooth_point2_x, tooth_point2_y),
                (tooth_outer_point2_x, tooth_outer_point2_y),
                (tooth_outer_point1_x, tooth_outer_point1_y)
            ]),
            fill=gear_outline_color
        )
    
    # Redraw the central circle to cover the border
    draw.ellipse(scale_coords([(center_x - inner_radius, center_y - inner_radius),
                               (center_x + inner_radius, center_y + inner_radius)]),
                 fill=gear_color, outline=gear_outline_color, width=2)
    
    # Second pass: Draw inner spokes
    for i in range(teeth_amount):
        # Calculate angle for each tooth (360 degrees / 16 teeth)
        angle = i * (360 / teeth_amount)
        
        # Convert angle to radians
        angle_rad = math.radians(angle)
        
        # Calculate the outer point of the tooth
        outer_x = center_x + radius * math.cos(angle_rad)
        outer_y = center_y + radius * math.sin(angle_rad)
        
        # Calculate perpendicular points for the tooth
        perp_angle = angle_rad + math.pi/2
        tooth_half_width = tooth_width / 2
        
        # Calculate tooth points
        tooth_point1_x = outer_x + tooth_half_width * math.cos(perp_angle)
        tooth_point1_y = outer_y + tooth_half_width * math.sin(perp_angle)
        
        tooth_point2_x = outer_x - tooth_half_width * math.cos(perp_angle)
        tooth_point2_y = outer_y - tooth_half_width * math.sin(perp_angle)
        
        # Extend tooth outward
        tooth_outer_point1_x = tooth_point1_x + tooth_height * math.cos(angle_rad)
        tooth_outer_point1_y = tooth_point1_y + tooth_height * math.sin(angle_rad)
        
        tooth_outer_point2_x = tooth_point2_x + tooth_height * math.cos(angle_rad)
        tooth_outer_point2_y = tooth_point2_y + tooth_height * math.sin(angle_rad)
        
        # Draw inner tooth
        draw.polygon(
            scale_coords([
                (tooth_point1_x, tooth_point1_y),
                (tooth_point2_x, tooth_point2_y),
                (tooth_outer_point2_x, tooth_outer_point2_y),
                (tooth_outer_point1_x, tooth_outer_point1_y)
            ]),
            fill=gear_color
        )
    
    # Central hole
    draw.ellipse(scale_coords([(center_x - hole_radius, center_y - hole_radius), (center_x + hole_radius, center_y + hole_radius)]),
                 fill=background_color, outline=gear_outline_color, width=4)
    
    return img

def generate_wifi_icon():
    img, draw = create_icon_base()
    width = 7
    height = 18
    # Circle background
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    
    # Wifi connection arcs
    # Outer arc (weakest signal)
    draw.arc(scale_coords([(3.2, height), (60.8, height - 13.2 + 70.8)]), start=225, end=315, fill=COLORS["bright_blue"], width=scale_coords(width))
    
    # Middle arc (medium signal)
    draw.arc(scale_coords([(15.1, height - 13.2 +25.1), (49.9, height - 13.2 +59.9)]), start=225, end=315, fill=COLORS["bright_blue"], width=scale_coords(width))
   
    # Inner arc (strongest signal)
    draw.arc(scale_coords([(26, height - 13.2 +36), (38, height - 13.2 +48)]), start=225, end=315, fill=COLORS["bright_blue"], width=scale_coords(width))
   
    return img

def generate_howto_icon():
    img, draw = create_icon_base()
    # Circle background
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    
    # Blackboard (green with white lines and symbols) - horizontally centered, big, slightly above vertical center
    board_left = 8
    board_top = 10
    board_right = 56
    board_bottom = 50
    # Dark edge outline
    draw.rounded_rectangle(scale_coords([(board_left, board_top), (board_right, board_bottom)]), radius=4, fill=COLORS["emerald_green"], outline=COLORS["dark_blue_gray"], width=4)
    
    # White text-like blocks on blackboard using loops
    # Adjustable parameters
    text_block_spacing = 2
    text_line_width_1 = 8
    text_line_width_2 = 8
    text_line_width_3 = 10
    
    # Block 1: 3 lines of text on left side
    for line in range(3):
        line_y = board_top + 8 + (line * text_block_spacing)
        draw.line(scale_coords([(board_left + 4, line_y), (board_left + 4 + text_line_width_1, line_y)]), fill=COLORS["white"], width=2)
    
    # Block 2: 4 lines of text in center
    for line in range(4):
        line_y = board_top + 8 + (line * text_block_spacing)
        draw.line(scale_coords([(board_left + 16, line_y), (board_left + 16 + text_line_width_2, line_y)]), fill=COLORS["white"], width=2)
    
    # Block 3: "?" text on right side
    try:
        font = ImageFont.truetype("assets/Archivo-Bold.ttf", scale_coords(36))
        draw.text(scale_coords((board_left + 25, board_top - 0)), "?", font=font, fill=COLORS["white"])
    except:
        # Fallback if font not available
        draw.text(scale_coords((board_left + 30, board_top + 10)), "?", fill=COLORS["white"])
    
    # Teacher figure (dark grey silhouette) - positioned bottom left, partially outside circle
    # Body
    draw.rectangle(scale_coords([(10, 38), (26, 58)]), fill=COLORS["charcoal_gray"])
    # Head
    draw.ellipse(scale_coords([(10, 26), (26, 42)]), fill=COLORS["charcoal_gray"])
    # Left arm
    draw.rectangle(scale_coords([(4, 38), (10, 52)]), fill=COLORS["charcoal_gray"])
    # Right arm (holding stick)
    draw.rectangle(scale_coords([(26, 38), (32, 52)]), fill=COLORS["charcoal_gray"])
    
    # Stick (angled up, held in right hand) - smaller and shorter
    stick_start_x = 28
    stick_start_y = 42
    stick_end_x = 38
    stick_end_y = 29
    stick_width = 2
    # Draw stick as a rotated rectangle (approximated with polygon)
    stick_points = scale_coords([
        (stick_start_x - stick_width, stick_start_y),
        (stick_start_x + stick_width, stick_start_y),
        (stick_end_x + stick_width, stick_end_y),
        (stick_end_x - stick_width, stick_end_y)
    ])
    draw.polygon(stick_points, fill=COLORS["dark_orange"])
    # Stick tip
    draw.ellipse(scale_coords([(stick_end_x - 2, stick_end_y - 2), (stick_end_x + 2, stick_end_y + 2)]), fill=COLORS["dark_orange"])
    
    return img

def generate_manage_apps_icon():
    img, draw = create_icon_base()
    background_color = COLORS["silver_gray"]
    
    # Circle background
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=background_color, outline=COLORS["light_gray"], width=8)
    
    app_colors = [COLORS["light_silver"], COLORS["light_silver"], COLORS["light_silver"], COLORS["light_silver"]]
    app_positions = [
        (18, 12), (34, 12),
        (18, 28), (34, 28),
    ]
    for i, (x, y) in enumerate(app_positions):
        draw.rectangle(scale_coords([(x, y), (x + 12, y + 12)]), fill=app_colors[i])
    

    # 1. Trash can (from generate_delete_apps_icon) - positioned on the left, smaller
    # Lid
    draw.rounded_rectangle(scale_coords([(12, 28), (28, 31)]), radius=2, fill=COLORS["dark_red"])
    draw.rectangle(scale_coords([(17, 25), (23, 28)]), fill=COLORS["dark_red"])
    
    # Body
    draw.polygon(scale_coords([(12, 33), (28, 33), (25, 52), (15, 52)]), fill=COLORS["red_orange"], outline=COLORS["dark_red"], width=4)
    
    # Vertical lines on body
    for x in [17, 20, 23]:
        draw.line(scale_coords([(x, 36), (x, 48)]), fill=COLORS["dark_red"], width=scale_coords(1))

    # 2. Update Arrow (from generate_update_apps_icon) - positioned on the right, smaller
    arrow_color = COLORS["bright_blue"]
    arrow_bottom = 52
    outline_width = 2
    
    # Draw an upload symbol (up arrow)
    draw.rectangle(scale_coords([(40, 38), (48, arrow_bottom)]), fill=arrow_color, outline=background_color, width=scale_coords(outline_width))
    draw.polygon(scale_coords([(35, 37), (53, 37), (44, 26)]), fill=arrow_color)
    draw.rectangle(scale_coords([(41, 36), (47, arrow_bottom-outline_width)]), fill=arrow_color)
    
    return img

def generate_delete_apps_icon():
    img, draw = create_icon_base()
    # Circle background
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    
    # Trash can
    # Lid
    draw.rounded_rectangle(scale_coords([(18, 14), (46, 18)]), radius=2, fill=COLORS["dark_red"])
    draw.rectangle(scale_coords([(28, 10), (36, 14)]), fill=COLORS["dark_red"])
    
    # Body
    draw.polygon(scale_coords([(18, 20), (46, 20), (42, 54), (22, 54)]), fill=COLORS["red_orange"], outline=COLORS["dark_red"], width=4)
    
    # Vertical lines on body
    for x in [26, 32, 38]:
        draw.line(scale_coords([(x, 26), (x, 48)]), fill=COLORS["dark_red"], width=scale_coords(1))
        
    return img

def generate_update_apps_icon():
    img, draw = create_icon_base()
    background_color = COLORS["silver_gray"]
    # background_color = COLORS["charcoal_gray"]
    arrow_color = COLORS["bright_blue"]
    
    # 1. Background: circular style (silver gray with light gray outline)
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=background_color, outline=COLORS["light_gray"], width=8)
    
    # 2. App Squares: four mini square items representing apps (from generate_appstore_icon)
    # app_colors = [COLORS["bright_blue"], COLORS["emerald_green"], COLORS["sun_yellow"], COLORS["amethyst_purple"]]
    
    # "light_silver": "#ECF0F1",
    # "silver_gray": "#BDC3C7",
    app_colors = [COLORS["light_silver"], COLORS["light_silver"], COLORS["light_silver"], COLORS["light_silver"]]
    app_positions = [
        (18, 12), (34, 12),
        (18, 28), (34, 28),
    ]
    for i, (x, y) in enumerate(app_positions):
        draw.rectangle(scale_coords([(x, y), (x + 12, y + 12)]), fill=app_colors[i])
    
    # 3. Arrow: upwards arrow (from generate_osupdate_icon)
    # Positioned to be balanced with the squares
    arrow_bottom = 56
    outline_width = 2
    # Draw an upload symbol (up arrow)
    draw.rectangle(scale_coords([(24, 35), (40, arrow_bottom)]), fill=arrow_color, outline=background_color, width=scale_coords(outline_width))
    draw.polygon(scale_coords([(19, 34), (45, 34), (32, 22)]), fill=arrow_color)
    draw.rectangle(scale_coords([(25, 33), (39, arrow_bottom-outline_width)]), fill=arrow_color)
    
    return img

def generate_retrocore_launcher_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["charcoal_gray"], outline=COLORS["light_gray"], width=8)

    # --- Gamepad body dimensions ---
    bx0, bx1 = 5, 59
    by0, by1 = 16, 48
    body_r = 16
    body_outline = 6

    draw.rounded_rectangle(scale_coords([(bx0, by0), (bx1, by1)]), radius=body_r,
                           fill=COLORS["silver_gray"], outline=COLORS["dark_blue_gray"], width=body_outline)

    # --- D-pad dimensions ---
    dpad_cx, dpad_cy = 18, 30
    dpad_w = 4            # thickness of each arm
    dpad_h = 12           # height of vertical arm
    dpad_arm = 12          # width of horizontal arm
    dpad_color = COLORS["dark_blue_gray"]

    draw.rectangle(scale_coords([(dpad_cx - dpad_w // 2, dpad_cy - dpad_h // 2), (dpad_cx + dpad_w // 2, dpad_cy + dpad_h // 2)]), fill=dpad_color)
    draw.rectangle(scale_coords([(dpad_cx - dpad_arm // 2, dpad_cy - dpad_w // 2), (dpad_cx + dpad_arm // 2, dpad_cy + dpad_w // 2)]), fill=dpad_color)

    # --- Action buttons ---
    btn_r = 3             # button radius
    btn_a_cx, btn_a_cy = 43, 25   # top-right (X / red)
    btn_b_cx, btn_b_cy = 49, 31   # bottom-right (A / yellow)
    knob_outline = 2
    draw.ellipse(scale_coords([(btn_a_cx - btn_r, btn_a_cy - btn_r), (btn_a_cx + btn_r, btn_a_cy + btn_r)]), fill=COLORS["red_orange"],outline=COLORS["dark_blue_gray"], width=knob_outline)
    draw.ellipse(scale_coords([(btn_b_cx - btn_r, btn_b_cy - btn_r), (btn_b_cx + btn_r, btn_b_cy + btn_r)]), fill=COLORS["sun_yellow"],outline=COLORS["dark_blue_gray"], width=knob_outline)

    # --- Start / End / Reset buttons ---
    se_w, se_h = 6, 3     # pill width & height
    se_r = 2
    se_y = 40
    se_gap = 4
    se_color = COLORS["charcoal_gray"]

    start_x = 25
    end_x = start_x + se_w + se_gap

    draw.rounded_rectangle(scale_coords([(start_x, se_y - se_h // 2), (start_x + se_w, se_y + se_h // 2)]), radius=se_r, fill=se_color)
    draw.rounded_rectangle(scale_coords([(end_x, se_y - se_h // 2), (end_x + se_w, se_y + se_h // 2)]), radius=se_r, fill=se_color)

    reset_r = 2           # tiny circle
    reset_cx, reset_cy = 35, 42
    reset_color = COLORS["red_orange"]

    # draw.ellipse(scale_coords([(reset_cx - reset_r, reset_cy - reset_r), (reset_cx + reset_r, reset_cy + reset_r)]), fill=reset_color)
    return img



def generate_space_invaders_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["dark_blue_gray"], outline=COLORS["light_gray"], width=8)
    # Original 1978 space invader on 11 columns, symmetrical
    invader = [
        "..x.....x..",
        "...x...x...",
        "..xxxxxxx..",
        ".xx.xxx.xx.",
        "xxxxxxxxxxx",
        "x.xxxxxxx.x",
        "x.x.....x.x",
        "...xx.xx...",
    ]
    pixel_size = 4
    start_x = 10
    start_y = 14
    for row, line in enumerate(invader):
        for col, char in enumerate(line):
            if char == 'x':
                x = start_x + col * pixel_size
                y = start_y + row * pixel_size
                draw.rectangle(scale_coords([(x, y), (x + pixel_size - 1, y + pixel_size - 1)]), fill=COLORS["emerald_green"])
    return img

def generate_texteditor_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    # Notepad
    draw.rounded_rectangle(scale_coords([(10, 6), (54, 58)]), radius=4, fill=COLORS["white"], outline=COLORS["light_gray"], width=8)
    # Spiral binding
    for x in [16, 24, 32, 40, 48]:
        draw.ellipse(scale_coords([(x - 1, 6), (x + 1, 10)]), fill=COLORS["light_gray"])
    # Text lines
    for y in [20, 28, 36, 44]:
        draw.line(scale_coords([(14, y), (50, y)]), fill=COLORS["light_silver"], width=4)
    # TXT label
    try:
        font = ImageFont.truetype("assets/Archivo-Bold.ttf", scale_coords(14))
        draw.text(scale_coords((16, 10)), "TXT", font=font, fill=COLORS["charcoal_gray"])
    except:
        draw.text(scale_coords((18, 12)), "TXT", fill=COLORS["charcoal_gray"])
    return img



def generate_breakout_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["charcoal_gray"], outline=COLORS["light_gray"], width=8)
    brick_colors = [COLORS["red_orange"], COLORS["sun_yellow"], COLORS["emerald_green"], COLORS["bright_blue"]]
    # Bricks
    for row in range(4):
        for col in range(5):
            x = 8 + col * 10
            y = 8 + row * 6
            draw.rectangle(scale_coords([(x, y), (x + 8, y + 4)]), fill=brick_colors[row], outline=COLORS["charcoal_gray"], width=2)
    # Paddle
    draw.rounded_rectangle(scale_coords([(20, 50), (44, 54)]), radius=4, fill=COLORS["white"])
    # Ball
    draw.ellipse(scale_coords([(34, 44), (38, 48)]), fill=COLORS["white"])
    return img

def generate_scan_bluetooth_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    # Bluetooth symbol matching SVG path, scaled 0.8 around center, line 2x thicker
    points = scale_coords([(20, 20), (44, 44), (32, 54), (32, 10), (44, 20), (20, 44)])
    draw.line(points, fill=COLORS["bright_blue"], width=16, joint="curve")
    # Scanning arcs on the right
    # draw.arc(scale_coords([(44, 34), (60, 50)]), start=0, end=180, fill=COLORS["emerald_green"], width=4)
    # draw.arc(scale_coords([(40, 38), (56, 54)]), start=0, end=180, fill=COLORS["emerald_green"], width=4)
    return img

def generate_calendar_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    # Calendar page
    draw.rounded_rectangle(scale_coords([(10, 12), (54, 52)]), radius=4, fill=COLORS["white"], outline=COLORS["light_gray"], width=8)
    # Calendar header
    draw.rounded_rectangle(scale_coords([(10, 12), (54, 24)]), radius=4, fill=COLORS["red_orange"])
    # Date
    try:
        font = ImageFont.truetype("assets/Archivo-Bold.ttf", scale_coords(24))
        draw.text(scale_coords((20, 26)), "17", font=font, fill=COLORS["dark_blue_gray"])
    except:
        draw.rectangle(scale_coords([(22, 30), (42, 44)]), fill=COLORS["dark_blue_gray"])
    return img

def generate_cellular_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)

    # --- Tower dimensions ---
    cx = 32
    tw = 24            # tower width at bottom
    top_y, bot_y = 18, 54
    leg_w = 6          # outer leg line width
    beam_w = 6         # cross beam line width
    x_w = 6            # X-bracing line width
    post_w = 10         # antenna post line width

    # Outer legs
    draw.line(scale_coords([(cx - tw // 2, bot_y), (cx, top_y)]), fill=COLORS["charcoal_gray"], width=leg_w)
    draw.line(scale_coords([(cx + tw // 2, bot_y), (cx, top_y)]), fill=COLORS["charcoal_gray"], width=leg_w)

    # Horizontal cross beams — wider at bottom, narrower at top
    beam_ys = [20, 28, 36, 44]
    for y in beam_ys:
        spread = int((y - top_y) * (tw / 2 / (bot_y - top_y)))
        draw.line(scale_coords([(cx - spread, y), (cx + spread, y)]), fill=COLORS["charcoal_gray"], width=beam_w)

    # Inner X cross-bracing
    for y0, y1 in [(20, 28), (28, 36), (36, 44)]:
        s0 = int((y0 - top_y) * (tw / 2 / (bot_y - top_y)))
        s1 = int((y1 - top_y) * (tw / 2 / (bot_y - top_y)))
        draw.line(scale_coords([(cx - s0, y0), (cx + s1, y1)]), fill=COLORS["charcoal_gray"], width=x_w)
        draw.line(scale_coords([(cx + s0, y0), (cx - s1, y1)]), fill=COLORS["charcoal_gray"], width=x_w)

    # Antenna post at top
    draw.line(scale_coords([(cx, top_y), (cx, top_y - 6)]), fill=COLORS["charcoal_gray"], width=post_w)

    # --- Signal wave arcs ---
    wave_color = COLORS["bright_blue"]
    wave_w = 8         # arc line width
    wave_step = 3      # gap between consecutive arcs
    wave_start_r = 6   # radius of innermost arc

    for i in range(4):
        r = wave_start_r + i * wave_step
        # Right: bottom-right quarter centered at (cx, top_y)
        draw.arc(scale_coords([(cx, top_y - r), (cx + r, top_y)]), start=270, end=360, fill=wave_color, width=wave_w)
        # Left: bottom-left quarter centered at (cx, top_y)
        draw.arc(scale_coords([(cx - r, top_y - r), (cx, top_y)]), start=180, end=270, fill=wave_color, width=wave_w)
    return img

def generate_columns_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["charcoal_gray"], outline=COLORS["light_gray"], width=8)

    # --- Grid & block dimensions ---
    cols = 5
    rows = 6
    cell = 6            # block cell size
    gap = 2             # gap between cells
    corner_r = 1        # block corner radius
    colors = [COLORS["bright_blue"], COLORS["emerald_green"], COLORS["red_orange"], COLORS["sun_yellow"]]

    # Compute board origin to center in 64x64
    board_w = cols * cell + (cols - 1) * gap
    board_h = rows * cell + (rows - 1) * gap
    board_x0 = (48 - board_w) // 2
    board_y0 = (64 - board_h) // 2

    import random
    random.seed(6)

    def draw_block(col, row, color):
        x = board_x0 + col * (cell + gap)
        y = board_y0 + row * (cell + gap)
        draw.rounded_rectangle(scale_coords([(x, y), (x + cell, y + cell)]), radius=corner_r, fill=color, outline=COLORS["light_gray"], width=1)

    # --- Settled I-pieces (1x3 vertical) at the bottom, random colors ---
    settled = [
        (0, rows - 1),
        (1, rows - 1),
        (2, rows - 2),
        (4, rows - 1),
        (5, rows - 1),
        (6, rows - 2),
    ]
    for col, bottom_row in settled:
        for r in range(3):
            ci = random.randrange(len(colors))
            draw_block(col, bottom_row - 2 + r, colors[ci])

    # --- Falling I-piece (1x3 vertical) in the air, random color ---
    fall_col = 3
    fall_top = 0
    fc = random.randrange(len(colors))
    for r in range(3):
        draw_block(fall_col, fall_top + r, colors[fc])
    return img

def generate_compass_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    # Compass face
    draw.ellipse(scale_coords([(10, 10), (54, 54)]), fill=COLORS["light_gray"], outline=COLORS["charcoal_gray"], width=8)
    # draw.ellipse(scale_coords([(10, 10), (54, 54)]), fill=COLORS["charcoal_gray"], outline=COLORS["charcoal_gray"], width=8)
    # Needle (north = red, south = light)
    draw.polygon(scale_coords([(32, 14), (36, 32), (32, 30), (28, 32)]), fill=COLORS["red_orange"])
    # draw.polygon(scale_coords([(32, 50), (36, 32), (32, 34), (28, 32)]), fill=COLORS["light_silver"])
    draw.polygon(scale_coords([(32, 50), (36, 32), (32, 34), (28, 32)]), fill=COLORS["charcoal_gray"])
    # N dot
    # draw.ellipse(scale_coords([(30, 12), (34, 16)]), fill=COLORS["red_orange"])
    return img

def generate_floodit_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    colors = [COLORS["red_orange"], COLORS["sun_yellow"], COLORS["emerald_green"], COLORS["bright_blue"], COLORS["amethyst_purple"]]
    import random
    random.seed(123)
    for row in range(5):
        for col in range(5):
            x = 10 + col * 9
            y = 10 + row * 9
            draw.rectangle(scale_coords([(x, y), (x + 7, y + 7)]), fill=random.choice(colors))
    return img

def generate_gyro_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)

    RENDER_SIZE = 256
    x_color = COLORS["sun_yellow"]
    y_color = COLORS["bright_blue"]
    z_color = COLORS["red_orange"]
    width = 2

    # Draw x_color ellipse directly (no rotation)
    draw.ellipse(scale_coords([(20, 10), (44, 54)]), outline=x_color, width=scale_coords(width))

    # Create temporary image for y_color ellipse, rotate, and paste
    y_ellipse_img = Image.new('RGBA', (RENDER_SIZE, RENDER_SIZE), (0, 0, 0, 0))
    y_ellipse_draw = ImageDraw.Draw(y_ellipse_img)
    y_ellipse_draw.ellipse(scale_coords([(12, 22), (52, 42)]), outline=y_color, width=scale_coords(width))
    y_ellipse_rotated = y_ellipse_img.rotate(30, center=(RENDER_SIZE/2, RENDER_SIZE/2), expand=False)
    img.paste(y_ellipse_rotated, (0, 0), y_ellipse_rotated)

    # Create temporary image for z_color ellipse, rotate, and paste
    z_ellipse_img = Image.new('RGBA', (RENDER_SIZE, RENDER_SIZE), (0, 0, 0, 0))
    z_ellipse_draw = ImageDraw.Draw(z_ellipse_img)
    z_ellipse_draw.ellipse(scale_coords([(14, 22), (50, 42)]), outline=z_color, width=scale_coords(width))
    z_ellipse_rotated = z_ellipse_img.rotate(-30, center=(RENDER_SIZE/2, RENDER_SIZE/2), expand=False)
    img.paste(z_ellipse_rotated, (0, 0), z_ellipse_rotated)
    return img

def generate_navstar_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["dark_blue_gray"], outline=COLORS["light_gray"], width=8)

    # Solar panels (large rectangles on left & right)
    panel_w, panel_h = 14, 28
    panel_y0, panel_y1 = 18, 46
    panel_color = COLORS["bright_blue"]
    panel_outline = COLORS["charcoal_gray"]

    draw.rectangle(scale_coords([(4, panel_y0), (4 + panel_w, panel_y1)]), fill=panel_color, outline=panel_outline, width=2)
    draw.rectangle(scale_coords([(60 - panel_w, panel_y0), (60, panel_y1)]), fill=panel_color, outline=panel_outline, width=2)

    # Panel grid lines (solar cell segmentation)
    for y in range(panel_y0 + 4, panel_y1, 4):
        draw.line(scale_coords([(6, y), (4 + panel_w - 1, y)]), fill=panel_outline, width=1)
        draw.line(scale_coords([(60 - panel_w + 1, y), (58, y)]), fill=panel_outline, width=1)

    # Connecting struts from body to panels
    strut_y0, strut_y1 = 28, 36
    draw.rectangle(scale_coords([(4 + panel_w, strut_y0), (22, strut_y1)]), fill=COLORS["light_gray"])
    draw.rectangle(scale_coords([(42, strut_y0), (60 - panel_w, strut_y1)]), fill=COLORS["light_gray"])

    # Satellite central body
    body_x0, body_x1 = 22, 42
    body_y0, body_y1 = 22, 42
    draw.rounded_rectangle(scale_coords([(body_x0, body_y0), (body_x1, body_y1)]), radius=4,
                           fill=COLORS["light_gray"], outline=COLORS["charcoal_gray"], width=4)

    # Antenna dish on top of body
    dish_cx, dish_cy = 32, 14
    dish_r = 8
    draw.arc(scale_coords([(dish_cx - dish_r, dish_cy - dish_r), (dish_cx + dish_r, dish_cy + dish_r)]),
             start=0, end=180, fill=COLORS["light_gray"], width=3)
    draw.line(scale_coords([(dish_cx, dish_cy), (dish_cx, dish_cy + 4)]), fill=COLORS["light_gray"], width=3)
    draw.line(scale_coords([(dish_cx - dish_r + 2, dish_cy), (dish_cx + dish_r - 2, dish_cy)]), fill=COLORS["light_gray"], width=2)
    return img

def generate_weather_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)

    import math

    # Bigger sun with rays (behind cloud)
    sun_cx, sun_cy = 44, 22
    sun_r = 12
    draw.ellipse(scale_coords([(sun_cx - sun_r, sun_cy - sun_r), (sun_cx + sun_r, sun_cy + sun_r)]), fill=COLORS["sun_yellow"])
    for angle in range(0, 360, 45):
        a = math.radians(angle)
        x1 = sun_cx + (sun_r + 2) * math.cos(a)
        y1 = sun_cy + (sun_r + 2) * math.sin(a)
        x2 = sun_cx + (sun_r + 9) * math.cos(a)
        y2 = sun_cy + (sun_r + 9) * math.sin(a)
        draw.line(scale_coords([(x1, y1), (x2, y2)]), fill=COLORS["sun_yellow"], width=12)

    # Bigger cloud (in front of sun)
    draw.ellipse(scale_coords([(11, 27), (33, 49)]), fill=COLORS["charcoal_gray"])
    draw.ellipse(scale_coords([(25, 21), (47, 43)]), fill=COLORS["charcoal_gray"])
    draw.ellipse(scale_coords([(35, 29), (53, 47)]), fill=COLORS["charcoal_gray"])

    # Thermometer with adjustable variables
    bulb_w = 16
    bulb_h = 16
    stem_w = 12
    stem_h = 32
    outline = 2
    percentage = 50  # how high red mercury reaches (0-100)

    cx = 15
    bulb_bottom = 58
    bulb_top = bulb_bottom - bulb_h
    bulb_mid_y = bulb_top + bulb_h // 2
    stem_top = bulb_mid_y - stem_h

    # Back body (light silver)
    draw.ellipse(scale_coords([(cx - bulb_w // 2, bulb_top), (cx + bulb_w // 2, bulb_bottom)]), fill=COLORS["light_silver"])
    draw.ellipse(scale_coords([(cx - stem_w // 2, stem_top - stem_w // 2), (cx + stem_w // 2, stem_top + stem_w // 2)]), fill=COLORS["light_silver"])
    draw.rectangle(scale_coords([(cx - stem_w // 2, stem_top), (cx + stem_w // 2, bulb_mid_y)]), fill=COLORS["light_silver"])
    draw.ellipse(scale_coords([(cx - bulb_w // 2, bulb_top), (cx + bulb_w // 2, bulb_bottom)]), fill=COLORS["light_silver"])

    # Red fill (smaller by outline on all sides, creating border)
    red_bulb_w = bulb_w - outline * 2
    red_bulb_h = bulb_h - outline * 2
    red_stem_w = stem_w - outline * 2

    red_bulb_top = bulb_top + outline
    red_bulb_bottom = bulb_bottom - outline
    red_bulb_mid_y = red_bulb_top + red_bulb_h // 2

    # Red bulb
    draw.ellipse(scale_coords([(cx - red_bulb_w // 2, red_bulb_top), (cx + red_bulb_w // 2, red_bulb_bottom)]), fill=COLORS["red_orange"])

    # Red stem height based on percentage
    red_stem_total = red_bulb_mid_y - stem_top - outline
    red_fill = int(red_stem_total * percentage / 100)
    red_rect_top = red_bulb_mid_y - red_fill

    if red_rect_top >= stem_top + outline:
        draw.rounded_rectangle(scale_coords([(cx - red_stem_w // 2, red_rect_top), (cx + red_stem_w // 2, red_bulb_mid_y)]), radius=4, fill=COLORS["red_orange"])

    return img

def generate_dj_addon_icon():
    img, draw = create_icon_base()
    # draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["charcoal_gray"], outline=COLORS["light_gray"], width=8)

    # --- Controller body dimensions ---
    bx0, bx1 = 4, 60
    by0, by1 = 16, 48
    body_r = 4
    body_w = body_outline = 4

    draw.rounded_rectangle(scale_coords([(bx0, by0), (bx1, by1)]), radius=body_r,
                        #    fill=COLORS["charcoal_gray"], outline=COLORS["dark_blue_gray"], width=body_outline)
                           fill=COLORS["silver_gray"], outline=COLORS["dark_blue_gray"], width=body_outline)

    cx = (bx0 + bx1) // 2  # 32

    # --- Knob dimensions ---
    knob_size = 4  # width & height
    knob_outline = 2
    # knob_colors = (COLORS["light_gray"], COLORS["silver_gray"])
    knob_colors = (COLORS["light_gray"], COLORS["charcoal_gray"])

    # --- Knob x positions ---
    left_knob_x0, left_knob_x1 = 8, 8 + knob_size
    right_knob_x0, right_knob_x1 = 52, 52 + knob_size

    # --- Knob row y positions ---
    knob_rows = [19, 29, 39]

    for y in knob_rows:
        for kx0, kx1 in [(left_knob_x0, left_knob_x1), (right_knob_x0, right_knob_x1)]:
            draw.ellipse(scale_coords([(kx0, y), (kx1, y + knob_size)]),
                         fill=knob_colors[0], outline=knob_colors[1], width=knob_outline)

    # --- Fader dimensions ---
    fader_x_l = 16
    fader_x_r = 48
    fader_top, fader_bot = by0 +4 , by1 -4
    fader_line_w = 3
    fader_handle_w = 4
    fader_handle_h = 4
    fader_handle_r = 1
    fader_color = COLORS["emerald_green"]

    draw.line(scale_coords([(fader_x_l, fader_top), (fader_x_l, fader_bot)]), fill=COLORS["charcoal_gray"], width=fader_line_w)
    draw.line(scale_coords([(fader_x_r, fader_top), (fader_x_r, fader_bot)]), fill=COLORS["charcoal_gray"], width=fader_line_w)

    # Left fader handle
    l_fh_x0 = fader_x_l - fader_handle_w // 2
    l_fh_x1 = l_fh_x0 + fader_handle_w
    draw.rounded_rectangle(scale_coords([(l_fh_x0, 30), (l_fh_x1, 30 + fader_handle_h)]),
                           radius=fader_handle_r, fill=fader_color)

    # Right fader handle
    r_fh_x0 = fader_x_r - fader_handle_w // 2
    r_fh_x1 = r_fh_x0 + fader_handle_w
    draw.rounded_rectangle(scale_coords([(r_fh_x0, 22), (r_fh_x1, 22 + fader_handle_h)]),
                           radius=fader_handle_r, fill=fader_color)

    # --- Pad grid dimensions ---
    pad_w = 6
    pad_h = 6
    pad_r = 2
    pad_rows = [23, 33]
    pad_cols = [cx - 12, cx - 6, cx + 0, cx + 6]  # 25, 29, 33, 37
    pad_color = COLORS["bright_blue"]

    for px in pad_cols:
        for py in pad_rows:
            draw.rounded_rectangle(scale_coords([(px, py), (px + pad_w - 1, py + pad_h - 1)]),
                                   radius=pad_r, fill=pad_color)

    # --- Crossfader dimensions ---
    cf_y = by1 -4
    cf_x0, cf_x1 = 20, 44
    cf_line_w = 3
    cf_handle_w = 4
    cf_handle_h = 4
    cf_handle_r = 1
    cf_color = COLORS["sun_yellow"]

    draw.line(scale_coords([(cf_x0, cf_y), (cf_x1, cf_y)]), fill=COLORS["charcoal_gray"], width=cf_line_w)
    cf_hx0 = cx - cf_handle_w // 2
    draw.rounded_rectangle(scale_coords([(cf_hx0, cf_y - cf_handle_h // 2), (cf_hx0 + cf_handle_w, cf_y + cf_handle_h // 2)]),
                           radius=cf_handle_r, fill=cf_color)

    
    # # --- Headphone (center-top) ---
    # hp_color = COLORS["silver_gray"]
    # hp_color = COLORS["sun_yellow"]
    # hp_band_box = [24, 1, 40, 18]
    # hp_cup_w, hp_cup_h = 5, 8
    # hp_cup_y0, hp_cup_y1 = 8, 16

    # draw.arc(scale_coords(hp_band_box), start=180, end=0, fill=hp_color, width=12)
    # draw.ellipse(scale_coords([(hp_band_box[0] - hp_cup_w // 2, hp_cup_y0), (hp_band_box[0] + hp_cup_w // 2, hp_cup_y1)]), fill=hp_color)
    # draw.ellipse(scale_coords([(hp_band_box[2] - hp_cup_w // 2, hp_cup_y0), (hp_band_box[2] + hp_cup_w // 2, hp_cup_y1)]), fill=hp_color)
    
    
    # # --- Music notes (above controller) ---
    # note_y = 54
    # note_x = 36
    # note_size = 11
    # note_thick = 3
    # second_note_x_offset = 18
    # second_note_y_offset = -3
    # note_height = 30
    # note_color = COLORS["dark_red"]
    # # Background
    # note_shape = scale_coords([(note_x, note_y), (note_x, note_height), (note_x+second_note_x_offset, note_height + second_note_y_offset),(note_x+second_note_x_offset, note_y + second_note_y_offset)])
    # # Note line all in one
    # draw.polygon(note_shape,  outline=note_color, width=scale_coords(note_thick))
    # # Erase bottom part
    # draw.rectangle(scale_coords([(note_x+note_thick, note_y+second_note_y_offset-note_thick), (note_x+second_note_x_offset-note_thick, note_y)]), fill=COLORS["silver_gray"])
    

    # # Main music note shape
    # draw.ellipse(scale_coords([(note_x-note_size+note_thick, note_y-note_size+(note_size/2)), (note_x+note_thick, note_y+(note_size/2))]), fill=note_color)
    # # Second note
    # draw.ellipse(scale_coords([(note_x-note_size + second_note_x_offset, note_y-note_size+second_note_y_offset+(note_size/2)), (note_x+ second_note_x_offset, note_y+second_note_y_offset+(note_size/2))]), fill=note_color)
    
    return img

def generate_lights_out_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    import random
    random.seed(7)
    for row in range(3):
        for col in range(3):
            x = 8 + col * 18
            y = 8 + row * 18
            color = random.choice([COLORS["sun_yellow"], COLORS["sun_yellow"], COLORS["dark_blue_gray"], COLORS["dark_blue_gray"], COLORS["dark_blue_gray"]])
            draw.rectangle(scale_coords([(x, y), (x + 14, y + 14)]), fill=color, outline=COLORS["charcoal_gray"], width=2)
    return img

def generate_memory_icon():
    img, draw = create_icon_base()
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)

    # --- Grid dimensions ---
    cols, rows = 4, 2
    card_w = 13        # card outer width
    card_h = 13        # card outer height
    card_r = 10         # card corner radius
    gap_x = 2          # horizontal gap between cards
    gap_y = 2          # vertical gap between rows
    outline_w = 1     # card outline width
    inset = 0        # inner color inset from card edge
    inner_r = 0        # inner color square corner radius

    # --- Colors ---
    bg_color = COLORS["white"]
    outline_color = COLORS["charcoal_gray"]
    # 4 pairs: 2 blue, 1 green, 1 red
    pair_colors = [COLORS["bright_blue"]] * 4 + [COLORS["emerald_green"]] * 2 + [COLORS["red_orange"]] * 2

    import random
    random.seed(1)
    random.shuffle(pair_colors)

    # --- Compute grid origin to center in 64x64 ---
    total_w = cols * card_w + (cols - 1) * gap_x
    total_h = rows * card_h + (rows - 1) * gap_y
    origin_x = (64 - total_w) // 2
    origin_y = (64 - total_h) // 2

    for row in range(rows):
        for col in range(cols):
            x = origin_x + col * (card_w + gap_x)
            y = origin_y + row * (card_h + gap_y)
            color = pair_colors[row * cols + col]
            # draw.rounded_rectangle(scale_coords([(x, y), (x + card_w, y + card_h)]),
            #                        radius=card_r, fill=bg_color, outline=outline_color, width=outline_w)
            draw.rounded_rectangle(scale_coords([(x, y), (x + card_w, y + card_h)]),
                                   radius=card_r, fill=color, outline=outline_color, width=outline_w)
            # draw.rounded_rectangle(scale_coords([(x + inset, y + inset), (x + card_w - inset, y + card_h - inset)]),
            #                        radius=inner_r, fill=color)
    return img

if __name__ == "__main__":
    main()
