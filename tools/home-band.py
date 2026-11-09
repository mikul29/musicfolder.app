"""Renders the home page's dark-band devices (also on Students) from the seeded 4.2 captures
(tools/hero-seed.py → the app's DEBUG marketing seed on the fixed simulators):

  python3 tools/home-band.py <captures-dir>

<captures-dir> holds ipad-home-portrait.png (MF iPad Pro 13 27.2, 2064 × 2752),
iphone-home-top.png (MF iPhone 17 Pro 27.2, 1206 × 2622) and ipad-home-landscape-sidebar.png
(2752 × 2064, the Mac app runs this same iPad UI). Writes assets/home-ipad.webp (13-inch
proportions), assets/home-iphone.webp and assets/home-mac.webp. The iMac is tools/imac-base.png
(the iMac, its wallpaper and an empty menu bar) with the 4.2 menu bar set in the system font and
an app window: the real Mac title bar (tools/mac-titlebar@2x.png, cut from the owner's 4.2 Mac
screenshot: traffic lights + "Music Folder") over the landscape capture below its status bar.
Headless Chrome renders each at 1×, transparent outside the device.
"""
import subprocess, sys, tempfile
from pathlib import Path
from PIL import Image

SITE = Path(__file__).resolve().parent.parent
TOOLS = SITE / 'tools'
CAP = Path(sys.argv[1]).resolve()
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
WORK = Path(tempfile.mkdtemp())
FONT = '-apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif'

def render(name, html, W, H):
    page = WORK / f'{name}.html'; page.write_text(html)
    png = WORK / f'{name}.png'
    subprocess.run([CHROME, '--headless=new', '--hide-scrollbars', '--force-device-scale-factor=1',
                    '--default-background-color=00000000', f'--user-data-dir={WORK / "chrome"}',
                    f'--window-size={W},{H}', f'--screenshot={png}', page.as_uri()], capture_output=True)
    Image.open(png).convert('RGBA').save(SITE / 'assets' / f'{name}.webp', quality=90, method=6)
    print('wrote assets/%s.webp' % name, Image.open(png).size)

# iPad / iPhone: a #0C0B0E body with a thin light rim, the screen inset, rounded (as before);
# the iPad frame now has the 13-inch screen's proportions (3 : 4)
def device(name, W, H, body_r, inset, screen_r, shot, island=None):
    isl = ''
    if island:
        x, y, w, h = island
        isl = f'<i style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{h / 2}px;background:#000"></i>'
    render(name, f'''<!doctype html><meta charset="utf-8"><style>
html,body{{margin:0;background:transparent}}
.body{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;box-sizing:border-box;border-radius:{body_r}px;
  background:#0C0B0E;box-shadow:inset 0 0 0 1px #AAAAAC,inset 0 0 0 2px #2A2A2C}}
.screen{{position:absolute;left:{inset}px;top:{inset}px;width:{W - 2 * inset}px;height:{H - 2 * inset}px;border-radius:{screen_r}px;overflow:hidden;background:#000}}
.screen img{{display:block;width:100%;height:100%;object-fit:cover;object-position:50% 0}}
</style><div class="body"><div class="screen"><img src="{(CAP / shot).as_uri()}"></div>{isl}</div>''', W, H)

device('home-ipad', 1200, 1571, 86, 44, 46, 'ipad-home-portrait.png')          # screen 1112 × 1483 = 3 : 4
device('home-iphone', 792, 1660, 121, 26, 97, 'iphone-home-top.png', (280, 46, 232, 68))

# iMac: screen area x 28–1572, menu bar y 28–58, desktop below it to y 896
land = Image.open(CAP / 'ipad-home-landscape-sidebar.png').convert('RGB')
# iPadOS draws a window-resize handle in the bottom-right corner; a Mac window has none, so the
# Mac copy repeats the pixels just to its left (background above the folder covers' tops)
patch = land.crop((2622, 1990, 2684, 2064))
land.paste(patch, (2690, 1990))
land.save(WORK / 'land-mac.png')
STATUS = 48                                   # the iPad status bar (24 pt): the Mac shows its title bar instead
cw, ch = land.width, land.height - STATUS     # window content, in capture pixels (2 px per point)
TOP, BOTTOM = 76, 880                         # the window on the desktop (as the old one sat)
TB = 24.7                                     # title bar: 32 pt at the window's scale
k = (BOTTOM - TOP - TB) / ch                  # capture px → image px
WW = round(cw * k); WX = round((1600 - WW) / 2)
tb = Image.open(TOOLS / 'mac-titlebar@2x.png')
tbk = k                                       # both are 2 px per point
menus = ''.join(f'<span>{m}</span>' for m in ['File', 'Edit', 'View', 'Chart', 'Window', 'Help'])
render('home-mac', f'''<!doctype html><meta charset="utf-8"><style>
html,body{{margin:0;background:transparent}}
.base{{position:absolute;left:0;top:0;width:1600px;height:1328px}}
.menu{{position:absolute;left:49px;top:33.5px;display:flex;gap:23.5px;font:400 15px/1 {FONT};color:#1D1D1F;letter-spacing:-0.1px;white-space:nowrap}}
.menu b{{font-weight:700;margin-right:0.5px}}
.clock{{position:absolute;right:51px;top:33.5px;font:400 15px/1 {FONT};color:#1D1D1F;letter-spacing:-0.1px;word-spacing:3px}}
.win{{position:absolute;left:{WX}px;top:{TOP}px;width:{WW}px;height:{BOTTOM - TOP}px;border-radius:10px;overflow:hidden;background:#FFF;
  box-shadow:0 0 0 0.5px rgba(0,0,0,0.28),0 22px 50px -10px rgba(0,0,0,0.38),0 6px 14px -4px rgba(0,0,0,0.18)}}
.tb{{position:absolute;left:0;top:0;right:0;height:{TB}px;background:#FFF}}
.tb img{{position:absolute;left:{12 * tbk:.2f}px;top:{(68 - 66) * tbk:.2f}px;width:{tb.width * tbk:.2f}px;height:{tb.height * tbk:.2f}px}}
.content{{position:absolute;left:0;top:{TB}px;width:{WW}px;height:{BOTTOM - TOP - TB}px;overflow:hidden}}
.content img{{position:absolute;left:0;top:{-STATUS * k:.2f}px;width:{land.width * k:.2f}px;height:{land.height * k:.2f}px}}
</style>
<img class="base" src="{(TOOLS / 'imac-base.png').as_uri()}">
<div class="menu"><b>Music Folder</b>{menus}</div><div class="clock">Mon Nov 9&nbsp; 9:41 AM</div>
<div class="win"><div class="tb"><img src="{(TOOLS / 'mac-titlebar@2x.png').as_uri()}"></div>
<div class="content"><img src="{(WORK / 'land-mac.png').as_uri()}"></div></div>''', 1600, 1328)
