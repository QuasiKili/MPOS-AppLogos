#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

import argparse
from PIL import Image, ImageDraw, ImageFont
import os

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
    draw.ellipse([(10, 15), (50, 55)], fill='#FFD700', outline='#FFA500', width=3)
    # Draw wing - adjusted for new body size and position
    draw.ellipse([(15, 35), (40, 50)], fill='#FFA500', outline='#FF8C00', width=2)
    # Draw eye - adjusted for new body size and position
    draw.ellipse([(32, 22), (42, 32)], fill='#FFFFFF', outline='#000000', width=2)
    draw.ellipse([(35, 25), (39, 29)], fill='#000000')
    # Draw beak - adjusted for new body size and position
    beak = [(44, 34), (56, 34), (49, 40)]
    draw.polygon(beak, fill='#FF6B35', outline='#D84315', width=1)
    beak = [(44, 34), (56, 34), (49, 28)]
    draw.polygon(beak, fill='#FF6B35', outline='#D84315', width=1)
    return img

def generate_quasi_calculator_icon():
    img, draw = create_icon_base()
    # Draw calculator body (rounded rectangle)
    draw.rounded_rectangle([(8, 8), (56, 56)], radius=4, fill='#2C3E50', outline='#34495E', width=2)
    # Draw display area (smaller rounded rectangle at top)
    draw.rounded_rectangle([(12, 12), (52, 22)], radius=2, fill='#7F8C8D')
    # Draw calculator buttons (grid)
    button_positions = [
        (14, 26), (26, 26), (38, 26),
        (14, 34), (26, 34), (38, 34),
        (14, 42), (26, 42), (38, 42),
    ]
    for x, y in button_positions:
        draw.rectangle([(x, y), (x+8, y+6)], fill='#95A5A6', outline='#BDC3C7', width=1)
    return img

def generate_quasi_nametag_icon():
    img, draw = create_icon_base()
    # Draw nametag body (rounded rectangle badge shape)
    draw.rounded_rectangle([(6, 14), (58, 50)], radius=6, fill='#E74C3C', outline='#C0392B', width=2)
    # Draw pin/clip at top
    draw.ellipse([(28, 8), (36, 16)], fill='#95A5A6', outline='#7F8C8D', width=1)
    draw.rectangle([(30, 12), (34, 18)], fill='#95A5A6')
    # Draw name lines (simulating text)
    draw.rectangle([(12, 22), (52, 26)], fill='#FFFFFF')
    draw.rectangle([(12, 30), (45, 34)], fill='#FFFFFF')
    draw.rectangle([(12, 38), (42, 42)], fill='#FFFFFF')
    return img

def generate_quasi_doodle_icon():
    img, draw = create_icon_base()
    # Draw canvas frame (white canvas with border)
    draw.rounded_rectangle([(4, 4), (60, 60)], radius=4, fill='#FFFFFF', outline='#95A5A6', width=2)
    # Draw inner canvas area
    draw.rounded_rectangle([(8, 8), (56, 56)], radius=2, fill='#F8F8F8')
    # Draw colorful doodles/squiggles on the canvas
    draw.ellipse([(14, 16), (26, 28)], fill='#EC048C')
    draw.ellipse([(18, 22), (30, 34)], fill='#EC048C')
    draw.ellipse([(22, 28), (34, 40)], fill='#EC048C')
    # Blue doodle
    draw.ellipse([(32, 14), (44, 26)], fill='#3498DB')
    draw.ellipse([(36, 20), (48, 32)], fill='#3498DB')
    # Yellow/Orange doodle
    draw.ellipse([(16, 36), (28, 48)], fill='#F39C12')
    draw.ellipse([(20, 42), (32, 54)], fill='#F39C12')
    # Purple accent
    draw.ellipse([(38, 34), (48, 44)], fill='#9B59B6')
    # Draw cursor crosshair (green to match app's CURSOR_COLOR)
    cursor_x, cursor_y = 46, 18
    cursor_size = 6
    draw.ellipse([(cursor_x - cursor_size, cursor_y - cursor_size),
                  (cursor_x + cursor_size, cursor_y + cursor_size)],
                 outline='#FFFFFF', width=2)
    draw.ellipse([(cursor_x - cursor_size + 1, cursor_y - cursor_size + 1),
                  (cursor_x + cursor_size - 1, cursor_y + cursor_size - 1)],
                 fill='#00FF00', outline='#00CC00', width=1)
    return img

def generate_camera_icon():
    img, draw = create_icon_base()
    # Camera body
    draw.rounded_rectangle([(10, 20), (54, 48)], radius=6, fill='#34495E', outline='#2C3E50', width=2)
    # Lens
    draw.ellipse([(22, 24), (42, 44)], fill='#7F8C8D', outline='#95A5A6', width=2)
    draw.ellipse([(28, 30), (36, 38)], fill='#2C3E50') # Inner lens
    # Flash
    draw.rectangle([(46, 24), (50, 30)], fill='#F1C40F', outline='#F39C12', width=1)
    # Shutter button
    draw.ellipse([(48, 16), (52, 20)], fill='#E74C3C', outline='#C0392B', width=1)
    return img

def generate_confetti_icon():
    img, draw = create_icon_base()
    colors = ['#E74C3C', '#F1C40F', '#2ECC71', '#3498DB', '#9B59B6']
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
    draw.rounded_rectangle([(8, 18), (56, 56)], radius=4, fill='#3498DB', outline='#2980B9', width=2)
    # Slots
    for r in range(3):
        for c in range(4):
            x = 12 + c * 10
            y = 22 + r * 10
            draw.ellipse([(x, y), (x + 8, y + 8)], fill='#ECF0F1', outline='#BDC3C7', width=1)
    # Red and Yellow pieces
    draw.ellipse([(12, 22), (20, 30)], fill='#E74C3C')
    draw.ellipse([(22, 32), (30, 40)], fill='#F1C40F')
    return img

def generate_doom_launcher_icon():
    img, draw = create_icon_base()
    # Fiery background
    draw.rectangle([(0, 0), (64, 64)], fill='#8B0000')
    # Stylized "D" using shapes
    draw.arc([(15, 10), (45, 50)], start=270, end=90, fill='#FFD700', width=8)
    draw.line([(19, 10), (19, 50)], fill='#FFD700', width=8)
    # Flame effect (simple triangles)
    draw.polygon([(5, 55), (15, 45), (25, 55)], fill='#FF4500')
    draw.polygon([(40, 50), (50, 40), (60, 50)], fill='#FF4500')
    return img

def generate_draw_icon():
    img, draw = create_icon_base()
    # Canvas
    draw.rounded_rectangle([(8, 8), (56, 56)], radius=4, fill='#FFFFFF', outline='#BDC3C7', width=2)
    # Paintbrush
    draw.rectangle([(40, 10), (44, 30)], fill='#8B4513') # Handle
    draw.polygon([(38, 30), (46, 30), (42, 38)], fill='#F1C40F') # Bristles
    # Paint stroke
    draw.arc([(15, 35), (40, 50)], start=180, end=0, fill='#3498DB', width=4)
    return img

def generate_errortest_icon():
    img, draw = create_icon_base()
    # Warning triangle
    draw.polygon([(32, 10), (54, 50), (10, 50)], fill='#F1C40F', outline='#F39C12', width=2)
    # Exclamation mark
    draw.rectangle([(30, 20), (34, 38)], fill='#2C3E50')
    draw.ellipse([(30, 42), (34, 46)], fill='#2C3E50')
    return img

def generate_filemanager_icon():
    img, draw = create_icon_base()
    # Folder icon
    draw.rectangle([(10, 20), (30, 50)], fill='#F1C40F', outline='#F39C12', width=2)
    draw.polygon([(10, 20), (15, 15), (35, 15), (30, 20)], fill='#F1C40F', outline='#F39C12', width=2)
    # Document icon
    draw.rectangle([(34, 28), (54, 50)], fill='#ECF0F1', outline='#BDC3C7', width=2)
    draw.polygon([(48, 28), (54, 34), (54, 28)], fill='#BDC3C7') # Folded corner
    return img

def generate_helloworld_icon():
    img, draw = create_icon_base()
    # Speech bubble
    draw.rounded_rectangle([(10, 10), (54, 45)], radius=8, fill='#FFFFFF', outline='#3498DB', width=2)
    draw.polygon([(20, 45), (28, 55), (30, 45)], fill='#FFFFFF', outline='#3498DB', width=2)
    # Text "Hi!" using shapes
    draw.line([(20, 20), (20, 35)], fill='#2C3E50', width=4)
    draw.line([(20, 20), (28, 20)], fill='#2C3E50', width=4)
    draw.line([(28, 20), (28, 28)], fill='#2C3E50', width=4)
    draw.line([(20, 28), (28, 28)], fill='#2C3E50', width=4)
    draw.line([(20, 35), (28, 35)], fill='#2C3E50', width=4)
    draw.ellipse([(23, 38), (25, 40)], fill='#2C3E50') # Exclamation dot
    return img

def generate_imageview_icon():
    img, draw = create_icon_base()
    # Mountain landscape
    draw.rectangle([(0, 0), (64, 64)], fill='#87CEEB') # Sky
    draw.polygon([(0, 40), (32, 15), (64, 40), (64, 64), (0, 64)], fill='#2ECC71') # Mountains
    draw.polygon([(10, 45), (25, 30), (40, 45), (40, 64), (10, 64)], fill='#27AE60') # Closer mountain
    # Sun
    draw.ellipse([(45, 5), (59, 19)], fill='#F1C40F')
    return img

def generate_imu_icon():
    img, draw = create_icon_base()
    # Gyroscope-like circles
    draw.ellipse([(10, 10), (54, 54)], outline='#3498DB', width=2)
    draw.ellipse([(15, 20), (49, 44)], outline='#2ECC71', width=2)
    draw.line([(10, 32), (54, 32)], fill='#E74C3C', width=2)
    draw.line([(32, 10), (32, 54)], fill='#E74C3C', width=2)
    return img

def generate_musicplayer_icon():
    img, draw = create_icon_base()
    # Music note
    draw.ellipse([(15, 35), (30, 50)], fill='#E74C3C', outline='#C0392B', width=2)
    draw.rectangle([(28, 15), (32, 40)], fill='#E74C3C', outline='#C0392B', width=2)
    draw.arc([(32, 10), (45, 25)], start=270, end=90, fill='#E74C3C', width=2)
    return img

def generate_nostr_icon():
    img, draw = create_icon_base()
    # Stylized "N" using shapes
    draw.line([(15, 50), (15, 10)], fill='#F1C40F', width=8)
    draw.line([(15, 10), (45, 50)], fill='#F1C40F', width=8)
    draw.line([(45, 50), (45, 10)], fill='#F1C40F', width=8)
    # Speech bubble/connection lines
    draw.line([(10, 50), (25, 35)], fill='#3498DB', width=2)
    draw.line([(35, 35), (50, 50)], fill='#3498DB', width=2)
    return img

def generate_showbattery_icon():
    img, draw = create_icon_base()
    # Battery body
    draw.rounded_rectangle([(15, 20), (49, 44)], radius=4, outline='#2C3E50', width=2)
    draw.rectangle([(49, 28), (52, 36)], fill='#2C3E50') # Terminal
    # Battery level (green)
    draw.rectangle([(17, 22), (47, 42)], fill='#2ECC71')
    return img

def generate_showfonts_icon():
    img, draw = create_icon_base()
    # "Aa" text using shapes
    # A
    draw.polygon([(10, 40), (20, 10), (30, 40)], fill='#E74C3C', outline='#C0392B', width=2)
    draw.line([(15, 30), (25, 30)], fill='#E74C3C', width=2)
    # a
    draw.ellipse([(35, 25), (45, 35)], fill='#3498DB', outline='#2980B9', width=2)
    draw.line([(45, 28), (45, 40)], fill='#3498DB', width=2)
    # Ruler/underline
    draw.line([(10, 50), (54, 50)], fill='#2C3E50', width=2)
    draw.line([(10, 52), (54, 52)], fill='#2C3E50', width=1)
    return img

def generate_soundrecorder_icon():
    img, draw = create_icon_base()
    # Microphone
    draw.ellipse([(25, 15), (39, 30)], fill='#7F8C8D', outline='#95A5A6', width=2) # Mic head
    draw.rectangle([(30, 30), (34, 45)], fill='#7F8C8D', outline='#95A5A6', width=2) # Mic body
    draw.rectangle([(28, 45), (36, 48)], fill='#7F8C8D', outline='#95A5A6', width=2) # Base
    # Sound waves
    draw.arc([(40, 20), (50, 30)], start=90, end=270, fill='#3498DB', width=2)
    draw.arc([(42, 18), (52, 32)], start=90, end=270, fill='#3498DB', width=2)
    return img

def generate_about_icon():
    img, draw = create_icon_base()
    # "i" for information using shapes
    draw.line([(32, 15), (32, 35)], fill='#3498DB', width=4)
    draw.ellipse([(30, 40), (34, 44)], fill='#3498DB')
    # Circle around it
    draw.ellipse([(10, 5), (54, 49)], outline='#3498DB', width=2)
    return img

def generate_appstore_icon():
    img, draw = create_icon_base()
    # Shopping bag
    draw.polygon([(15, 15), (49, 15), (54, 50), (10, 50)], fill='#2ECC71', outline='#27AE60', width=2)
    draw.line([(20, 15), (20, 10)], fill='#27AE60', width=2)
    draw.line([(44, 15), (44, 10)], fill='#27AE60', width=2)
    draw.arc([(18, 5), (46, 15)], start=180, end=0, fill='#2ECC71', width=2)
    draw.arc([(18, 5), (46, 15)], start=180, end=0, fill='#27AE60', width=2)
    # "A" for App using shapes
    draw.polygon([(28, 35), (32, 25), (36, 35)], fill='#FFFFFF', outline='#BDC3C7', width=2)
    draw.line([(30, 30), (34, 30)], fill='#FFFFFF', width=2)
    return img

def generate_launcher_icon():
    img, draw = create_icon_base()
    # Home icon
    draw.polygon([(32, 10), (54, 32), (10, 32)], fill='#3498DB', outline='#2980B9', width=2) # Roof
    draw.rectangle([(15, 30), (49, 54)], fill='#ECF0F1', outline='#BDC3C7', width=2) # House body
    draw.rectangle([(28, 40), (36, 54)], fill='#7F8C8D', outline='#95A5A6', width=1) # Door
    return img

def generate_osupdate_icon():
    img, draw = create_icon_base()
    # Up arrow
    draw.polygon([(22, 40), (42, 40), (32, 20)], fill='#2ECC71', outline='#27AE60', width=2)
    draw.rectangle([(28, 40), (36, 50)], fill='#2ECC71', outline='#27AE60', width=2)
    # Circle around it
    draw.ellipse([(10, 10), (54, 54)], outline='#2ECC71', width=2)
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
