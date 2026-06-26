from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, random

out_dir = r'C:\Users\Kyrie\Documents\2.0\portfolio\images'
os.makedirs(out_dir, exist_ok=True)

font_paths = [
    r'C:\Windows\Fonts\msyh.ttc',
    r'C:\Windows\Fonts\msyhbd.ttc',
    r'C:\Windows\Fonts\simhei.ttf',
    r'C:\Windows\Fonts\simsun.ttc',
]

font_large = None
font_medium = None
font_small = None

for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_large = ImageFont.truetype(fp, 72)
            font_medium = ImageFont.truetype(fp, 42)
            font_small = ImageFont.truetype(fp, 28)
            break
        except:
            pass

if font_large is None:
    font_large = ImageFont.load_default()
    font_medium = ImageFont.load_default()
    font_small = ImageFont.load_default()

def create_gradient(width, height, colors):
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    for y in range(height):
        ratio = y / height
        r = int(colors[0][0] * (1-ratio) + colors[1][0] * ratio)
        g = int(colors[0][1] * (1-ratio) + colors[1][1] * ratio)
        b = int(colors[0][2] * (1-ratio) + colors[1][2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    return img

def generate_image(filename, title, subtitle, colors, circle_count=3, w=1600, h=1067):
    print(f'  Generating: {filename}...', end='')
    base = create_gradient(w, h, colors)
    draw = ImageDraw.Draw(base)
    random.seed(abs(hash(filename)))
    overlay = Image.new('RGBA', (w, h), (0,0,0,0))
    odraw = ImageDraw.Draw(overlay)
    for _ in range(circle_count):
        cx = random.randint(int(-w*0.1), int(w*1.1))
        cy = random.randint(int(-h*0.1), int(h*1.1))
        r = random.randint(100, 300)
        alpha = random.randint(20, 50)
        odraw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(255, 255, 255, alpha))
    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=40))
    base = Image.alpha_composite(base.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(base)
    draw.rectangle([40, 40, w-40, h-40], outline=(255,255,255,30), width=1)
    if font_large:
        bbox = font_large.getbbox(title)
        tw = bbox[2] - bbox[0] if bbox else len(title) * 40
        tx = (w - tw) // 2
        ty = h // 2 - 80
        draw.text((tx+3, ty+3), title, font=font_large, fill=(0,0,0,60))
        draw.text((tx, ty), title, font=font_large, fill=(255,255,255,220))
    if subtitle and font_small:
        bbox = font_small.getbbox(subtitle)
        sw = bbox[2] - bbox[0] if bbox else len(subtitle) * 16
        sx = (w - sw) // 2
        sy = ty + 100
        draw.line([(w//2 - 40, sy-15), (w//2 + 40, sy-15)], fill=(255,255,255,180), width=2)
        draw.text((sx+1, sy+1), subtitle, font=font_small, fill=(0,0,0,50))
        draw.text((sx, sy), subtitle, font=font_small, fill=(255,255,255,180))
    filepath = os.path.join(out_dir, filename)
    base.save(filepath, 'JPEG', quality=92)
    print(' OK')
    return filepath

print('Generating portfolio images...')

generate_image('cover.jpg', 'LIU YIJING', 'AI Content  |  New Media  |  Portfolio 2025',
               [(25, 30, 70), (80, 60, 150)], circle_count=6)

generate_image('p1-1.jpg', 'AI Interview & Journalism', 'Xiaolu AI Transcription + Interview',
               [(20, 60, 90), (60, 120, 140)], circle_count=3)
generate_image('p1-2.jpg', 'Script & Video Production', 'AI-assisted Script Refinement',
               [(30, 80, 100), (80, 140, 160)], circle_count=3)
generate_image('p1-3.jpg', 'Multi-Platform Publishing', 'Shangjie . Toutiao . Sohu',
               [(40, 50, 90), (90, 110, 150)], circle_count=3)

generate_image('p2-1.jpg', 'Commercial Short Films', 'Laundry Detergent / Heat Pump / DJI',
               [(120, 60, 30), (180, 120, 60)], circle_count=4)
generate_image('p2-2.jpg', 'Brand Marketing Campaign', 'Mazhua Magic - Champion Award',
               [(140, 70, 40), (200, 140, 80)], circle_count=4)
generate_image('p2-3.jpg', 'Business Youth Magazine', 'Short Film Production & Editing',
               [(100, 50, 30), (170, 110, 70)], circle_count=3)

generate_image('p3-1.jpg', 'Midjourney Brand Design', 'AI Brand Visual Identity System',
               [(80, 40, 100), (140, 80, 160)], circle_count=4)
generate_image('p3-2.jpg', 'IP Character Design', 'Yellow Peach Brand Identity',
               [(90, 50, 110), (150, 90, 170)], circle_count=3)
generate_image('p3-3.jpg', 'Posters & Merchandise', 'Full Visual System Application',
               [(70, 30, 90), (130, 70, 150)], circle_count=3)

generate_image('p4-1.jpg', 'Data Visualization', 'Flourish Interactive Charts',
               [(20, 80, 60), (60, 140, 110)], circle_count=4)
generate_image('p4-2.jpg', 'Greenwashing Investigation', 'Corporate Environmental Data Research',
               [(30, 90, 70), (70, 150, 120)], circle_count=3)
generate_image('p4-3.jpg', 'Readymag Publication', 'Interactive Digital Data Journalism',
               [(40, 70, 60), (80, 130, 110)], circle_count=3)

generate_image('p5-1.jpg', 'Drone Oblique Photography', '2000+ Aerial Images Collection',
               [(10, 30, 70), (40, 80, 130)], circle_count=4)
generate_image('p5-2.jpg', '3D Reality Modeling', 'ContextCapture 3D Reconstruction',
               [(20, 40, 80), (50, 90, 140)], circle_count=4)
generate_image('p5-3.jpg', 'VR Spatial Visualization', '720 Yun Virtual Tour',
               [(15, 35, 75), (45, 85, 135)], circle_count=3)

generate_image('p6-1.jpg', 'State Grid Safety Video', 'AI Animation + Live Action',
               [(20, 50, 100), (60, 100, 160)], circle_count=3)
generate_image('p6-2.jpg', 'Water Resources Science Video', 'MG Animation Promotional Video',
               [(30, 60, 110), (70, 110, 170)], circle_count=3)
generate_image('p6-3.jpg', 'AI Production Workflow', 'Doubao . Jimeng Animation',
               [(40, 50, 90), (80, 100, 150)], circle_count=3)

print()
print('All 19 images generated successfully!')
