from Lib import *
from PIL import Image, ImageDraw, ImageFont

os.makedirs('transgrp', exist_ok=True)
namelist = open_json('names.json')

for f in namelist:
    transname = namelist[f]
    img = Image.new('RGBA', (475, 56), (255, 255, 255, 0))
    font = ImageFont.truetype("wenquanyi.ttf", 45)
    draw = ImageDraw.Draw(img)
    x = 6
    y = 0
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            draw.text((x+dx, y+dy), transname, fill = (107,97,175), font=font)
    draw.text((x, y), transname, fill = (255,255,255), font=font)
    img.save(f"transgrp\winyoko_name{f}.png")
    img.save(f"transgrp\winyoko_name{transname}.png")
