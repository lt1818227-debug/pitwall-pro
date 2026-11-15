from PIL import Image, ImageDraw, ImageFont
import os, glob
fp = next(iter(glob.glob('/usr/share/fonts/**/DejaVuSans-Bold.ttf', recursive=True)), None)
def make(size, round_=False):
    S = size*4
    im = Image.new('RGBA',(S,S),(0,0,0,0)); d = ImageDraw.Draw(im)
    bg = (8,13,20,255)
    if round_: d.ellipse((0,0,S-1,S-1), fill=bg)
    else: d.rounded_rectangle((0,0,S-1,S-1), radius=int(S*0.22), fill=bg)
    m = int(S*0.2)
    d.rounded_rectangle((m,m,S-m,S-m), radius=int(S*0.12), fill=(240,68,82,255))
    f = ImageFont.truetype(fp, int(S*0.30)) if fp else ImageFont.load_default()
    bb = d.textbbox((0,0),"PW",font=f); w,h = bb[2]-bb[0], bb[3]-bb[1]
    d.text(((S-w)/2-bb[0],(S-h)/2-bb[1]-S*0.03),"PW",font=f,fill=(255,255,255,255))
    y = int(S*0.70)
    d.rounded_rectangle((int(S*0.32),y,int(S*0.68),y+int(S*0.03)),radius=int(S*0.015),fill=(85,217,232,255))
    return im.resize((size,size), Image.LANCZOS)
RES='android/app/src/main/res'
for k,v in {'mdpi':48,'hdpi':72,'xhdpi':96,'xxhdpi':144,'xxxhdpi':192}.items():
    p=f'{RES}/mipmap-{k}'; os.makedirs(p,exist_ok=True)
    make(v).save(f'{p}/ic_launcher.png'); make(v,True).save(f'{p}/ic_launcher_round.png'); make(v).save(f'{p}/ic_launcher_foreground.png')
