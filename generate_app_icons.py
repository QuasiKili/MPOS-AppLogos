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
    # draw.rectangle(scale_coords([(4, 4), (60, 60)]), fill=COLORS["bright_blue"])
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
    # Circle background
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    
    # Circle canvas
    draw.ellipse(scale_coords([(10, 10), (50, 50)]), fill=COLORS["white"], outline=COLORS["silver_gray"], width=8)
    
    # Squiggly line being drawn
    draw.arc(scale_coords([(15, 20), (45, 40)]), start=0, end=180, fill=COLORS["bright_blue"], width=16)
    draw.arc(scale_coords([(15, 30), (45, 50)]), start=180, end=0, fill=COLORS["red_orange"], width=16)
    
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
    
    # Tree view representation
    # Trunk/main line
    draw.rectangle(scale_coords([(30, 10), (34, 50)]), fill=COLORS["dark_blue_gray"], width=8)
    
    # Branches
    # Left branch
    draw.line(scale_coords([(30, 20), (20, 30)]), fill=COLORS["dark_blue_gray"], width=8)
    # Right branch
    draw.line(scale_coords([(30, 30), (40, 40)]), fill=COLORS["dark_blue_gray"], width=8)
    
    # Another left branch
    draw.line(scale_coords([(30, 40), (15, 50)]), fill=COLORS["dark_blue_gray"], width=8)
    # Another right branch
    draw.line(scale_coords([(30, 40), (45, 50)]), fill=COLORS["dark_blue_gray"], width=8)
    
    # Folder/file indicators at branch ends
    # Left side
    draw.rectangle(scale_coords([(12, 46), (18, 52)]), fill=COLORS["sun_yellow"], outline=COLORS["dark_orange"], width=4)
    draw.rectangle(scale_coords([(15, 48), (21, 54)]), fill=COLORS["light_silver"], outline=COLORS["silver_gray"], width=4)
    
    # Right side
    draw.rectangle(scale_coords([(42, 46), (48, 52)]), fill=COLORS["sun_yellow"], outline=COLORS["dark_orange"], width=4)
    draw.rectangle(scale_coords([(45, 48), (51, 54)]), fill=COLORS["light_silver"], outline=COLORS["silver_gray"], width=4)
    
    return img

def generate_helloworld_icon():
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

def generate_imageview_icon():
    img, draw = create_icon_base()
    # Mountain landscape
    draw.rounded_rectangle([scale_coords((4, 4)), scale_coords((60, 60))], fill=COLORS["bright_blue"], radius=scale_coords(4))
    # draw.rectangle([(0, 0), (RENDER_SIZE, RENDER_SIZE)], fill=COLORS["bright_blue"])
    # draw.polygon(scale_coords([(6, 40), (32, 15), (58, 40), (58, 58), (6, 58)]), fill=COLORS["emerald_green"])
    draw.rounded_rectangle([scale_coords((4, 40)), scale_coords((60, 60))], fill=COLORS["emerald_green"], radius=scale_coords(4))
    # house
    # draw.polygon(scale_coords([(14, 35), (24, 25), (34, 35), (34, 48), (14, 48)]), fill=COLORS["dark_blue_gray"])
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
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    draw.ellipse(scale_coords([(15, 25), (49, 39)]), outline=z_color, width=scale_coords(4) )
    draw.ellipse(scale_coords([(10, 20), (54, 44)]), outline=y_color, width=scale_coords(4) )
    draw.ellipse(scale_coords([(20, 10), (44, 54)]), outline=x_color, width=scale_coords(4) )
    
    
    # # Central circle (main body)
    # draw.ellipse(scale_coords([(12, 12), (52, 52)]), fill=COLORS["dark_blue_gray"])
    # # Inner circle (representing sensor)
    # draw.ellipse(scale_coords([(20, 20), (44, 44)]), fill=COLORS["charcoal_gray"])
    # # Small central dot (indicator)
    # draw.ellipse(scale_coords([(29, 29), (35, 35)]), fill=COLORS["bright_blue"])
    # Horizontal and vertical bars (axes)
    # draw.rectangle(scale_coords([(10, 30), (54, 34)]), fill=COLORS["light_gray"])
    # draw.rectangle(scale_coords([(30, 10), (34, 54)]), fill=COLORS["light_gray"])
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
    # draw.rectangle(scale_coords([(note_x+note_size-note_thick, note_height), (note_x+note_size, note_y-(note_size/2))]), fill=COLORS["red_orange"])
    # Second note
    draw.ellipse(scale_coords([(note_x-note_size + second_note_x_offset, note_y-note_size+second_note_y_offset+(note_size/2)), (note_x+ second_note_x_offset, note_y+second_note_y_offset+(note_size/2))]), fill=note_color)
    # draw.rectangle(scale_coords([(note_x+note_size-note_thick+ second_note_x_offset, note_height+second_note_y_offset), (note_x+note_size+ second_note_x_offset, note_y-(note_size/2)+second_note_y_offset)]), fill=COLORS["red_orange"])
    # Connection
    # draw.line(([scale_coords((note_x+note_size-note_thick+ second_note_x_offset+3, note_height+second_note_y_offset)),scale_coords((note_x+note_size-3, note_height))]), fill=COLORS["red_orange"], width=scale_coords(3) )



    # draw.arc(scale_coords([(35, 13), (48, 28)]), start=270, end=90, fill=COLORS["red_orange"], width=2)
    
    # Play button triangle (integrated)
    # draw.polygon(scale_coords([(25, 25), (40, 32), (25, 39)]), fill=COLORS["white"])
    return img

def generate_nostr_icon():
    img, draw = create_icon_base()
    # Stylized "N" using shapes
    draw.line(scale_coords([(15, 50), (15, 10)]), fill=COLORS["sun_yellow"], width=32)
    draw.line(scale_coords([(15, 10), (45, 50)]), fill=COLORS["sun_yellow"], width=32)
    draw.line(scale_coords([(45, 50), (45, 10)]), fill=COLORS["sun_yellow"], width=32)
    # Speech bubble/connection lines
    draw.line(scale_coords([(10, 50), (25, 35)]), fill=COLORS["bright_blue"], width=8)
    draw.line(scale_coords([(35, 35), (50, 50)]), fill=COLORS["bright_blue"], width=8)
    return img

def generate_showbattery_icon():
    img, draw = create_icon_base()
    # Battery body
    draw.rounded_rectangle(scale_coords([(15, 20), (49, 44)]), radius=16, outline=COLORS["dark_blue_gray"], width=8)
    draw.rectangle(scale_coords([(49, 28), (52, 36)]), fill=COLORS["dark_blue_gray"])
    # Battery level (green)
    draw.rectangle(scale_coords([(17, 22), (47, 42)]), fill=COLORS["emerald_green"])
    return img

def generate_showfonts_icon():
    img, draw = create_icon_base()
    # A
    draw.polygon(scale_coords([(10, 40), (20, 10), (30, 40)]), fill=COLORS["red_orange"], outline=COLORS["dark_red"], width=8)
    draw.line(scale_coords([(15, 30), (25, 30)]), fill=COLORS["red_orange"], width=8)
    # a
    draw.ellipse(scale_coords([(35, 25), (45, 35)]), fill=COLORS["bright_blue"], outline=COLORS["steel_blue"], width=8)
    draw.line(scale_coords([(45, 28), (45, 40)]), fill=COLORS["bright_blue"], width=8)
    # Ruler/underline
    draw.line(scale_coords([(10, 50), (54, 50)]), fill=COLORS["dark_blue_gray"], width=8)
    draw.line(scale_coords([(10, 52), (54, 52)]), fill=COLORS["dark_blue_gray"], width=4)
    return img

def generate_soundrecorder_icon():
    img, draw = create_icon_base()
    # Microphone
    draw.ellipse(scale_coords([(25, 15), (39, 30)]), fill=COLORS["light_gray"], outline=COLORS["silver_gray"], width=8)
    draw.rectangle(scale_coords([(30, 30), (34, 45)]), fill=COLORS["light_gray"], outline=COLORS["silver_gray"], width=8)
    draw.rectangle(scale_coords([(28, 45), (36, 48)]), fill=COLORS["light_gray"], outline=COLORS["silver_gray"], width=8)
    # Sound waves
    draw.arc(scale_coords([(40, 20), (50, 30)]), start=90, end=270, fill=COLORS["bright_blue"], width=8)
    draw.arc(scale_coords([(42, 18), (52, 32)]), start=90, end=270, fill=COLORS["bright_blue"], width=8)
    return img

def generate_about_icon():
    img, draw = create_icon_base()
    # draw.rounded_rectangle(scale_coords([(5, 5), (59, 59)]), radius=32, fill=COLORS["white"])
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
        # draw.text(scale_coords((29, 19)), "i", font=font, fill=COLORS["white"])
        draw.rectangle(scale_coords([(30, 29), (34, 41)]), fill=COLORS["white"])
        draw.ellipse(scale_coords([(30, 22), (34, 26)]), fill=COLORS["white"])
        
    except FileNotFoundError:
        print("Error: MicroPythonOS-logo-symbol-black-short64.png not found in assets directory.")
        draw.text(scale_coords((10, 20)), "About", fill=COLORS["black"])
    return img

def generate_appstore_icon():
    img, draw = create_icon_base()
    # draw.ellipse(scale_coords([(4, 4), (60,60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    draw.ellipse(scale_coords([(4, 4), (60,60)]), fill=COLORS["charcoal_gray"], outline=COLORS["silver_gray"], width=8)
    # Draw a rounded rectangle as the base
    # draw.rounded_rectangle(scale_coords([(5, 5), (59, 59)]), radius=32, fill=COLORS["light_silver"], outline=COLORS["silver_gray"], width=8)
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
    draw.polygon(scale_coords([(20, 52), (44, 52), (32, 62)]), fill=COLORS["red_orange"], outline=COLORS["charcoal_gray"])
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
        "com.micropythonos.settings": generate_settings_icon,
        "com.micropythonos.wifi": generate_wifi_icon,
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
    gear_color = COLORS["charcoal_gray"]
    gear_outline_color = COLORS["black"]

    # Gear teeth (16 evenly spaced teeth)
    center_x, center_y = 32, 32  # Center of the 64x64 image
    radius = 14  # Radius of the gear
    inner_radius = 9  # Radius of the inner gear body
    hole_radius = 4
    tooth_width = 6  # Width of each tooth
    tooth_height = 7  # Height of each tooth
    teeth_amount = 12
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
    # Circle background
    draw.ellipse(scale_coords([(4, 4), (60, 60)]), fill=COLORS["silver_gray"], outline=COLORS["light_gray"], width=8)
    
    # Wifi connection arcs
    # Outer arc (weakest signal)
    draw.arc(scale_coords([(12, 22), (52, 62)]), start=225, end=315, fill=COLORS["bright_blue"], width=20)
    
    # Middle arc (medium signal)
    draw.arc(scale_coords([(20, 30), (44, 54)]), start=225, end=315, fill=COLORS["bright_blue"], width=20)
   
    # Inner arc (strongest signal)
    draw.arc(scale_coords([(28, 38), (36, 46)]), start=225, end=315, fill=COLORS["bright_blue"], width=20)
   
    return img

if __name__ == "__main__":
    main()