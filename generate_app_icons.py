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

def save_icon(img, app_name, output_base_dir="."):
    """Saves the generated icon to the specified path within the app's directory structure."""
    output_dir = os.path.join(output_base_dir, app_name, 'res', 'mipmap-mdpi')
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

def main():
    parser = argparse.ArgumentParser(description="Generate app icons.")
    parser.add_argument('--app', nargs='*', help='Specify app names to generate icons for (e.g., "QuasiBird" "QuasiCalculator"). If not specified, all icons will be generated.')
    args = parser.parse_args()

    apps = {
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
