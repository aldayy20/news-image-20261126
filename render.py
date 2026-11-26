#!/usr/bin/env python3
"""Render the 26 November 2026 world-news poster (1024x1024 PNG).

Run:  python3 render.py            -> writes entry.png beside this file
Uses only Pillow + the DejaVu fonts shipped with most Linux systems.
The graded entrypoint is main.ts, which copies the rendered entry.png
to $MAKEFUN_OUTPUT_DIR/entry.png. This script is kept in the repo so
anyone can regenerate the image from source.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 231)
INK = (17, 17, 17)
RED = (185, 28, 28)
DARKRED = (127, 29, 29)
BLUE = (29, 78, 216)
NAVY = (30, 58, 138)
TEAL = (13, 116, 128)
AMBER = (180, 83, 9)
GREEN = (21, 101, 52)
GREY = (87, 83, 78)
LIGHT = (255, 255, 255)
PANEL = (255, 255, 255)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading=None):
    lines = wrap(draw, text, fnt, max_w)
    lh = leading or int(fnt.size * 1.22)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def kicker(draw, x, y, label, colour):
    f = font(FB, 21)
    w = int(draw.textlength(label, font=f)) + 22
    draw.rounded_rectangle([x, y, x + w, y + 32], radius=4, fill=colour)
    draw.text((x + 11, y + 4), label, font=f, fill=LIGHT)
    return w


def panel(draw, x, y, w, h):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10,
                           fill=PANEL, outline=(210, 205, 192), width=2)


def main():
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)

    # ---- top black bar: the date, unmissable -------------------------------
    d.rectangle([0, 0, W, 62], fill=INK)
    d.text((24, 12), "THURSDAY, 26 NOVEMBER 2026", font=font(FB, 32), fill=LIGHT)
    d.text((W - 24 - d.textlength("ONE DAY  •  ONE IMAGE", font=font(FB, 24)), 18),
           "ONE DAY  •  ONE IMAGE", font=font(FB, 24), fill=(251, 191, 36))

    # ---- masthead ------------------------------------------------------------
    d.text((24, 74), "THE WORLD IN ONE IMAGE", font=font(FB, 58), fill=INK)
    d.text((24, 140), "Seven stories that defined the day — from tariffs to Thanksgiving.",
           font=font(FR, 24), fill=GREY)
    d.line([24, 178, W - 24, 178], fill=INK, width=3)

    # ---- HERO: Taiwan keeps its 15% tariff deal ------------------------------
    x, y, w, h = 24, 192, 976, 218
    panel(d, x, y, w, h)
    d.rounded_rectangle([x, y, x + 320, y + h], radius=10, fill=NAVY)
    d.rounded_rectangle([x + 300, y, x + 320, y + h], radius=0, fill=NAVY)
    d.text((x + 26, y + 18), "15%", font=font(FB, 92), fill=LIGHT)
    d.text((x + 26, y + 128), "TAIWAN", font=font(FB, 40), fill=LIGHT)
    d.text((x + 26, y + 172), "KEEPS IT", font=font(FB, 40), fill=(147, 197, 253))
    kicker(d, x + 350, y + 18, "TRADE  •  TARIFFS", NAVY)
    d.text((x + 350, y + 62), "TAIPEI HOLDS THE LINE",
           font=font(FB, 34), fill=INK)
    text_block(d, x + 350, y + 118,
               "Taiwan says it is confident of keeping its agreed 15% "
               "US tariff rate, a day after Trump fired a new salvo at "
               "14 trading partners — China facing 20%, the EU, Japan "
               "and South Korea capped at 15%.",
               font(FR, 20), INK, 600, leading=25)

    # ---- Row 2: Thanksgiving | F-15EX -----------------------------------------
    y2, h2 = 426, 218
    # Thanksgiving
    x, w = 24, 476
    panel(d, x, y2, w, h2)
    kicker(d, x + 18, y2 + 16, "USA  •  THANKSGIVING", DARKRED)
    d.text((x + 18, y2 + 58), "PARADE PUSHED", font=font(FB, 38), fill=INK)
    d.text((x + 18, y2 + 100), "TO SATURDAY", font=font(FB, 38), fill=INK)
    text_block(d, x + 18, y2 + 148,
               "Macy's parade moves to Saturday as gales bear down on "
               "New York; storms threaten Thanksgiving travel for 250m "
               "Americans.",
               font(FR, 19), INK, w - 36, leading=23)
    # F-15EX
    x, w = 524, 476
    panel(d, x, y2, w, h2)
    kicker(d, x + 18, y2 + 16, "DEFENCE  •  OKINAWA", AMBER)
    d.text((x + 18, y2 + 58), "F-15EX FIGHTERS", font=font(FB, 38), fill=INK)
    d.text((x + 18, y2 + 100), "AT KADENA", font=font(FB, 38), fill=INK)
    text_block(d, x + 18, y2 + 148,
               "The US Air Force unveils its newest F-15EX fighters at "
               "Kadena Air Base in Okinawa, the front line of Pacific "
               "deterrence.",
               font(FR, 19), INK, w - 36, leading=23)

    # ---- Row 3: Flipkart | Kenya | Chess --------------------------------------
    y3, h3, w3 = 660, 196, 312
    # Flipkart
    x = 24
    panel(d, x, y3, w3, h3)
    kicker(d, x + 16, y3 + 14, "BUSINESS", TEAL)
    d.text((x + 16, y3 + 54), "FLIPKART CHIEF", font=font(FB, 27), fill=INK)
    d.text((x + 16, y3 + 86), "TO STEP DOWN", font=font(FB, 27), fill=INK)
    text_block(d, x + 16, y3 + 124,
               "Flipkart CEO Kalyan Krishnamurthy steps down in "
               "December.",
               font(FR, 18), INK, w3 - 32, leading=23)
    # Kenya
    x = 356
    panel(d, x, y3, w3, h3)
    kicker(d, x + 16, y3 + 14, "AFRICA", GREEN)
    d.text((x + 16, y3 + 54), "293,600 JOBS", font=font(FB, 30), fill=INK)
    d.text((x + 16, y3 + 86), "IN SAUDI", font=font(FB, 30), fill=INK)
    text_block(d, x + 16, y3 + 124,
               "Kenya secures 293,600 job opportunities in Saudi Arabia "
               "for its workers, officials say.",
               font(FR, 18), INK, w3 - 32, leading=23)
    # Chess
    x = 688
    panel(d, x, y3, w3, h3)
    kicker(d, x + 16, y3 + 14, "CHESS  •  GENEVA", BLUE)
    d.text((x + 16, y3 + 54), "GAME 3", font=font(FB, 30), fill=INK)
    d.text((x + 16, y3 + 86), "IN GENEVA", font=font(FB, 30), fill=INK)
    text_block(d, x + 16, y3 + 124,
               "Gukesh and Sindarov, both 20, play Game 3 of the "
               "youngest world title match in 140 years.",
               font(FR, 18), INK, w3 - 32, leading=23)

    # ---- Sport strip -----------------------------------------------------------
    y4, h4 = 872, 104
    panel(d, 24, y4, 976, h4)
    kicker(d, 42, y4 + 14, "SPORT", GREEN)
    d.text((42, y4 + 52), "Liverpool 3-0 Brugge, PSG 2-2 Roma; Lille stun Bayern 2-1.",
           font=font(FB, 22), fill=INK)
    d.text((42, y4 + 82), "Barcelona 4-1 Sabah, Man Utd 2-2 Sporting; Inter 2-0 Stuttgart, Atlético 2-0 Viking.",
           font=font(FR, 18), fill=GREY)

    # ---- footer ------------------------------------------------------------------
    d.line([24, 982, W - 24, 982], fill=(210, 205, 192), width=2)
    d.text((24, 988), "Sources: Reuters, AP, UEFA, FIDE, C54 News, SimpleLife",
           font=font(FR, 13), fill=GREY)
    d.text((24, 1006), "Also: India marks Constitution Day; Ghana unveils Heritage banknotes; "
           "São Tomé reappoints its PM; ECOWAS plans regional force by 2027.",
           font=font(FR, 13), fill=GREY)

    im.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png", im.size)


if __name__ == "__main__":
    main()
