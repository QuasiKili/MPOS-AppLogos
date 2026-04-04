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

if __name__ == "__main__":
    main()
