#!/usr/bin/env python3
"""写真を図鑑用に整える: 向きを直す → 回転 → (任意で)切り抜き → 縦3:4 → 900px → EXIF/GPS を消して保存。

使い方:
  python3 tools/add_photo.py 元写真.jpg photos/名前.jpg [--rotate 90|180|270] [--crop 左,上,右,下]

  --rotate  時計回りに回す角度（横向きのモケケを縦にする）。
  --crop    回転後の画像に対する割合 0〜1（例 0.2,0.05,0.8,0.95）。省略時は中央を3:4で切り抜き。
"""
import argparse
from PIL import Image, ImageOps

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("dst")
ap.add_argument("--rotate", type=int, default=0, choices=[0, 90, 180, 270])
ap.add_argument("--crop", default=None)
a = ap.parse_args()

im = ImageOps.exif_transpose(Image.open(a.src)).convert("RGB")
if a.rotate:
    im = im.rotate(-a.rotate, expand=True)  # PIL は反時計回りなので符号を反転
W, H = im.size
if a.crop:
    l, t, r, b = [float(x) for x in a.crop.split(",")]
    im = im.crop((int(l * W), int(t * H), int(r * W), int(b * H)))
W, H = im.size
# 3:4 (縦長) に合わせて中央切り抜き
target = 3 / 4
if W / H > target:
    nw = int(H * target); x = (W - nw) // 2; im = im.crop((x, 0, x + nw, H))
else:
    nh = int(W / target); y = (H - nh) // 2; im = im.crop((0, y, W, y + nh))
im.thumbnail((900, 1200), Image.LANCZOS)
clean = Image.new("RGB", im.size); clean.paste(im)  # EXIF/GPS を持たない新しい画像
clean.save(a.dst, "JPEG", quality=85, optimize=True, progressive=True)
print("saved", a.dst, clean.size)
