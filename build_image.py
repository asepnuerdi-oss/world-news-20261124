#!/usr/bin/env python3
"""Build the 1024x1024 'world news of 24 Nov 2026 in one image' artwork.

Deterministic: pure PIL drawing, fixed geometry, no randomness, no clock.
Output: world-news-2026-11-24.png next to this script.

Stories are the real world news of Tuesday 24 November 2026, researched
on the day from BBC, Reuters, UN News / WHO and WSJ reporting; see
NEWS_SOURCES.md for the source headline behind every panel.
"""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "world-news-2026-11-24.png")

W = H = 1024
PAPER = (247, 243, 234)
INK = (20, 24, 38)
MUTED = (92, 96, 110)
CARD = (255, 255, 255)
ACCENT = (178, 34, 52)      # headline red
SPACE = (16, 24, 54)
EARTH = (46, 110, 168)
SAND = (233, 220, 194)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def wrap(text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def centered(text, font, y, fill=INK):
    d.text(((W - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)


# ---------- masthead ----------
centered("THE WORLD IN ONE IMAGE", F(SERIF_B, 58), 26)
centered("Tuesday, 24 November 2026  ·  The day's biggest stories, in a single picture",
         F(SANS, 24), 102, MUTED)
d.line([(36, 148), (W - 36, 148)], fill=INK, width=4)
d.line([(36, 156), (W - 36, 156)], fill=INK, width=1)

# ---------- lead story ----------
lead = (36, 168, W - 36, 424)
d.rounded_rectangle(lead, radius=14, fill=CARD, outline=INK, width=3)
# space scene (left): night sky, Earth arc, satellite under a warning ring.
# Drawn on its own layer first so the Earth arc stays clipped to the box.
sx0, sy0, sx1, sy1 = 56, 188, 356, 404
scene = Image.new("RGB", (sx1 - sx0, sy1 - sy0), SPACE)
s = ImageDraw.Draw(scene)
SW, SH = sx1 - sx0, sy1 - sy0
# stars (fixed positions, no randomness)
stars = [(18, 16), (58, 40), (96, 12), (140, 34), (188, 14), (232, 44),
         (268, 18), (24, 84), (70, 66), (250, 78), (282, 58), (150, 62)]
for px, py in stars:
    s.ellipse((px, py, px + 5, py + 5), fill=(235, 238, 250))
# Earth arc at the bottom
s.ellipse((-60, SH - 92, SW + 60, SH + 130), fill=EARTH)
s.ellipse((30, SH - 78, 120, SH - 40), fill=(74, 148, 96))
s.ellipse((170, SH - 70, 268, SH - 34), fill=(74, 148, 96))
# satellite body
bx, by = 118, 88
s.rectangle((bx, by, bx + 64, by + 40), fill=(206, 212, 222), outline=INK, width=2)
s.rectangle((bx + 24, by - 14, bx + 40, by), fill=(150, 158, 172), outline=INK, width=2)
# solar panels
s.rectangle((bx - 78, by + 8, bx - 6, by + 32), fill=(58, 92, 168), outline=INK, width=2)
s.rectangle((bx + 70, by + 8, bx + 142, by + 32), fill=(58, 92, 168), outline=INK, width=2)
for gx in range(4):
    s.line([(bx - 66 + gx * 16, by + 8), (bx - 66 + gx * 16, by + 32)], fill=INK, width=1)
    s.line([(bx + 82 + gx * 16, by + 8), (bx + 82 + gx * 16, by + 32)], fill=INK, width=1)
# red warning ring around the satellite
s.ellipse((bx - 92, by - 34, bx + 156, by + 76), outline=ACCENT, width=5)
img.paste(scene, (sx0, sy0))
d.rectangle((sx0, sy0, sx1, sy1), outline=INK, width=2)
# lead text
tx = 380
d.text((tx, 186), "SPACE · NATO", font=F(SANS_B, 22), fill=ACCENT)
lh = F(SERIF_B, 37)
y = 216
for line in wrap("NATO vows defence against space threat", lh, W - 36 - tx - 18):
    d.text((tx, y), line, font=lh, fill=INK)
    y += 45
y += 6
ls = F(SANS, 22)
for line in wrap("Alliance chief Mark Rutte pledges to defend against any "
                 "threat in space, after reports Russia is preparing to "
                 "launch a nuclear-armed satellite.", ls, W - 36 - tx - 18):
    d.text((tx, y), line, font=ls, fill=MUTED)
    y += 28

# ---------- grid panels ----------
panels = [
    ("MYANMAR · LAW", ACCENT, "World court: genocide against Rohingya",
     "The ICJ rules Myanmar committed genocide; the UK sanctions top Myanmar generals."),
    ("GAZA", (120, 60, 140), "Israeli strikes kill six in Gaza",
     "Tuesday's airstrikes kill at least six Palestinians, including two police officers, medics say."),
    ("CONGO · HEALTH", (178, 34, 52), "Fighting traps Ebola responders",
     "Heavy fighting near a hospital in Ituri forces WHO Ebola teams to take cover for over a day."),
    ("UN · AI", (16, 110, 60), "UN chief seeks global AI rules",
     "Guterres urges member states to build a multilateral framework to limit AI risks within a year."),
    ("INDONESIA", ACCENT, "Ex-police chief charged with treason",
     "Six officials are named suspects in a wiretapping case said to target trust in President Prabowo."),
    ("BUSINESS", (196, 124, 22), "Sanofi buys Insmed for $41bn",
     "The French drugmaker's cash deal is the biggest biotech takeover in nearly three years."),
]
gx0, gy0 = 36, 434
gw, gh, gap = 468, 176, 12
for i, (kicker, kc, head, sub) in enumerate(panels):
    cx = gx0 + (i % 2) * (gw + gap)
    cy = gy0 + (i // 2) * (gh + gap)
    d.rounded_rectangle((cx, cy, cx + gw, cy + gh), radius=12, fill=CARD, outline=INK, width=2)
    d.text((cx + 18, cy + 12), kicker, font=F(SANS_B, 19), fill=kc)
    hy = cy + 40
    hf = F(SANS_B, 25)
    for line in wrap(head, hf, gw - 36):
        d.text((cx + 18, hy), line, font=hf, fill=INK)
        hy += 28
    sf = F(SANS, 19)
    for line in wrap(sub, sf, gw - 36)[:3]:
        d.text((cx + 18, hy + 2), line, font=sf, fill=MUTED)
        hy += 24

# ---------- footer ----------
fy = gy0 + 3 * gh + 2 * gap + 14
d.line([(36, fy), (W - 36, fy)], fill=INK, width=1)
centered("Compiled from the day's wire reports — BBC, Reuters, UN News / WHO and WSJ, 24 November 2026.",
         F(SANS, 16), fy + 8, MUTED)

img.save(OUT, format="PNG", optimize=True)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
