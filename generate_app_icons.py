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

def create_icon_base():
    """Creates a new 64x64 RGBA image with a transparent background."""
    img = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    return img, draw

def save_icon(img, app_name, output_base_dir=""):
    """Saves the generated icon to the specified path within the app's directory structure."""
    # output_dir = os.path.join(output_base_dir, app_name, 'res', 'mipmap-mdpi')
    output_dir = os.path.join(output_base_dir, app_name)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'icon_64x64.png')
    img.save(output_path, 'PNG', optimize=True)
    print(f"Icon saved for {app_name}: {output_path}")

def generate_quasi_bird_icon():
    img, draw = create_icon_base()
    # Draw bird body (yellow circle)
    # Draw bird body (yellow circle) - scaled up and centered
    draw.ellipse([(10, 15), (50, 55)], fill=COLORS["sun_yellow"], outline=COLORS["dark_orange"], width=3)
    # Draw wing - adjusted for new body size and position
    draw.ellipse([(15, 35), (40, 50)], fill=COLORS["dark_orange"], outline=COLORS["red_orange"], width=2)
    # Draw eye - adjusted for new body size and position
    draw.ellipse([(32, 22), (42, 32)], fill=COLORS["white"], outline=COLORS["black"], width=2)
    draw.ellipse([(35, 25), (39, 29)], fill=COLORS["black"])
    # Draw beak - adjusted for new body size and position
    beak = [(44, 34), (56, 34), (49, 40)]
    draw.polygon(beak, fill=COLORS["dark_orange"], outline=COLORS["red_orange"], width=1)
    beak = [(44, 34), (56, 34), (49, 28)]
    draw.polygon(beak, fill=COLORS["dark_orange"], outline=COLORS["red_orange"], width=1)
    return img

def generate_quasi_calculator_icon():
    img, draw = create_icon_base()
    # Draw calculator body (rounded rectangle)
    draw.rounded_rectangle([(8, 8), (56, 56)], radius=4, fill=COLORS["dark_blue_gray"], outline=COLORS["charcoal_gray"], width=2)
    # Draw display area (smaller rounded rectangle at top)
    draw.rounded_rectangle([(12, 12), (52, 22)], radius=2, fill=COLORS["light_gray"])
    # Draw calculator buttons (grid)
    button_positions = [
        (14, 26), (26, 26), (38, 26),
        (14, 34), (26, 34), (38, 34),
        (14, 42), (26, 42), (38, 42),
    ]
    for x, y in button_positions:
        draw.rectangle([(x, y), (x+8, y+6)], fill=COLORS["light_gray"], outline=COLORS["silver_gray"], width=1)
    return img

def generate_quasi_nametag_icon():
    img, draw = create_icon_base()
    # Draw nametag body (rounded rectangle badge shape)
    draw.rounded_rectangle([(6, 14), (58, 50)], radius=6, fill=COLORS["red_orange"], outline=COLORS["dark_red"], width=2)
    # Draw pin/clip at top
    draw.ellipse([(28, 8), (36, 16)], fill=COLORS["light_gray"], outline=COLORS["silver_gray"], width=1)
    draw.rectangle([(30, 12), (34, 18)], fill=COLORS["light_gray"])
    # Draw name lines (simulating text)
    draw.rectangle([(12, 22), (52, 26)], fill=COLORS["white"])
    draw.rectangle([(12, 30), (45, 34)], fill=COLORS["white"])
    draw.rectangle([(12, 38), (42, 42)], fill=COLORS["white"])
    return img

def generate_quasi_doodle_icon():
    img, draw = create_icon_base()
    # Draw canvas frame (white canvas with border)
    draw.rounded_rectangle([(4, 4), (60, 60)], radius=4, fill=COLORS["white"], outline=COLORS["light_gray"], width=2)
    # Draw inner canvas area
    draw.rounded_rectangle([(8, 8), (56, 56)], radius=2, fill=COLORS["light_silver"])
    # Draw colorful doodles/squiggles on the canvas
    draw.ellipse([(14, 16), (26, 28)], fill=COLORS["red_orange"])
    draw.ellipse([(18, 22), (30, 34)], fill=COLORS["red_orange"])
    draw.ellipse([(22, 28), (34, 40)], fill=COLORS["red_orange"])
    # Blue doodle
    draw.ellipse([(32, 14), (44, 26)], fill=COLORS["bright_blue"])
    draw.ellipse([(36, 20), (48, 32)], fill=COLORS["bright_blue"])
    # Yellow/Orange doodle
    draw.ellipse([(16, 36), (28, 48)], fill=COLORS["dark_orange"])
    draw.ellipse([(20, 42), (32, 54)], fill=COLORS["dark_orange"])
    # Purple accent
    draw.ellipse([(38, 34), (48, 44)], fill=COLORS["amethyst_purple"])
    # Draw cursor crosshair (green to match app's CURSOR_COLOR)
    cursor_x, cursor_y = 46, 18
    cursor_size = 6
    draw.ellipse([(cursor_x - cursor_size, cursor_y - cursor_size),
                  (cursor_x + cursor_size, cursor_y + cursor_size)],
                 outline=COLORS["white"], width=2)
    draw.ellipse([(cursor_x - cursor_size + 1, cursor_y - cursor_size + 1),
                  (cursor_x + cursor_size - 1, cursor_y + cursor_size - 1)],
                 fill=COLORS["emerald_green"], outline=COLORS["emerald_green"], width=1)
    return img

def generate_camera_icon():
    img, draw = create_icon_base()
    # Camera body
    draw.rounded_rectangle([(10, 20), (54, 48)], radius=6, fill=COLORS["charcoal_gray"], outline=COLORS["dark_blue_gray"], width=2)
    # Lens
    draw.ellipse([(22, 24), (42, 44)], fill=COLORS["light_gray"], outline=COLORS["silver_gray"], width=2)
    draw.ellipse([(28, 30), (36, 38)], fill=COLORS["dark_blue_gray"]) # Inner lens
    # Flash
    draw.rectangle([(46, 24), (50, 30)], fill=COLORS["sun_yellow"], outline=COLORS["dark_orange"], width=1)
    # Shutter button
    draw.ellipse([(48, 16), (52, 20)], fill=COLORS["red_orange"], outline=COLORS["dark_red"], width=1)
    return img

def generate_confetti_icon():
    img, draw = create_icon_base()
    colors = [COLORS["red_orange"], COLORS["sun_yellow"], COLORS["emerald_green"], COLORS["bright_blue"], COLORS["amethyst_purple"]]
    import random
    for _ in range(30):
        x = random.randint(5, 59)
        y = random.randint(5, 59)
        size = random.randint(3, 8)
        color = random.choice(colors)
        draw.rectangle([(x, y), (x + size, y + size)], fill=color)
    return img

def generate_connect4_icon():
    img, draw = create_icon_base()
    # Board
    draw.rounded_rectangle([(8, 18), (56, 56)], radius=4, fill=COLORS["bright_blue"], outline=COLORS["steel_blue"], width=2)
    # Slots
    for r in range(3):
        for c in range(4):
            x = 12 + c * 10
            y = 22 + r * 10
            draw.ellipse([(x, y), (x + 8, y + 8)], fill=COLORS["light_silver"], outline=COLORS["silver_gray"], width=1)
    # Red and Yellow pieces
    draw.ellipse([(12, 22), (20, 30)], fill=COLORS["red_orange"])
    draw.ellipse([(22, 32), (30, 40)], fill=COLORS["sun_yellow"])
    return img

def generate_doom_launcher_icon():
    img, draw = create_icon_base()
    # Fiery background
    draw.rectangle([(0, 0), (64, 64)], fill=COLORS["dark_red"])
    # Stylized "D" using shapes
    draw.arc([(15, 10), (45, 50)], start=270, end=90, fill=COLORS["sun_yellow"], width=8)
    draw.line([(19, 10), (19, 50)], fill=COLORS["sun_yellow"], width=8)
    # Flame effect (simple triangles)
    draw.polygon([(5, 55), (15, 45), (25, 55)], fill=COLORS["dark_orange"])
    draw.polygon([(40, 50), (50, 40), (60, 50)], fill=COLORS["dark_orange"])
    return img

def generate_draw_icon():
    img, draw = create_icon_base()
    # Canvas
    draw.rounded_rectangle([(8, 8), (56, 56)], radius=4, fill=COLORS["white"], outline=COLORS["silver_gray"], width=2)
    # Paintbrush
    draw.rectangle([(40, 10), (44, 30)], fill=COLORS["dark_blue_gray"]) # Handle
    draw.polygon([(38, 30), (46, 30), (42, 38)], fill=COLORS["sun_yellow"]) # Bristles
    # Paint stroke
    draw.arc([(15, 35), (40, 50)], start=180, end=0, fill=COLORS["bright_blue"], width=4)
    return img

def generate_errortest_icon():
    img, draw = create_icon_base()
    # Warning triangle
    draw.polygon([(32, 10), (54, 50), (10, 50)], fill=COLORS["sun_yellow"], outline=COLORS["dark_orange"], width=2)
    # Exclamation mark
    draw.rectangle([(30, 20), (34, 38)], fill=COLORS["dark_blue_gray"])
    draw.ellipse([(30, 42), (34, 46)], fill=COLORS["dark_blue_gray"])
    return img

def generate_filemanager_icon():
    img, draw = create_icon_base()
    # Folder icon
    draw.rectangle([(10, 20), (30, 50)], fill=COLORS["sun_yellow"], outline=COLORS["dark_orange"], width=2)
    draw.polygon([(10, 20), (15, 15), (35, 15), (30, 20)], fill=COLORS["sun_yellow"], outline=COLORS["dark_orange"], width=2)
    # Document icon
    draw.rectangle([(34, 28), (54, 50)], fill=COLORS["light_silver"], outline=COLORS["silver_gray"], width=2)
    draw.polygon([(48, 28), (54, 34), (54, 28)], fill=COLORS["silver_gray"]) # Folded corner
    return img

def generate_helloworld_icon():
    img, draw = create_icon_base()
    # Speech bubble
    draw.rounded_rectangle([(5, 10), (59, 45)], radius=8, fill=COLORS["steel_blue"], outline=COLORS["bright_blue"], width=4)
    draw.polygon([(20, 45), (28, 55), (30, 45)], fill=COLORS["steel_blue"], outline=COLORS["bright_blue"], width=4)
    # Text "Hi!" using shapes
    # use a truetype font
    font = ImageFont.truetype("assets/Archivo-Bold.ttf",15)
    draw.text((12, 19), "Hello!", font=font, fill=COLORS["white"])
    return img

def generate_imageview_icon():
    img, draw = create_icon_base()
    # Mountain landscape
    draw.rectangle([(0, 0), (64, 64)], fill=COLORS["bright_blue"]) # Sky
    draw.polygon([(0, 40), (32, 15), (64, 40), (64, 64), (0, 64)], fill=COLORS["emerald_green"]) # Mountains
    draw.polygon([(10, 45), (25, 30), (40, 45), (40, 64), (10, 64)], fill=COLORS["emerald_green"]) # Closer mountain
    # Sun
    draw.ellipse([(45, 5), (59, 19)], fill=COLORS["sun_yellow"])
    return img

def generate_imu_icon():
    img, draw = create_icon_base()
    # Gyroscope-like circles
    # Redesigned IMU icon: Integrated elements, no lines/background
    # Central circle (main body)
    draw.ellipse([(12, 12), (52, 52)], fill=COLORS["dark_blue_gray"])
    # Inner circle (representing sensor)
    draw.ellipse([(20, 20), (44, 44)], fill=COLORS["charcoal_gray"])
    # Small central dot (indicator)
    draw.ellipse([(29, 29), (35, 35)], fill=COLORS["bright_blue"])
    # Horizontal and vertical bars (axes)
    draw.rectangle([(10, 30), (54, 34)], fill=COLORS["light_gray"])
    draw.rectangle([(30, 10), (34, 54)], fill=COLORS["light_gray"])
    return img

def generate_musicplayer_icon():
    img, draw = create_icon_base()
    # Music note
    # Redesigned Music Player icon: Integrated elements, no lines/background
    # Main music note shape
    draw.ellipse([(18, 38), (33, 53)], fill=COLORS["red_orange"]) # Note head
    draw.rectangle([(31, 18), (35, 43)], fill=COLORS["dark_red"]) # Note stem
    draw.arc([(35, 13), (48, 28)], start=270, end=90, fill=COLORS["dark_orange"], width=0) # Note flag
    # Play button triangle (integrated)
    draw.polygon([(25, 25), (40, 32), (25, 39)], fill=COLORS["white"])
    return img

def generate_nostr_icon():
    img, draw = create_icon_base()
    # Stylized "N" using shapes
    draw.line([(15, 50), (15, 10)], fill=COLORS["sun_yellow"], width=8)
    draw.line([(15, 10), (45, 50)], fill=COLORS["sun_yellow"], width=8)
    draw.line([(45, 50), (45, 10)], fill=COLORS["sun_yellow"], width=8)
    # Speech bubble/connection lines
    draw.line([(10, 50), (25, 35)], fill=COLORS["bright_blue"], width=2)
    draw.line([(35, 35), (50, 50)], fill=COLORS["bright_blue"], width=2)
    return img

def generate_showbattery_icon():
    img, draw = create_icon_base()
    # Battery body
    draw.rounded_rectangle([(15, 20), (49, 44)], radius=4, outline=COLORS["dark_blue_gray"], width=2)
    draw.rectangle([(49, 28), (52, 36)], fill=COLORS["dark_blue_gray"]) # Terminal
    # Battery level (green)
    draw.rectangle([(17, 22), (47, 42)], fill=COLORS["emerald_green"])
    return img

def generate_showfonts_icon():
    img, draw = create_icon_base()
    # "Aa" text using shapes
    # A
    draw.polygon([(10, 40), (20, 10), (30, 40)], fill=COLORS["red_orange"], outline=COLORS["dark_red"], width=2)
    draw.line([(15, 30), (25, 30)], fill=COLORS["red_orange"], width=2)
    # a
    draw.ellipse([(35, 25), (45, 35)], fill=COLORS["bright_blue"], outline=COLORS["steel_blue"], width=2)
    draw.line([(45, 28), (45, 40)], fill=COLORS["bright_blue"], width=2)
    # Ruler/underline
    draw.line([(10, 50), (54, 50)], fill=COLORS["dark_blue_gray"], width=2)
    draw.line([(10, 52), (54, 52)], fill=COLORS["dark_blue_gray"], width=1)
    return img

def generate_soundrecorder_icon():
    img, draw = create_icon_base()
    # Microphone
    draw.ellipse([(25, 15), (39, 30)], fill=COLORS["light_gray"], outline=COLORS["silver_gray"], width=2) # Mic head
    draw.rectangle([(30, 30), (34, 45)], fill=COLORS["light_gray"], outline=COLORS["silver_gray"], width=2) # Mic body
    draw.rectangle([(28, 45), (36, 48)], fill=COLORS["light_gray"], outline=COLORS["silver_gray"], width=2) # Base
    # Sound waves
    draw.arc([(40, 20), (50, 30)], start=90, end=270, fill=COLORS["bright_blue"], width=2)
    draw.arc([(42, 18), (52, 32)], start=90, end=270, fill=COLORS["bright_blue"], width=2)
    return img

def generate_about_icon():
    img, draw = create_icon_base()
    # Draw a rounded rectangle as the base
    # draw.rounded_rectangle([(2, 2), (62, 62)], radius=8, fill=COLORS["white"], outline=COLORS["silver_gray"], width=2)
    draw.rounded_rectangle([(5, 5), (59, 59)], radius=8, fill=COLORS["white"])
    # Load the MicroPythonOS logo symbol
    try:
        logo = Image.open("assets/MicroPythonOS-logo-symbol-black-short64.png").convert("RGBA")
    except FileNotFoundError:
        print("Error: MicroPythonOS-logo-symbol-black-short64.png not found in assets directory.")
        # Create a placeholder if the logo is not found
        draw.text((10, 20), "About", fill=COLORS["black"])
        return img

    # Resize logo to fit within the icon, if necessary
    logo = logo.resize((48, 48), Image.LANCZOS)

    # Calculate position to center the logo
    x = (64 - logo.width) // 2
    y = (64 - logo.height) // 2

    # Paste the logo onto the icon
    img.paste(logo, (x, y), logo)
    return img

def generate_appstore_icon():
    img, draw = create_icon_base()
    # Draw a rounded rectangle as the base, similar to the about icon
    draw.rounded_rectangle([(5, 5), (59, 59)], radius=8, fill=COLORS["light_silver"],outline=COLORS["silver_gray"], width=2)

    # Draw four mini square items representing apps
    app_colors = [COLORS["bright_blue"], COLORS["emerald_green"], COLORS["sun_yellow"], COLORS["amethyst_purple"]]
    app_positions = [
        (15, 10), (35, 10),
        (15, 30), (35, 30),
    ]
    for i, (x, y) in enumerate(app_positions):
        draw.rectangle([(x, y), (x + 12, y + 12)], fill=app_colors[i], outline=COLORS["charcoal_gray"], width=1)

    # Draw a download symbol (down arrow)
    # Arrow body
    draw.rectangle([(24, 35), (40, 48)], fill=COLORS["red_orange"],outline=COLORS["charcoal_gray"])
    # Arrowhead
    draw.polygon([(20, 46), (44, 46), (32, 56)], fill=COLORS["red_orange"],outline=COLORS["charcoal_gray"])
    # mask edge triangle
    draw.rectangle([(26, 37), (38, 50)], fill=COLORS["red_orange"])
    return img

def generate_launcher_icon():
    img, draw = create_icon_base()
    # Home icon
    draw.polygon([(32, 10), (54, 32), (10, 32)], fill=COLORS["bright_blue"], outline=COLORS["steel_blue"], width=2) # Roof
    draw.rectangle([(15, 30), (49, 54)], fill=COLORS["light_silver"], outline=COLORS["silver_gray"], width=2) # House body
    draw.rectangle([(28, 40), (36, 54)], fill=COLORS["light_gray"], outline=COLORS["silver_gray"], width=1) # Door
    return img

def generate_osupdate_icon():
    img, draw = create_icon_base()
    # Up arrow
    # Redesigned OS Update icon: Integrated elements, no lines/background
    # Main gear shape (outer circle with cogs)
    draw.ellipse([(10, 10), (54, 54)], fill=COLORS["dark_blue_gray"])
    # Inner circle (center of gear)
    draw.ellipse([(20, 20), (44, 44)], fill=COLORS["charcoal_gray"])
    # Up arrow (integrated into the gear)
    draw.polygon([(22, 38), (42, 38), (32, 18)], fill=COLORS["bright_blue"])
    draw.rectangle([(28, 38), (36, 48)], fill=COLORS["bright_blue"])
    return img

def main():
    parser = argparse.ArgumentParser(description="Generate app icons.")
    parser.add_argument('--app', nargs='*', help='Specify app names to generate icons for (e.g., "QuasiBird" "QuasiCalculator"). If not specified, all icons will be generated.')
    args = parser.parse_args()

    apps = {
        "com.micropythonos.camera": generate_camera_icon,
        "com.micropythonos.confetti": generate_confetti_icon,
        "com.micropythonos.connect4": generate_connect4_icon,
        "com.micropythonos.doom_launcher": generate_doom_launcher_icon,
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
        "com.micropythonos.launcher": generate_launcher_icon,
        "com.micropythonos.osupdate": generate_osupdate_icon,
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

if __name__ == "__main__":
    main()
